import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

def train_and_save():
    print("Loading EmotionDetection.csv dataset...")
    
    # Load the dataset
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'EmotionDetection.csv')
    df = pd.read_csv(csv_path)
    
    print(f"Dataset loaded: {df.shape[0]} samples, {df['Emotion'].nunique()} emotions")
    print(f"\nEmotion distribution:")
    print(df['Emotion'].value_counts())
    
    # Prepare data
    X = df['text']
    y = df['Emotion']
    
    # Map emotions to sentiment categories for feedback system
    emotion_to_sentiment = {
        'happiness': 'positive',
        'love': 'positive',
        'enthusiasm': 'positive',
        'fun': 'positive',
        'relief': 'positive',
        'surprise': 'positive',
        
        'sadness': 'negative',
        'anger': 'negative',
        'hate': 'negative',
        'worry': 'negative',
        'empty': 'negative',
        'boredom': 'negative',
        
        'neutral': 'neutral'
    }
    
    # Create sentiment labels
    y_sentiment = y.map(emotion_to_sentiment)
    
    print(f"\nSentiment distribution:")
    print(y_sentiment.value_counts())
    
    # Split data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_sentiment, test_size=0.2, random_state=42, stratify=y_sentiment
    )
    
    print(f"\nTraining set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")
    
    # Vectorize text using TF-IDF (better than CountVectorizer)
    print("\nVectorizing text with TF-IDF...")
    vectorizer = TfidfVectorizer(
        max_features=5000,  # Top 5000 features
        ngram_range=(1, 2),  # Unigrams and bigrams
        min_df=5,  # Ignore terms that appear in less than 5 documents
        stop_words='english'
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print(f"Vocabulary size: {len(vectorizer.vocabulary_)}")
    
    # Train model with better parameters
    print("\nTraining Logistic Regression model...")
    model = LogisticRegression(
        max_iter=1000,
        random_state=42,
        C=1.0,  # Regularization strength
        solver='lbfgs',
        class_weight='balanced'  # Handle class imbalance
    )
    model.fit(X_train_vec, y_train)
    
    # Evaluate model
    print("\nEvaluating model...")
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n{'='*60}")
    print(f"Model Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"{'='*60}")
    
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Test with sample sentences
    print("\n" + "="*60)
    print("Testing with sample sentences:")
    print("="*60)
    
    test_sentences = [
        "I love this product, it's amazing!",
        "This is terrible, I hate it",
        "It's okay, nothing special",
        "I'm so happy and excited!",
        "I feel sad and disappointed",
        "The service was excellent and wonderful",
        "Worst experience ever, very angry",
        "Average quality, meets expectations"
    ]
    
    for sentence in test_sentences:
        vec = vectorizer.transform([sentence])
        prediction = model.predict(vec)[0]
        probabilities = model.predict_proba(vec)[0]
        confidence = max(probabilities) * 100
        print(f"\nText: '{sentence}'")
        print(f"Prediction: {prediction} (confidence: {confidence:.1f}%)")
    
    # Save model and vectorizer
    model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump({
            'model': model,
            'vectorizer': vectorizer,
            'accuracy': accuracy,
            'emotion_mapping': emotion_to_sentiment
        }, f)
    
    print(f"\n{'='*60}")
    print(f"✅ Model saved successfully to: {model_path}")
    print(f"{'='*60}")
    print(f"\nModel Statistics:")
    print(f"  - Training samples: {len(X_train):,}")
    print(f"  - Test samples: {len(X_test):,}")
    print(f"  - Accuracy: {accuracy*100:.2f}%")
    print(f"  - Features: {len(vectorizer.vocabulary_):,}")
    print(f"  - Classes: {len(model.classes_)}")
    print(f"\n🎉 Model training complete!")

if __name__ == '__main__':
    train_and_save()
