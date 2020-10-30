import requests
import json
import uuid
from time import sleep
from random import randint

s = requests.Session()

cookie = ""
if (cookie == ""):
  cookie = input().strip()

def main():
  url1 = f'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
  url2 = f'https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign'
  device_id = str(uuid.uuid3(uuid.NAMESPACE_URL,cookie)).replace('-','').upper()
  headers1 = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.1.0',
    'Referer': 'https://webstatic.mihoyo.com/bbs/event/signin-ys/index.html?bbs_auth_required=true&act_id=e202009291139501&utm_source=bbs&utm_medium=mys&utm_campaign=icon',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': cookie
}
  headers2 = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.1.0',
    'Referer': 'https://webstatic.mihoyo.com/bbs/event/signin-ys/index.html?bbs_auth_required=true&act_id=e202009291139501&utm_source=bbs&utm_medium=mys&utm_campaign=icon',
    'Accept-Encoding': 'gzip, deflate, br',
    'cookie': cookie,
    'x-rpc-device_id': device_id
}
  r1 = s.get(url1, headers = headers1)
  d1 = json.loads(r1.text)
  uid = d1['data']['list'][0]['game_uid']
  data = {
    'act_id': 'e202009291139501',
    'region': 'cn_gf01',
    'uid': uid
}
  r2 = s.post(url2, headers = headers2, data = json.dumps(data))
  d2 = json.loads(r2.text)
  if d2['retcode'] == 0:
    print("======\n签到成功!\n======")
  else :
    if d2['retcode'] == -5003:
      print("======\n" + d2['message'] + "\n======")
    else :
      print("======\n签到失败!\n详细信息:" + d2['message'] + "\n======")
      exit(100)


if __name__ == "__main__":
  sleep(randint(10,300))
  main()
