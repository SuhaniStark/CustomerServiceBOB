import pandas as pd
from transformers import pipeline

# Load pretrained model and tokenizer from Hugging Face
chatbot = pipeline('text-generation', model='gpt-3.5-turbo')

# Sample customer interaction data
data = {
    'customer_id': [1, 2, 1, 3],
    'interaction': [
        'Looking for a new laptop', 
        'Need help with my phone bill', 
        'Interested in gaming laptops', 
        'Want to switch my internet plan'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

def get_customer_history(customer_id):
    # Get past interactions of a customer
    customer_history = df[df['customer_id'] == customer_id]['interaction'].tolist()
    return customer_history

def generate_recommendation(history):
    # Concatenate interaction history
    history_text = " ".join(history)
    # Generate recommendation
    response = chatbot(f"Based on the history: {history_text} What would you recommend?")
    return response[0]['generated_text']

def update_recommendations(customer_id):
    # Get customer history
    history = get_customer_history(customer_id)
    if history:
        # Generate and return recommendation
        recommendation = generate_recommendation(history)
        return recommendation
    else:
        return "No interaction history found for this customer."

# Example usage
customer_id = 1
recommendation = update_recommendations(customer_id)
print(f"Recommendation for customer {customer_id}: {recommendation}")
