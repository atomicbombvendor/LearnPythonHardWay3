# 登陆PriceXOI并获取一条信息
import gzip
import urllib
from http import cookiejar
from io import BytesIO

from urllib import request
from lxml import etree

from PriceDetail import PriceDetail

cooke_file = "resource/pricexoicookie.dat"
shareClassId = "0P00000003"
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'price.xoi.morningstar.com',
            'Pragma': 'no - cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
result_file ="resource/price_details.dat"
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

def get_content():
    result = ""
    try:
        url = "http://price.xoi.morningstar.com/DataPlatform/DataOutput.aspx?" \
              "Package=HistoricalData" \
              "&ContentType=MarketPrice&IdType=PerformanceId&Id=" \
              + shareClassId +"&Dates=2018&SplitAdjusted=1"
        cookie = cookiejar.MozillaCookieJar()
        cookie.load(cooke_file, ignore_discard=True, ignore_expires=True)
        request = urllib.request.Request(url, None, headers)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        response = opener.open(request)
        content = response.read()
        try:
            buff = BytesIO(content)  # 把content转为文件对象, Gzip解压
            f = gzip.GzipFile(fileobj=buff)
            resource = f.read().decode('utf-8')
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

def parse_content(content):
    tree = etree.XML(content.encode('utf-8'))
    result = ""
    path = "/Performance/PriceHistory/PriceDetail"
    target_node = tree.xpath(path)
    for node in target_node[0:30]:
        detail = PriceDetail()
        detail._shareClassId = shareClassId
        childrens = node.getchildren()
        for children in childrens:
            if "EndDate" in children.tag:
                detail._endDate = children.text
            if "ClosePrice" in children.tag:
                detail._closePrice = children.text
            if "OpenPrice" in children.tag:
                detail._openPrice = children.text
            if "HighPrice" in children.tag:
                detail._highPrice = children.text
            if "LowPrice" in children.tag:
                detail._lowPrice = children.text
            if "Volume" in children.tag:
                detail._volume = children.text
        result += detail.__str__()
    write_content(result_file, result)

def write_content(file, content):
    with open(file, "w+") as f:
        f.write(content)
    print("Write content Done")

login()
parse_content(get_content())
# 如何用脚本的参数形式把ShareClassId传入


