# 根据params列表获取音乐本体链接
import requests
import re

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://www.kugou.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kugou.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

params = {
    'srcappid': '2919',
    'clientver': '20000',
    'clienttime': '1762753956302',
    'mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'uuid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
    'appid': '1014',
    'platid': '4',
    'encode_album_audio_id': '1plx3hfe',
    'token': 'eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377',
    'userid': '698985232',
    'signature': 'eb7a8af478cf8bba76d838d74d8a700d'
}

response = requests.get('https://wwwapi.kugou.com/play/songinfo', params=params, headers=headers)

pattern = r'"play_url":"([^"]+)"'
match = re.search(pattern, response.text)

if match:
    play_url = match.group(1).replace('\\/', '/')
    print(play_url)