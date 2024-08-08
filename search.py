import yt_dlp

def keyword_search(keyword, num):
    search_query = "ytsearch"+str(num)+":"+keyword

    # Define options for yt-dlp
    ydl_opts = {
        'format': 'best',  # You can specify the format here
    }

    # Use yt-dlp to search and retrieve video information
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Perform the search
        info_dict = ydl.extract_info(search_query, download=False)
        videos = info_dict.get('entries', [])

    # Search results
    results = []
    for idx, video in enumerate(videos):
        info = {}
        info['idx'] = idx+1
        info['title'] = video['title']
        info['uploader'] = video['uploader']
        info['url'] = video['webpage_url']
        info['thumbnail_url'] = video['thumbnail']
        info['video_id'] = video['webpage_url'].split('=')[-1]
        results.append(info)

    return results

# print(keyword_search('my chemical romance', 3))