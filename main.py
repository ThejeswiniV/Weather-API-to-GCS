import requests
from google.cloud import storage

def fetch_and_upload(data, context):
    # API URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=12.74&longitude=77.83&hourly=rain&daily=weathercode,sunrise,sunset,rain_sum&current_weather=true&timezone=Asia%2FSingapore"
    
    # Fetch news data from API
    response = requests.get(url)
    
    # Initialize Google Cloud Storage client
    client = storage.Client()

    # Get Cloud Storage bucket
    bucket_name = 'my_storage_11'
    bucket = client.bucket(bucket_name)

    # Upload news data to Cloud Storage
    blob = bucket.blob("weather_data.csv")
    blob.upload_from_string(response.content)

    return f"News data uploaded to Cloud Storage successfully!: {bucket_name}"
