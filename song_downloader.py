# song_downloader.py
import requests
import re
import os


class SongDownloader:
    def __init__(self):
        self.headers = {
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

    def get_download_url(self, full_url, params):
        """获取歌曲下载链接"""
        response = requests.get(full_url, params=params, headers=self.headers)

        # pattern = r'"play_url":"([^"]+)"'
        # match = re.search(pattern, response.text)
        #
        # if match:
        #     play_url = match.group(1).replace('\\/', '/')
        #     return play_url
        # return None
        return response.text

    def download_song(self, download_url, song_name, download_folder="downloads"):
        """下载歌曲文件"""
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # 清理文件名中的非法字符
        safe_name = re.sub(r'[<>:"/\\|?*]', '', song_name)
        file_path = os.path.join(download_folder, f"{safe_name}.mp3")

        try:
            response = requests.get(download_url, headers=self.headers, stream=True)
            response.raise_for_status()

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return file_path
        except Exception as e:
            print(f"下载失败: {e}")
            return None

if __name__ == '__main__':
    song_downloader = SongDownloader()
    full_url = 'https://wwwapi.kugou.com/play/songinfo'
    params = {
        "srcappid": "2919",
        "clientver": "20000",
        "clienttime": '1763911014830',
        "mid": "fb92a6fbada0f5060cf0f5058f1d800e",
        "uuid": "fb92a6fbada0f5060cf0f5058f1d800e",
        "dfid": "1bq5wP3V9dAI106DWJ2Px1xI",
        "appid": "1014",
        "platid": "4",
        "encode_album_audio_id": "gvq5k33",
        "token": "eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377",
        "userid": "698985232",
        "signature": "41a2af10c39304f3787191b73e6dba70"
    }
    url = song_downloader.get_download_url(full_url, params)
    print(url)