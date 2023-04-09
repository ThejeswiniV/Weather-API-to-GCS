# Weather-API-to-GCS
## Building a Cloud Function to Fetch and Store Weather Data(OpenMeteo) in Cloud Storage.
 
We'll start by setting up a Cloud Storage bucket and then create a Cloud Function that makes an API request to fetch the weather data. The function will then store the data in a file in the Cloud Storage bucket.


## What we will need for this tutorial:

1. One free API to get various information on weather conditions all around the globe(OpenMeteo).
2. In this article, we will use some service from Google: Cloud Storage, Cloud Function, Cloud Scheduler.
3. Make sure your cloud function service account have Storage Object Creator.


# Step:1 Create Cloud Storage:
  
  Create new bucket my_storage_11 with location type asia-south1(Mumbai).

# Step:2 Create job in Cloud Scheduler: 
  
Create a new job and start by defining:
1. Name Weather_Job, Region asia-south1(Mumbai),
2. Frequency, Schedule specific using crontab format (00 00 * * *) and Timezone (IST),
3. Configure Target type as Pub/Sub,
4. Create a Topic, Topic ID "weather",
5. Message body as "update",
6. Click Create.

# Step:3 Create Cloud function:

Note: Cloud Functions can be considered as small containers that will execute the code within them. 

They support different languages such as: .NEt, Go, Java, Node, PHP, Python, or Ruby.

1. We create a function called "Weather_update", Region "asia-south1" and triggered by "Pub/Sub" messages of the "weather" topic.

2. Now Configuration is over, Let's move to code, Choose "Python 3.9" as runtime and Entry point as "api_to_gcs"

3. main.py

4. requirements.txt

5. Click on "Deploy" and wait for the Cloud Function to be active:

As we want to make sure that the function is working well, we click on "Test function" to immediately run it:
The logs do confirm the proper execution of the function.

6.Check your data will be available in GCS.
