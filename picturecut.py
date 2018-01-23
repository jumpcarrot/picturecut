import requests
import re,os
import urllib.request
import time

def getHtml(url):
    Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36',
               "Connection":"keep-alive",
               "Referer":""}
    page = requests.get(url,headers=Headers, timeout=10)
    return page.content

def download(name,src):
    try:
    #    urllib.request.urlretrieve(src,'./img/%s.jpg' % name)
        with open(name,'wb') as f:
            f.write(getHtml(src))
            print(src,'ok！')
    except:
        print(src,'下载失败')

def getImg(html):
    try:
        imgre = re.compile(r'http://[\S]*\.jpg')
        imglist = re.findall(imgre,repr(html))
        print('图片网址解析ok')
    except:
        print('图片网址解析失败')
    path= './img'
    num = 1
    while (os.path.exists(path)):
        path = './img%s' %num
        num=num+1
    os.mkdir(path)
    print("新建img文件夹，开始缓存")  
    x = 0
    for imgurl in imglist:
        download(path+'/%s'%x+'.jpg',imgurl)
        x=x+1
     #   time.sleep(1)

url='http://www.suibianlu.com/meitu/'
html = getHtml(url)
getImg(html)
