from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os

# Get the HTML of the stuff.html file in the same directory
with open('stuff.html', 'r') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all 'a' tags with 'href' starting with '/watch?v='
video_tags = soup.find_all('a', href=True)

# Extract the video links
video_links = list(set([tag['href'] for tag in video_tags if tag['href'].startswith('/watch?v=')]))
print(video_links)

# If you want the full YouTube URL, you can add 'https://www.youtube.com' before each link
full_links = ['https://www.youtube.com' + link for link in video_links]

# Destination directory
destination = './jonhoo'
if not os.path.exists(destination):
    os.makedirs(destination)

# Iterate through all videos in the playlist
for url in video_links:
    try:
        yt = YouTube(url)

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # Check if file already exists
        new_file = os.path.join(destination, yt.title + '.mp3')
        if not os.path.exists(new_file):
            # download the file
            out_file = video.download(output_path=destination)

            # save the file
            base, ext = os.path.splitext(out_file)
            os.rename(out_file, new_file)

            # result of success
            print(yt.title + " has been successfully downloaded.")
        else:
            print(yt.title + " already exists. Skipping download.")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}. Moving to next video.")
