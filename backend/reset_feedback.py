"""
Script to reset all feedback records in the database
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.db import db
from models.feedback_model import Feedback
from app import create_app

def reset_feedback():
    """Delete all feedback records from the database"""
    app = create_app()
    with app.app_context():
        try:
            # Count existing records
            count = Feedback.query.count()
            print(f"\n{'='*60}")
            print(f"Current feedback records: {count}")
            print(f"{'='*60}\n")
            
            if count == 0:
                print("✅ No feedback records to delete. Database is already empty.")
                return
            
            # Delete all feedback records
            deleted = Feedback.query.delete()
            db.session.commit()
            
            # Verify deletion
            remaining = Feedback.query.count()
            
            print(f"{'='*60}")
            print(f"✅ Successfully deleted {deleted} feedback record(s)")
            print(f"Remaining records: {remaining}")
            print(f"{'='*60}\n")
            
            if remaining == 0:
                print("🎉 All feedback records have been reset to 0!")
            else:
                print(f"⚠️ Warning: {remaining} records still remain")
                
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error resetting feedback: {str(e)}")
            sys.exit(1)

if __name__ == '__main__':
    print("\n🔄 Resetting Feedback Records...")
    reset_feedback()
