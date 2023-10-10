import requests
import json
from bs4 import BeautifulSoup

# API endpoint URL, replace it with your actual URL
API_URL = "http://localhost:8000/predict"  # Replace with your actual API endpoint if different

# 20 Product reviews with sentiments that aren't immediately obvious
reviews = [
    "The product does its job, but I've seen better.",
    "Works well most of the time.",
    "Not bad, but could be improved.",
    "Does what it's supposed to do, nothing more, nothing less.",
    "It's okay for the price.",
    "A solid choice if you're not looking for anything fancy.",
    "Good, but leaves room for improvement.",
    "It's not the best, but it's not the worst either.",
    "I'm somewhat satisfied with this product.",
    "Better than I expected, but still not great.",
    "Decent for everyday use.",
    "I have mixed feelings about this product.",
    "Okayish, but I expected more for the price.",
    "It's good, but not good enough for me to buy it again.",
    "Not terrible, but I wouldn't purchase again.",
    "Could be worse, but also could be much better.",
    "I guess you get what you pay for.",
    "Somewhat underwhelming, but not a total waste.",
    "Fine for now, but I'll be looking for something better.",
    "Serves its purpose, but I'm not blown away."
]

# Loop through each review and post it to the API
responses = []
for review in reviews:
    # Prepare data payload
    data = {'review': review}
    
    # Post the data to the API and get the response
    try:
        response = requests.post(API_URL, data=data)
        if response.status_code == 200:
            # Parse the HTML response with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the paragraph containing the sentiment analysis
            sentiment_analysis = soup.find('p').text
            
            # Remove the prefix to keep only the sentiment
            sentiment = sentiment_analysis.replace("Your review is: ", "")
            
            print(f"Review: '{review}'\nSentiment Analysis: {sentiment}\n")
        else:
            print(f"Failed to analyze the review: '{review}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
