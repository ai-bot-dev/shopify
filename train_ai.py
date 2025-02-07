import openai
import json

API_KEY = "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"

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# Load Shopify store data
with open("store_data.json", "r") as f:
    store_data = json.load(f)

# Train AI with store data
def train_ai():
    training_text = f"""
    Products:
    {store_data["products"]}

    Orders:
    {store_data["orders"]}
    """

    return training_text

# Train AI model
ai_training_data = train_ai()
print("AI is now trained on Shopify store data.")
