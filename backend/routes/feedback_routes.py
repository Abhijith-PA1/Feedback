from flask import Blueprint
from controllers.feedback_controller import submit_feedback

feedback_bp = Blueprint('feedback', __name__)

feedback_bp.route('', methods=['POST'])(submit_feedback)
