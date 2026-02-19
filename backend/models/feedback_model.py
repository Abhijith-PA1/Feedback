from database.db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    __table_args__ = (
        db.Index('idx_feedback_user_id', 'user_id'),
        db.Index('idx_feedback_sentiment', 'sentiment'),
        db.Index('idx_feedback_rating', 'rating'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), default='neutral')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'sentiment': self.sentiment
        }
