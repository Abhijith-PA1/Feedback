from flask import jsonify, request
from database.db import db
from models.feedback_model import Feedback
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.sentiment_service import predict_sentiment

@jwt_required()
def submit_feedback():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Request body is required'}), 400

    rating = data.get('rating')
    comment = data.get('comment', '').strip()

    if not rating or not comment:
        return jsonify({'error': 'Rating and comment are required'}), 400

    if not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    # Get user ID from JWT
    user_id = get_jwt_identity()
    
    # Predict sentiment using ML model
    sentiment = predict_sentiment(comment)

    # Save feedback
    new_feedback = Feedback(
        user_id=int(user_id),
        rating=rating,
        comment=comment,
        sentiment=sentiment
    )
    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({
        'message': 'Feedback submitted successfully!',
        'sentiment': sentiment
    }), 201
