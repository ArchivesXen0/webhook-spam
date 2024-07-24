import requests
import time

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "YOUR_WEBHOOK_URL"

# List of messages to send
messages = [
    "NEW SERVER JOIN https://discord.gg/mWDZhtNvXM",
    "NEW SERVER JOIN https://discord.gg/cnGnAWbp",
    "NEW SERVER JOIN https://discord.gg/yK2BSEtRkp"
]

# Function to send a message to the Discord webhook
def send_message(content):
    data = {
        "content": content
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"Message sent: {content}")
    else:
        print(f"Failed to send message: {response.status_code}")

# Spam the webhook with messages
while True:
    for message in messages:
        send_message(message)
        time.sleep(1)  # Delay between messages
