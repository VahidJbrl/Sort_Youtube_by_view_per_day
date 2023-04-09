# Sort_Youtube_by_view_per_day
YouTube Channel Video Sorter (by view per day)

Description:
This Python script fetches all videos from a given YouTube channel and sorts them by their average views per day. The results are displayed in the console and saved as an Excel file for further analysis.

Features:
• Supports standard channel URLs with '/channel/' or '/user/' and custom URLs with the '@' symbol
• Fetches all videos from the channel using the YouTube Data API v3
• Calculates the average views per day for each video
• Sorts the videos in descending order based on their average views per day
• Saves the sorted list of videos with their titles, URLs, and views per day to an Excel file

Requirements:
• Python 3.6 or higher
• Google API client library for Python ( 'googLe-api-python-client')
• 'pandas" and 'openpyxl' libraries for handling and exporting data to Excel

Usage:
1. Obtain a YouTube Data API v3 key from the Google Developers Console
2. Replace the 'api_key' variable in the script with your API key
3. Install the required libraries using 'pip'
pip install google-api-python-client pandas openpyxl
4. Run the script:
python youtube_channel_video_sorter.py
5. Enter the YouTube channel URL when prompted
The script will fetch all videos from the channel, calculate their average views per day, and display the sorted list in the console. The results will also be saved as an Excel file named sorted_videos.xlsx in the same directory as the script.
