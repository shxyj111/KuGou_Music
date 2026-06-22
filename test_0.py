# 根据歌单id获取歌单歌曲名称和歌曲链接和歌曲id
import requests
import re
import json

cookies = {
    'kg_mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'kg_dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
    'KuGoo': 'KugooID=698985232&KugooPwd=FE9FA778A25727ECBD370D351AF670A2&NickName=%u56f4%u89c2%u0076%u0069%u0070&Pic=http://imge.kugou.com/kugouicon/165/20210116/20210116021340552482.jpg&RegState=1&RegFrom=&t=eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377&t_ts=1762694984&t_key=&a_id=1014&ct=1762694984&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0036%u0039%u0038%u0039%u0038%u0035%u0032%u0033%u0032',
    'KugooID': '698985232',
    't': 'eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377',
    'a_id': '1014',
    'UserName': '%u006b%u0067%u006f%u0070%u0065%u006e%u0036%u0039%u0038%u0039%u0038%u0035%u0032%u0033%u0032',
    'mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
    'Hm_lvt_aedee6983d4cfc62f509129360d6bb3d': '1762574889,1762581119,1762660201,1762743377',
    'HMACCOUNT': '6526E05123E169EF',
    'ACK_SERVER_10015': '%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D',
    'kg_dfid_collect': 'd41d8cd98f00b204e9800998ecf8427e',
    'kg_mid_temp': 'fb92a6fbada0f5060cf0f5058f1d800e',
    'ACK_SERVER_10016': '%7B%22list%22%3A%5B%5B%22gzreg-user.kugou.com%22%5D%5D%7D',
    'ACK_SERVER_10017': '%7B%22list%22%3A%5B%5B%22gzverifycode.service.kugou.com%22%5D%5D%7D',
    'Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d': '1762748502',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.kugou.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    # 'cookie': 'kg_mid=fb92a6fbada0f5060cf0f5058f1d800e; kg_dfid=1bq5wP3V9dAI106DWJ2Px1xI; KuGoo=KugooID=698985232&KugooPwd=FE9FA778A25727ECBD370D351AF670A2&NickName=%u56f4%u89c2%u0076%u0069%u0070&Pic=http://imge.kugou.com/kugouicon/165/20210116/20210116021340552482.jpg&RegState=1&RegFrom=&t=eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377&t_ts=1762694984&t_key=&a_id=1014&ct=1762694984&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0036%u0039%u0038%u0039%u0038%u0035%u0032%u0033%u0032; KugooID=698985232; t=eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377; a_id=1014; UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0036%u0039%u0038%u0039%u0038%u0035%u0032%u0033%u0032; mid=fb92a6fbada0f5060cf0f5058f1d800e; dfid=1bq5wP3V9dAI106DWJ2Px1xI; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1762574889,1762581119,1762660201,1762743377; HMACCOUNT=6526E05123E169EF; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=fb92a6fbada0f5060cf0f5058f1d800e; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22gzreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22gzverifycode.service.kugou.com%22%5D%5D%7D; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1762748502',
}

response = requests.get('https://www.kugou.com/songlist/gcid_3zk1rd2mzmcz0e1/', cookies=cookies, headers=headers)


def extract_song_info(html_content):
    """
    从HTML内容中提取歌曲名称、歌曲链接和歌曲ID
    """
    # 方法1：从JavaScript变量中提取（更可靠）
    songs_data = []

    # 提取JavaScript中的歌曲数据
    js_data_pattern = r'var nData\s*=\s*({.*?});'
    js_match = re.search(js_data_pattern, html_content, re.DOTALL)

    if js_match:
        try:
            js_data = js_match.group(1)
            data = json.loads(js_data)
            songs = data.get('songs', [])

            for song in songs:
                song_name = song.get('name', '')
                song_url = song.get('song_url', '')
                # 从encode_album_audio_id获取歌曲ID
                song_id = song.get('encode_album_audio_id', '')

                songs_data.append({
                    'name': song_name,
                    'url': song_url,
                    'id': song_id
                })

            return songs_data
        except json.JSONDecodeError:
            print("JSON解析失败，使用正则表达式方法")

    # 方法2：使用正则表达式从HTML链接中提取（备用方法）
    songs_data = []

    # 匹配歌曲链接的模式
    pattern = r'<a title="([^"]*)"[^>]*href="(https://www\.kugou\.com/mixsong/([^"]+)\.html)"'

    matches = re.findall(pattern, html_content)

    for match in matches:
        song_name = match[0]
        song_url = match[1]
        song_id = match[2]

        songs_data.append({
            'name': song_name,
            'url': song_url,
            'id': song_id
        })

    return songs_data


def main():
    # 这里应该是您从文件或网络获取的HTML内容
    # 为了演示，我将使用您提供的数据中的一部分
    html_content = response.text

    # 在实际使用中，您应该读取整个HTML文件
    # 这里为了演示，我使用完整的HTML内容
    # 在实际代码中，您需要将完整的HTML内容传递给extract_song_info函数

    # 假设html_content包含完整的HTML
    songs = extract_song_info(html_content)

    print("提取到的歌曲信息：")
    print("=" * 80)

    for i, song in enumerate(songs, 1):
        print(f"歌曲 {i}:")
        print(f"  名称: {song['name']}")
        print(f"  链接: {song['url']}")
        print(f"  ID: {song['id']}")
        print("-" * 50)


if __name__ == "__main__":
    main()