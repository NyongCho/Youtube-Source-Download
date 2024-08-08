import yt_dlp

url = 'https://www.youtube.com/watch?v=hT4vALZ8C64'

ydl_opts = {
    'format':'best',
    'outtmpl':'%(title)s.%(ext)s',
    # 'postprocessors': [
    #     {
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     },
    #     {
    #         'key': 'FFmpegMetadata',
    #     },
    # ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    # print(ydl.extract_info(url, download=True))