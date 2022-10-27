import hashlib
import urllib.parse


class Sing(object):
    @staticmethod
    def sort_data(data, app_secret):
        res = ''
        str_data = sorted(data.items(), key=lambda x: x[0])
        for i in str_data:
            res = res + i[0] + '=' + i[1] + ','
        res = res + 'secret=' + app_secret
        print(res)
        url_encoded = urllib.parse.quote_plus(res)
        sign = hashlib.md5(url_encoded.encode())
        res_sign = sign.hexdigest()
        return res_sign
