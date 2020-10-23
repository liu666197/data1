import requests
from base import download
# rn: 每页的数据条数
# pn: rn * page
userInput = input('请输入想下载的图片名称: ')
# 所有的图片数据
count = 0
for page in range(1,5):
    print('第{}页开始'.format(page))
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=55&gsm=1e&1597988871073='
    # 关键的参数
    dic = {
        'pn': 30 * page,
        'rn': 30,
        'queryWord': userInput,
        'word': userInput
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # params: get请求的字典参数
    response = requests.get(url, headers=headers,params=dic)
    # 服务器返回的如果是json数据,使用json()
    content = response.json()

    # 所有的数据(最后一项没有)
    allData = content['data'][:len(content['data']) - 1]
    for img in allData:
        count += 1
        imgUrl = img['hoverURL'] or img['middleURL']
        print(count, '++++',imgUrl)
        # 所有图片的url地址
        # print(img['hoverURL'])
        download(imgUrl)
    print('第{}页开始'.format(page))