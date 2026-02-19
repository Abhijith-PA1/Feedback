import sqlite3
import os

def view_all_feedback():
    """View all feedback stored in the database"""
    
    # Connect to database
    db_path = os.path.join('instance', 'database.db')
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at: {db_path}")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get total counts
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM feedbacks")
    total_feedback = cursor.fetchone()[0]
    
    print("=" * 80)
    print("📊 FEEDBACK DATABASE VIEWER")
    print("=" * 80)
    print(f"Database: {os.path.abspath(db_path)}")
    print(f"Total Users: {total_users}")
    print(f"Total Feedback: {total_feedback}")
    print("=" * 80)
    
    if total_feedback == 0:
        print("\n⚠️  No feedback found in database.")
        print("Submit some feedback through the web app first!")
        conn.close()
        return
    
    # Query all feedback with user information
    query = """
    SELECT 
        f.id,
        u.name as user_name,
        u.email,
        f.rating,
        f.comment,
        f.sentiment
    FROM feedbacks f
    JOIN users u ON f.user_id = u.id
    ORDER BY f.id DESC
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    print(f"\n📝 ALL FEEDBACK RECORDS ({len(results)} total)\n")
    
    for row in results:
        feedback_id, user_name, email, rating, comment, sentiment = row
        
        # Create star rating visual
        stars = "⭐" * rating + "☆" * (5 - rating)
        
        # Color code sentiment
        sentiment_emoji = {
            'positive': '😊',
            'negative': '😞',
            'neutral': '😐'
        }.get(sentiment, '❓')
        
        print(f"┌─ Feedback ID: {feedback_id} " + "─" * 60)
        print(f"│ 👤 User: {user_name} ({email})")
        print(f"│ ⭐ Rating: {stars} ({rating}/5)")
        print(f"│ 💬 Comment: {comment}")
        print(f"│ {sentiment_emoji} Sentiment: {sentiment.upper()}")
        print(f"└" + "─" * 78)
        print()
    
    # Show sentiment summary
    cursor.execute("""
        SELECT sentiment, COUNT(*) as count
        FROM feedbacks
        GROUP BY sentiment
    """)
    sentiment_counts = cursor.fetchall()
    
    print("=" * 80)
    print("📊 SENTIMENT SUMMARY")
    print("=" * 80)
    for sentiment, count in sentiment_counts:
        percentage = (count / total_feedback) * 100
        emoji = {'positive': '😊', 'negative': '😞', 'neutral': '😐'}.get(sentiment, '❓')
        print(f"{emoji} {sentiment.capitalize()}: {count} ({percentage:.1f}%)")
    
    # Show average rating
    cursor.execute("SELECT AVG(rating) FROM feedbacks")
    avg_rating = cursor.fetchone()[0]
    print(f"\n⭐ Average Rating: {avg_rating:.2f}/5.00")
    print("=" * 80)
    
    conn.close()

if __name__ == '__main__':
    view_all_feedback()
