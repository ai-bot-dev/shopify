from flask import Flask, request, jsonify, render_template
import openai
import json

app = Flask(__name__)

API_KEY = "your_openrouter_api_key"

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# Load Shopify store data
with open("store_data.json", "r") as f:
    store_data = json.load(f)

# AI chatbot function
def chat_with_ai(user_message):
    prompt = f"""
    You are a Shopify AI chatbot that answers questions about products, orders, and store policies.

    Products:
    {store_data["products"]}

    Orders:
    {store_data["orders"]}

    Customer Question: {user_message}
    AI Response:
    """
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Chat API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    ai_response = chat_with_ai(user_message)
    return jsonify({"response": ai_response})

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
