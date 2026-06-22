# 通过反爬获取加密参数r和params列表以及获取音乐本体链接的接口网址
import hashlib
import time
import urllib.parse

def generate_kugou_url(encode_album_audio_id, signature, t,params_dict=None):

    # 默认参数模板
    default_params = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': t,
        'mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
        'uuid': 'fb92a6fbada0f5060cf0f5058f1d800e',
        'dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
        'appid': '1014',
        'platid': '4',
        'encode_album_audio_id': encode_album_audio_id,  # 动态传入
        'token': 'eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377',
        'userid': '698985232',
        'signature': signature  # 动态传入
    }

    # 如果提供了自定义参数，则更新默认参数
    if params_dict:
        default_params.update(params_dict)

    # 确保必要的参数存在
    default_params['encode_album_audio_id'] = encode_album_audio_id
    default_params['signature'] = signature

    # 按照指定顺序排列参数
    ordered_params = {
        'srcappid': default_params['srcappid'],
        'clientver': default_params['clientver'],
        'clienttime': default_params['clienttime'],
        'mid': default_params['mid'],
        'uuid': default_params['uuid'],
        'dfid': default_params['dfid'],
        'appid': default_params['appid'],
        'platid': default_params['platid'],
        'encode_album_audio_id': default_params['encode_album_audio_id'],
        'token': default_params['token'],
        'userid': default_params['userid'],
        'signature': default_params['signature']
    }
    # 将字典格式化为每行一个键值对的字符串
    formatted_output = "{\n"
    for key, value in ordered_params.items():
        formatted_output += f"    '{key}': '{value}',\n"
    formatted_output = formatted_output.rstrip(',\n') + "\n}"

    # 构建URL参数字符串
    query_string = '&'.join([f"{key}={urllib.parse.quote_plus(str(value))}"
                             for key, value in ordered_params.items()])

    # 生成完整URL
    base_url = "https://wwwapi.kugou.com/play/songinfo"
    full_url = f"{base_url}?{query_string}"

    return full_url, formatted_output

def generate_param_list(encode_album_audio_id,t):

    param_list = [
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
        "appid=1014",
        f"clienttime={t}",
        "clientver=20000",
        "dfid=1bq5wP3V9dAI106DWJ2Px1xI",
        f"encode_album_audio_id={encode_album_audio_id}",
        "mid=fb92a6fbada0f5060cf0f5058f1d800e",
        "platid=4",
        "srcappid=2919",
        "token=eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377",
        "userid=698985232",
        "uuid=fb92a6fbada0f5060cf0f5058f1d800e",
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    ]

    return param_list

# 使用示例
if __name__ == "__main__":
    # 动态传入歌曲ID和签名
    song_id = "1plx3hfe"
    t = int(time.time() * 1000)
    signature = hashlib.md5(''.join(generate_param_list(song_id,t)).encode('utf-8')).hexdigest()
    print(signature)

    full_url,params = generate_kugou_url(song_id, signature,t)
    print(full_url)
    print(params)
