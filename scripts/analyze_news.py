import requests

# Function to analyze news using DeepSeek API

def analyze_news_deepseek(news_article):
    # Your DeepSeek API endpoint
    deepseek_api_url = 'https://api.deepseek.ai/analyze'
    payload = {'article': news_article}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(deepseek_api_url, json=payload, headers=headers)
    return response.json()

# Function to analyze news using Qwen API

def analyze_news_qwen(news_article):
    # Your Qwen API endpoint
    qwen_api_url = 'https://api.qwen.ai/analyze'
    payload = {'article': news_article}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(qwen_api_url, json=payload, headers=headers)
    return response.json()

# Example usage
if __name__ == '__main__':
    article = "Your news article content goes here"
    deepseek_analysis = analyze_news_deepseek(article)
    qwen_analysis = analyze_news_qwen(article)
    print('DeepSeek Analysis:', deepseek_analysis)
    print('Qwen Analysis:', qwen_analysis)