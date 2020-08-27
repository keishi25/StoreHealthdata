import requests
import json

#URL = "http://10.23.137.229:8000/store/"
URL = "http://10.23.137.152:8000/store/recode_person"


sess = requests.session()

# csrf認証
sess.get(URL)

csrftoken = sess.cookies['csrftoken']

# ヘッダ
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}
# 送信データ
payload = {"param1": "aaaa", "param2": "bbbbb"}
# JSON変換
json_payload = json.dumps(payload)

# POST送信
res = sess.post(URL, data=json_payload, headers=headers)
print(res.text)  # textメソッドでレスポンスの値を取得する
