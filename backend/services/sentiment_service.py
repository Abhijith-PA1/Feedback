import pickle
import os
import threading

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ml_model', 'sentiment_model.pkl')

class SentimentAnalyzer:
    """Thread-safe singleton for sentiment analysis"""
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Load the ML model and vectorizer"""
        self.model = None
        self.vectorizer = None
        try:
            with open(MODEL_PATH, 'rb') as f:
                data = pickle.load(f)
                self.model = data['model']
                self.vectorizer = data['vectorizer']
        except FileNotFoundError:
            print("Warning: Sentiment model not found. Run train_model.py first.")
    
    def predict(self, text):
        """Predict sentiment for given text"""
        if self.model is None or self.vectorizer is None:
            return 'neutral'
        
        text_vectorized = self.vectorizer.transform([text])
        prediction = self.model.predict(text_vectorized)[0]
        return prediction

# Create singleton instance
_analyzer = SentimentAnalyzer()

def predict_sentiment(text):
    """Public API for sentiment prediction"""
    return _analyzer.predict(text)
