# 登陆PriceXOI并获取一条信息
import gzip
import urllib
from http import cookiejar
from io import BytesIO

from urllib import request


cooke_file = "resource/pricexoicookie.dat"

headers = {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'identity;q=1.0,compress;q=0.8,gzip;q=0.5, deflate;q=0.3,*;q=0',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'price.xoi.morningstar.com',
            'Pragma': 'no - cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/58.0'
        }

def login():

    login_url = "http://price.xoi.morningstar.com/DataPlatform/Login.aspx"
    login_userName = "GlobalEquityData@morningstar.com"
    login_password ="GXy1q88E"

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, login_url, login_userName, login_password)
    http_handler = urllib.request.HTTPBasicAuthHandler(password_mgr=password_mgr)
    cookie = cookiejar.MozillaCookieJar()
    cookie_handler = request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(http_handler, cookie_handler)
    response = opener.open(login_url)
    status = response.getcode()
    if 200 == status:
        print("Login Successful")
        cookie.save(cooke_file, ignore_expires=True, ignore_discard=True)


def process_content():
    result = ""
    try:
        url = "http://price.xoi.morningstar.com/DataPlatform/DataOutput.aspx?Package=HistoricalData&ContentType=MarketPrice&IdType=PerformanceId&Id=0P00000003&Dates=2018&SplitAdjusted=1"
        cookie = cookiejar.MozillaCookieJar()
        cookie.load(cooke_file, ignore_discard=True, ignore_expires=True)
        request = urllib.request.Request(url)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        response = opener.open(request, None, headers)
        content = response.read()
        try:
            buff = BytesIO(content)  # 把content转为文件对象, Gzip解压
            f = gzip.GzipFile(fileobj=buff)
            resource = f.read().decode('utf-8')

            # resource = content.decode('GBK')  # 不是gzip的压缩方式

            status = response.getcode()
            if status == 200:
                print(u"获取页面请求成功, url->\n%s" % url)
            else:
                print(u"获取页面请求失败, url->\n%s" % url)
            result = resource
        except IOError as e:
            if e.strerror.find('gzipped') > 0:
                resource = content.decode('utf-8')  # 不是gzip的压缩方式
                status = response.getcode()
                if status == 200:
                    print(u"获取页面请求成功, url->\n%s" % url)
                else:
                    print(u"获取页面请求失败, url->\n%s" % url)
                result = resource
        finally:
            return result
    except urllib.request.HTTPError as e:
        print(u'The server couldn\'t fulfill the request')
        print(u'Error code: ', e.reason)
    except urllib.request.URLError as e:
        print(u'We failed to reach a server.')
        print(u'Reason: ', e.reason)


login()
print(process_content())


