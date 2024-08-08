from flask import Flask, request, render_template, jsonify, send_file
from search import keyword_search
from crawl_search import crawl_search
from apscheduler.schedulers.background import BackgroundScheduler
from glob import glob
import yt_dlp
import time
import os

def scheduler():
    tmp_list = glob('*.mp*')
    for path  in tmp_list:
        os.remove(path)
        print("Removed ", path)

schedule = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
schedule.add_job(scheduler, 'interval', minutes=10)
schedule.start()

app = Flask(__name__)

# 홈 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 검색 요청 처리
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    search_results = crawl_search(keyword, 5)
    # print(search_results)
    return jsonify(search_results)

@app.route('/download-video', methods=['POST'])
def download_video():
    data = request.json
    url = data['url']
    title = data['title']
    
    file_path = title+'.mp4'

    ydl_opts = {
        'format': 'bestv',
        'outtmpl': file_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file(file_path, as_attachment=True, download_name=f"{title}.mp4")

@app.route('/download-mp3', methods=['POST'])
def download_mp3():
    data = request.json
    url = data['url']
    title = data['title']

    ydl_opts = {
        'format': 'best',
        'outtmpl': title,
        'quiet': True,
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'FFmpegMetadata',
            },
        ],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # file_path = glob('*.mp3')[0]
    # print(file_path)
    return send_file(title+'.mp3', as_attachment=True, download_name=f"{title}.mp3")

if __name__ == '__main__':
    app.run(debug=True)