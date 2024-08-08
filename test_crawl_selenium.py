from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def youtube_search(query):
    # ChromeDriver 경로 설정
    driver_path = '/path/to/chromedriver'  # ChromeDriver 경로로 변경
    driver = webdriver.Chrome(driver_path)

    try:
        # YouTube 검색 페이지 열기
        driver.get('https://www.youtube.com')

        # 검색창 찾기 및 검색어 입력
        search_box = driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # 검색 결과가 로드될 때까지 대기
        time.sleep(5)

        # 검색 결과 파싱
        results = []
        videos = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        for video in videos:
            title = video.get_attribute('title')
            url = video.get_attribute('href')
            channel_elem = video.find_element(By.XPATH, '../..//*[@id="text"]/a')
            channel = channel_elem.text if channel_elem else 'Unknown'
            results.append({'title': title, 'channel': channel, 'url': url})

        return results

    finally:
        driver.quit()

# 예제 실행
if __name__ == "__main__":
    query = "Python tutorial"
    results = youtube_search(query)
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Channel: {result['channel']}")
        print(f"URL: {result['url']}")
        print()
