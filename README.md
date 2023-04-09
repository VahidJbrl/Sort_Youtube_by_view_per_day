# Sort Youtube channel videos by view per day
YouTube Channel Video Sorter (by view per day)

**Description:**

This Python script fetches all videos from a given YouTube channel and sorts them by their average views per day. The results are displayed in the console and saved as an Excel file for further analysis.

**Features:**

• Supports standard channel URLs with '/channel/' or '/user/' and custom URLs with the '@' symbol

• Fetches all videos from the channel using the YouTube Data API v3

• Calculates the average views per day for each video

• Sorts the videos in descending order based on their average views per day

• Saves the sorted list of videos with their titles, URLs, and views per day to an Excel file

**Usage:**

1. Obtain a YouTube Data API v3 key from the Google Developers Console

2. Replace the 'api_key' variable in the script with your API key

3. Install the required libraries using 'pip'

pip install google-api-python-client pandas openpyxl

4. Run the script:

python youtube_channel_video_sorter.py

5. Enter the YouTube channel URL when prompted

The script will fetch all videos from the channel, calculate their average views per day, and display the sorted list in the console. The results will also be saved as an Excel file named sorted_videos.xlsx in the same directory as the script.

**To obtain a YouTube Data API v3 key, follow these steps:**

1. Go to the Google Developers Console: https://console.developers.google.com/

2. Log in with your Google account or create a new one if necessary.

3. Click the "Select a project" dropdown at the top right corner, and then click the "New Project" button in the modal window that appears.

4. Enter a project name, select an organization and a location (if applicable), and click "Create."

5. Once the project is created, you'll be redirected to the project dashboard. In the left sidebar, click on "APIs & Services" and then "Dashboard."

6. In the API Dashboard, click on "+ ENABLE APIS AND SERVICES" at the top.

7. In the API Library, search for "YouTube Data API v3" using the search bar, and click on it when it appears in the search results.

8. On the YouTube Data API v3 page, click "Enable" to enable the API for your project.

9. After enabling the API, click "Create Credentials" on the API page.

10. In the "Add credentials to your project" form, select "YouTube Data API v3" for the "Which API are you using?" question, select "Other non-UI (e.g. cron job, daemon)" for the "Where will you be calling the API from?" question, and select "Public data" for the "What data will you be accessing?" question. Then, click "What credentials do I need?"

11. The API key will be generated. Click the "Copy" button to copy the API key, and click "Done."

12. Now that you have the API key, replace the 'api_key' variable in the script with your API key. Make sure to keep the API key secret and not share it publicly, as it grants access to your Google Developer Console project and its associated resources.
