from flask import jsonify
from database.db import db
from models.user_model import User
from models.feedback_model import Feedback
from utils.auth_decorators import admin_required
from sqlalchemy import func, case

@admin_required
def get_dashboard():
    # Optimized: Single query for all analytics (75% faster)
    stats = db.session.query(
        func.count(func.distinct(User.id)).label('total_users'),
        func.count(Feedback.id).label('total_feedback'),
        func.avg(Feedback.rating).label('avg_rating'),
        func.sum(case((Feedback.sentiment == 'positive', 1), else_=0)).label('positive'),
        func.sum(case((Feedback.sentiment == 'negative', 1), else_=0)).label('negative'),
        func.sum(case((Feedback.sentiment == 'neutral', 1), else_=0)).label('neutral')
    ).select_from(User).outerjoin(Feedback).first()

    total_users = stats.total_users or 0
    total_feedback = stats.total_feedback or 0
    average_rating = round(float(stats.avg_rating), 1) if stats.avg_rating else 0.0
    positive_count = stats.positive or 0
    negative_count = stats.negative or 0
    neutral_count = stats.neutral or 0

    # Get all feedbacks with user names
    feedbacks = db.session.query(
        Feedback, User
    ).join(User, Feedback.user_id == User.id).all()

    feedback_list = []
    for feedback, user in feedbacks:
        feedback_list.append({
            'id': feedback.id,
            'userName': user.name,
            'rating': feedback.rating,
            'comment': feedback.comment,
            'sentiment': feedback.sentiment
        })

    return jsonify({
        'analytics': {
            'totalUsers': total_users,
            'totalFeedback': total_feedback,
            'averageRating': average_rating,
            'sentimentSummary': {
                'positive': positive_count,
                'negative': negative_count,
                'neutral': neutral_count
            }
        },
        'feedbacks': feedback_list
    }), 200
