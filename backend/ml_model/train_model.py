import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_and_save():
    # Sample dataset for sentiment analysis
    data = {
        'text': [
            # Positive
            'I love this product, it is amazing',
            'Great experience, highly recommend',
            'Fantastic service, very satisfied',
            'Excellent quality and fast delivery',
            'Best purchase I have ever made',
            'Wonderful experience, will come back',
            'The team was very helpful and kind',
            'Outstanding performance and quality',
            'Very happy with the results',
            'Superb customer service experience',
            'This platform is incredibly useful',
            'I am extremely pleased with the service',
            'Everything was perfect and smooth',
            'Amazing quality for the price',
            'Really enjoyed using this product',
            'The support team was very responsive',
            'Highly satisfied with my purchase',
            'This exceeded all my expectations',
            'Love the new features and design',
            'Impressive performance overall',
            'Very user friendly and intuitive',
            'Great value for money',
            'The product works flawlessly',
            'Absolutely brilliant experience',
            'I would definitely recommend this',
            
            # Negative
            'Terrible experience, very disappointed',
            'Worst service I have ever received',
            'The product broke after one day',
            'Very poor quality, not worth the money',
            'Awful customer support, no help at all',
            'I hate this product, complete waste',
            'Very frustrating experience overall',
            'The delivery was extremely late',
            'Product does not work as described',
            'Horrible quality and bad packaging',
            'I am very unhappy with this purchase',
            'The service was rude and unprofessional',
            'Complete disappointment with this product',
            'Never buying from here again',
            'The worst experience I have ever had',
            'This product is defective and useless',
            'Very bad quality control',
            'I regret buying this product',
            'Terrible value for the price paid',
            'Unacceptable service and quality',
            'The product failed within a week',
            'Very dissatisfied with the experience',
            'Poor communication from the team',
            'I want a full refund immediately',
            'This is a scam, do not buy',

            # Neutral
            'The product is okay, nothing special',
            'Average experience, meets basic needs',
            'It works fine for the price',
            'Standard quality, as expected',
            'Delivery was on time, product is decent',
            'Normal product, does what it says',
            'It is an average product overall',
            'Nothing remarkable but not bad either',
            'The service was adequate',
            'Regular experience, no complaints',
            'It is a basic product',
            'Average quality for this price range',
            'The product does its job',
            'Not great not terrible just fine',
            'Meets minimum expectations',
        ],
        'sentiment': [
            # Positive labels
            'positive', 'positive', 'positive', 'positive', 'positive',
            'positive', 'positive', 'positive', 'positive', 'positive',
            'positive', 'positive', 'positive', 'positive', 'positive',
            'positive', 'positive', 'positive', 'positive', 'positive',
            'positive', 'positive', 'positive', 'positive', 'positive',
            
            # Negative labels
            'negative', 'negative', 'negative', 'negative', 'negative',
            'negative', 'negative', 'negative', 'negative', 'negative',
            'negative', 'negative', 'negative', 'negative', 'negative',
            'negative', 'negative', 'negative', 'negative', 'negative',
            'negative', 'negative', 'negative', 'negative', 'negative',

            # Neutral labels
            'neutral', 'neutral', 'neutral', 'neutral', 'neutral',
            'neutral', 'neutral', 'neutral', 'neutral', 'neutral',
            'neutral', 'neutral', 'neutral', 'neutral', 'neutral',
        ]
    }

    df = pd.DataFrame(data)
    
    # Vectorize text
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['text'])
    y = df['sentiment']

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f"Model trained successfully! Accuracy: {accuracy:.2f}")

    # Save model and vectorizer
    model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump({'model': model, 'vectorizer': vectorizer}, f)
    
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    train_and_save()
