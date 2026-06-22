# 获得加密参数params
import hashlib
import time
import urllib.parse


class SignatureGenerator:
    def __init__(self):
        self.base_params = {
            'srcappid': '2919',
            'clientver': '20000',
            'clienttime': '',
            'mid': 'fb92a6fbada0f5060cf0f5058f1d800e',
            'uuid': 'fb92a6fbada0f5060cf0f5058f1d800e',
            'dfid': '1bq5wP3V9dAI106DWJ2Px1xI',
            'appid': '1014',
            'platid': '4',
            'encode_album_audio_id': '',
            'token': 'eea2079550f7563bea339ed7920fedf4eec6f2fdfabfefd3d6dd0db5d23bd377',
            'userid': '698985232',
            'signature': '',
        }

    def generate_param_list(self, encode_album_audio_id, t):
        """生成参数列表用于签名计算"""
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

    def generate_signature(self, encode_album_audio_id, t=None):
        """生成签名"""
        if t is None:
            t = int(time.time() * 1000)

        param_list = self.generate_param_list(encode_album_audio_id, t)
        signature = hashlib.md5(''.join(param_list).encode('utf-8')).hexdigest()
        return signature, t

    def generate_kugou_url(self, encode_album_audio_id, signature, t):
        """生成酷狗API请求URL和参数"""
        params = self.base_params.copy()
        params.update({
            'clienttime': t,
            'encode_album_audio_id': encode_album_audio_id,
            'signature': signature
        })

        # 构建URL参数字符串
        query_string = '&'.join([f"{key}={urllib.parse.quote_plus(str(value))}"
                                 for key, value in params.items()])

        # 生成完整URL
        base_url = "https://wwwapi.kugou.com/play/songinfo"
        full_url = f"{base_url}?{query_string}"

        return full_url, params

if __name__ == '__main__':
    full = SignatureGenerator()
    encode_album_audio_id = "gvq5k33"
    signature, t = full.generate_signature(encode_album_audio_id)
    print(signature)
    print(t)
    # full_url, params = full.generate_kugou_url(encode_album_audio_id, signature, t)
    # print(full_url)
    # print(params)