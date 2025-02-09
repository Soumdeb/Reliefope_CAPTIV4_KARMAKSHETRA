import requests

def send_sms_alert(phone_number, message):
    """Sends an SMS alert using Twilio API."""
    from twilio.rest import Client

    account_sid = "YOUR_TWILIO_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_="YOUR_TWILIO_PHONE",
        to=phone_number
    )

def get_real_time_disaster_updates():
    """Fetches disaster updates from an API."""
    response = requests.get("https://api.reliefweb.int/v1/reports")
    if response.status_code == 200:
        return response.json()
    return None
