#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:44:45 2023

@author: vahid
"""

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import datetime
import pandas as pd

api_key = "api_key"  # Replace with your YouTube Data API key

def get_channel_videos(channel_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    videos = []
    page_token = None

    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=page_token,  # Add the pageToken parameter for pagination
            order="date",
            type="video"
        )

        response = request.execute()
        for item in response["items"]:
            video_id = item["id"]["videoId"]
            video_title = item["snippet"]["title"]
            published_at = item["snippet"]["publishedAt"]
            videos.append((video_id, video_title, published_at))

        # Check if there's a nextPageToken, and if not, break the loop
        if "nextPageToken" in response:
            page_token = response["nextPageToken"]
        else:
            break

    return videos


def get_video_stats(video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    
    response = request.execute()
    video_stats = response["items"][0]["statistics"]
    
    return video_stats

def sort_videos_by_views_per_day(videos):
    video_stats = [(video[0], video[1], get_video_stats(video[0]), video[2]) for video in videos]
    video_views_per_day = []
    
    for video in video_stats:
        video_id, video_title, stats, published_at = video
        view_count = int(stats["viewCount"])
        published_date = datetime.datetime.fromisoformat(published_at[:-1])
        days_since_published = (datetime.datetime.now() - published_date).days
        views_per_day = view_count / (days_since_published + 1)  # Add 1 to avoid ZeroDivisionError
        video_views_per_day.append((video_title, views_per_day, video_id))
    
    video_views_per_day.sort(key=lambda x: x[1], reverse=True)
    
    return video_views_per_day

def get_channel_id_from_username(username):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    
    request = youtube.channels().list(
        part="id",
        forUsername=username
    )
    
    response = request.execute()
    
    if "items" not in response or len(response["items"]) == 0:
        print("Invalid YouTube channel username.")
        return None

    channel_id = response["items"][0]["id"]
    
    return channel_id


import re

def main():
    channel_url = input("Enter the YouTube channel URL: ")
    channel_id_match = re.search(r"(/channel/|/user/|@)([^/]+)", channel_url)  # Update the regular expression to include the @ symbol
    
    if not channel_id_match:
        print("Invalid YouTube channel URL.")
        return

    channel_id = channel_id_match.group(2)
    if channel_id_match.group(1) == "/user/" or channel_id_match.group(1) == "@":  # Check for the @ symbol in the URL
        # Retrieve channel ID from the user name
        channel_id = get_channel_id_from_username(channel_id)

    videos = get_channel_videos(channel_id)
    sorted_videos = sort_videos_by_views_per_day(videos)
    
    print("Sorted videos by views per day:")
    video_data = []
    for video in sorted_videos:
        title, views_per_day, video_id = video
        url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"{title} ({url}): {views_per_day:.2f} views per day")
        video_data.append({"Title": title, "URL": url, "Views Per Day": views_per_day})

    df = pd.DataFrame(video_data)
    output_filename = "sorted_videos.xlsx"
    df.to_excel(output_filename, index=False, engine='openpyxl')

    print(f"\nResults saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
