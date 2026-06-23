# KuGou Music - 酷狗音乐歌单批量下载工具

基于 Python 的酷狗音乐歌单批量下载工具，支持根据歌单链接自动获取歌曲列表并批量下载。

## 功能特性

- **歌单解析**：通过歌单 URL 自动提取歌单内所有歌曲信息（名称、ID）
- **签名生成**：自动生成酷狗 API 请求所需的签名参数
- **批量下载**：支持歌单内所有歌曲的一键批量下载
- **自动命名**：下载文件自动以歌曲名命名，并过滤非法字符

## 项目结构

```
KuGou_Music/
├── main.py                # 主入口，整合批量下载流程
├── song_list_fetcher.py   # 歌单获取模块，解析歌单页面提取歌曲信息
├── signature_generator.py # 签名生成模块，生成 API 请求签名
├── song_downloader.py     # 歌曲下载模块，处理下载请求
├── test_0.py ~ test_4.py  # 各模块的测试/调试脚本
├── test_0.js ~ test_4.js  # JavaScript 版辅助脚本
├── package.json           # Node.js 依赖配置
├── 加密参数.txt            # 加密参数说明
└── downloads/             # 下载文件存放目录（自动创建）
```

## 环境依赖

### Python 依赖
- Python 3.6+
- `requests` — HTTP 请求库

### Node.js 依赖（可选，仅部分测试脚本使用）
- `jsdom`
- `jquery`

## 安装

1. 克隆项目：
```bash
git clone <repository-url>
cd KuGou_Music
```

2. 安装 Python 依赖：
```bash
pip install requests
```

3. （可选）安装 Node.js 依赖：
```bash
npm install
```

## 使用方法

### 基本使用

```bash
python main.py
```

默认会下载歌单 `gcid_3zrptyuoz45z065` 中的所有歌曲到 `downloads/` 目录。

### 自定义歌单

修改 `main.py` 中的 `playlist_url` 变量为你想要的歌单链接：

```python
playlist_url = "https://www.kugou.com/songlist/gcid_xxxxx/"
```

### 单独使用各模块

**获取歌单歌曲列表：**
```python
from song_list_fetcher import SongListFetcher

fetcher = SongListFetcher()
songs = fetcher.get_song_list("gcid_3zrptyuoz45z065")
print(songs)  # 返回包含 name, url, id 的歌曲信息列表
```

**生成签名：**
```python
from signature_generator import SignatureGenerator

generator = SignatureGenerator()
signature, timestamp = generator.generate_signature("gvq5k33")
```

## 工作原理

1. **歌单解析** — 从酷狗歌单页面 HTML 中提取 `nData` JavaScript 变量，解析出歌曲列表
2. **签名生成** — 按特定参数顺序拼接后计算 MD5，生成 API 请求所需的 `signature`
3. **获取下载链接** — 调用酷狗 API (`/play/songinfo`) 获取歌曲播放/下载地址
4. **文件下载** — 流式下载 MP3 文件到本地 `downloads/` 目录

## 注意事项

- 请合理使用，避免请求频率过高导致 IP 被限制（代码已内置 1 秒延迟）
- 下载的歌曲仅供个人学习研究使用，请遵守相关版权法规
- Cookie 信息已脱敏处理，如需使用请替换为自己的酷狗账号 Cookie

## License

ISC
