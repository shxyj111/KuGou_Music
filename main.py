# main.py
import time
from song_list_fetcher import SongListFetcher
from signature_generator import SignatureGenerator
from song_downloader import SongDownloader


def main():
    # 初始化各个组件
    song_list_fetcher = SongListFetcher()
    signature_generator = SignatureGenerator()
    song_downloader = SongDownloader()

    # 歌单URL
    playlist_url = "https://www.kugou.com/songlist/gcid_3zrptyuoz45z065/"

    print("开始获取歌单信息...")

    # 获取歌单中的歌曲列表
    songs = song_list_fetcher.get_song_list(playlist_url)

    if not songs:
        print("未找到歌曲信息，请检查歌单URL或网络连接")
        return

    print(f"共找到 {len(songs)} 首歌曲")
    print("=" * 60)

    # 批量处理每首歌曲
    for i, song in enumerate(songs, 1):
        print(f"\n正在处理第 {i}/{len(songs)} 首歌曲: {song['name']}")

        try:
            # 生成签名和时间戳
            signature, t = signature_generator.generate_signature(song['id'])

            # 生成API请求参数
            api_url, params = signature_generator.generate_kugou_url(song['id'], signature, t)

            # 获取下载链接
            download_url = song_downloader.get_download_url(params)

            if download_url:
                print(f"获取到下载链接，开始下载...")

                # 下载歌曲
                file_path = song_downloader.download_song(download_url, song['name'])

                if file_path:
                    print(f"✓ 下载完成: {file_path}")
                else:
                    print(f"✗ 下载失败: {song['name']}")
            else:
                print(f"✗ 无法获取下载链接: {song['name']}")

        except Exception as e:
            print(f"✗ 处理歌曲时出错: {song['name']}, 错误: {e}")

        # 添加延迟，避免请求过于频繁
        time.sleep(1)

    print("\n" + "=" * 60)
    print("批量下载任务完成！")


if __name__ == "__main__":
    main()