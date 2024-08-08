# from requests import get
# from youtube_dl import YoutubeDL

# YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

# def search(arg):
#     with YoutubeDL(YDL_OPTIONS) as ydl:
#         try:
#             get(arg) 
#         except:
#             entries = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries']
#             print("Length of Entries :", len(entries))
#             video = entries[0]
#         else:
#             video = ydl.extract_info(arg, download=False)

#     return video


# print(search('한로로'))
import yt_dlp

# Define the search query
search_query = "ytsearch5:Hanroro"

# Define options for yt-dlp
ydl_opts = {
    'format': 'best',  # You can specify the format here
}

# Use yt-dlp to search and retrieve video information
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Perform the search
    info_dict = ydl.extract_info(search_query, download=False)
    videos = info_dict.get('entries', [])

# Print the search results
for idx, video in enumerate(videos):
    print(f"Result {idx+1}:")
    print(f"Title: {video['title']}")
    print(f"Uploader: {video['uploader']}")
    print(f"URL: {video['webpage_url']}\n")
