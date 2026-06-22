import hashlib

param_list = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    "clienttime=1763909893890",
    "clientver=20000",
    "dfid=1bq5wP3V9dAI106DWJ2Px1xI",
    "encode_album_audio_id=1t7lpt5b",
    "mid=fb92a6fbada0f5060cf0f5058f1d800e",
    "platid=4",
    "srcappid=2919",
    "token=eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377",
    "userid=698985232",
    "uuid=fb92a6fbada0f5060cf0f5058f1d800e",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]

signature = hashlib.md5(''.join(param_list).encode('utf-8')).hexdigest()
t = "1763909893890"
encode_album_audio_id = "1t7lpt5b"

import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://www.kugou.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kugou.com/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

params = {
    'srcappid': '2919',
    'clientver': '20000',
    'clienttime': t,
    'mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'uuid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
    'appid': '1014',
    'platid': '4',
    'encode_album_audio_id': encode_album_audio_id,
    'token': 'eea2079550f7563bea339ed7920fedf4f0091311a172e24c1462309aaff604f4',
    'userid': '698985232',
    'signature': signature,
}

response = requests.get('https://wwwapi.kugou.com/play/songinfo', params=params, headers=headers)
print(response.text)