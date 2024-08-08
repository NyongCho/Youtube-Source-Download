import requests

def crawl_search(keyword, num):
    url = 'https://www.youtube.com/results?search_query='+keyword
    yt = requests.get(url).text

    url_pre_text = '"commandMetadata":{"webCommandMetadata":{"url":"/watch'
    title_pre_text = '"title":{"runs":[{"text":"'
    info_pre_text = '"}],"accessibility":{"accessibilityData":{"label":"'

    urls = []
    titles = []
    ytdotcom = 'https://youtube.com'

    idx = 0
    while True:
        yt = yt[idx:]
        if info_pre_text in yt:
            idx = yt.find(info_pre_text)
            titles.append(yt[idx+len(info_pre_text):idx+len(info_pre_text)+yt.find('\"')])

            if url_pre_text in yt:
                idx = yt.find(url_pre_text)
                end = 68#yt[idx:].find('\\')
                element = yt[idx+48:idx+end]
                idx += 1

                urls.append(ytdotcom+element)
            # print(urls[-1])
            else:
                break
        else:
            break

    urls = list(set(urls))[:num]
    titles = list(set(titles))[:num]
    print(len(titles))

    results = []
    for idx, e in enumerate(zip(titles, urls)):
        info = {}
        info['idx'] = idx+1
        info['title'] = e[0]
        info['uploader'] = ''
        info['url'] = e[1]
        info['thumbnail_url'] = ''
        info['video_id'] = e[1].split('=')[-1]
        results.append(info)

    return results

# print(crawl_search('한로로', 5))