from flask import Blueprint
from controllers.admin_controller import get_dashboard

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/dashboard', methods=['GET'])(get_dashboard)
