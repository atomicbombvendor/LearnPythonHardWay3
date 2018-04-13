import gzip
import os
import urllib
from http import cookiejar
from io import BytesIO
from urllib import request

import sys
from lxml import etree

cooke_file = "data/test/pricexoicookie.dat"
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
shareClassId = None
result_file = "data/test/@ShareId_XOI.dat"


def login():
    login_url = "http://price.xoi.morningstar.com/DataPlatform/Login.aspx"
    login_userName = "GlobalEquityData@morningstar.com"
    login_password = "GXy1q88E"

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
        cookie.save(cooke_file, ignore_expires=False, ignore_discard=False)


def get_content(sid):
    result = ""
    global shareClassId
    shareClassId = sid
    try:
        url = "http://price.xoi.morningstar.com/DataPlatform/DataOutput.aspx?" \
              "Package=HistoricalData" \
              "&ContentType=MarketPrice&IdType=PerformanceId&Id=" \
              + shareClassId + "&Dates=2018&SplitAdjusted=1"
        cookie = genereate_cookie()
        print("start request URL>>>%s\r\n" % (url))
        request = urllib.request.Request(url, None, headers)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        response = opener.open(request)
        content = response.read()
        try:
            buff = BytesIO(content)
            f = gzip.GzipFile(fileobj=buff)
            resource = f.read().decode('utf-8')
            status = response.getcode()
            if status == 200:
                print(u"Request page successful")
            else:
                print(u"Request failed")
            result = resource
        except IOError as e:
            if e.strerror.find('gzipped') > 0:
                resource = content.decode('utf-8')
                status = response.getcode()
                if status == 200:
                    print(u"Get page successful")
                else:
                    print(u"Get page failed")
                result = resource
        finally:
            return result
    except urllib.request.HTTPError as e:
        print(u'Cant find Page, Error: ', e.reason)
    except urllib.request.URLError as e:
        print(u'We failed to reach a server.')
        print(u'Reason: ', e.reason)


def genereate_cookie():
    create_folder(cooke_file)
    cookie = cookiejar.MozillaCookieJar()
    if (not os.path.exists(cooke_file)) or (not cookie.load(cooke_file, ignore_discard=False, ignore_expires=False)):
            login()
            cookie.load(cooke_file, ignore_discard=False, ignore_expires=False)
    else:
        cookie.load(cooke_file, ignore_discard=False, ignore_expires=False)
    return cookie


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
    write_content(result_file.replace("@ShareId", shareClassId), result)


def write_content(file, content):
    create_folder(file)
    with open(file, "w+") as f:
        f.write(content)
    print("Write content Done. path: " + file)


def create_folder(path):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

class PriceDetail(object):

    __slots__ = ('_shareClassId', '_endDate', '_closePrice', '_openPrice', '_highPrice', '_lowPrice', '_volume')

    def __init__(self, shareClassId = None, endDate = None, closePrice = None, openPrice = None, highPrice = None, lowPrice = None, volume = None):
        self._shareClassId = shareClassId
        self._endDate = endDate
        self._closePrice = closePrice
        self._openPrice = openPrice
        self._highPrice = highPrice
        self._lowPrice = lowPrice
        self._volume = volume

    @property
    def ShareClassId(self):
        return str(self._endDate)

    @ShareClassId.setter
    def ShareClassId(self, shareClassId):
        self._shareClassId = shareClassId

    @property
    def EndDate(self):
        return str(self._endDate)

    @EndDate.setter
    def EndDate(self, endDate):
        self._endDate = endDate

    @property
    def ClosePrice(self):
        return str(self._closePrice)

    @ClosePrice.setter
    def ClosePrice(self, closePrice):
        self._closePrice = closePrice

    @property
    def HighPrice(self):
        return str(self._highPrice)

    @HighPrice.setter
    def HighPrice(self, highPrice):
        self._openPrice = highPrice

    @property
    def LowPrice(self):
        return str(self._lowPrice)

    @LowPrice.setter
    def LowPrice(self, lowPrice):
        self._endDate = lowPrice

    @property
    def Volume(self):
        return str(self._volume)

    @Volume.setter
    def Volume(self, volume):
        self._volume = volume

    @property
    def OpenPrice(self):
        return str(self._openPrice)

    @OpenPrice.setter
    def OpenPrice(self, openPrice):
        self._openPrice = openPrice

    def __str__(self):
       return "%s, %s, %s, %s, %s, %s, %s\n" % (self._shareClassId, self._endDate, self._closePrice, self._openPrice, self._highPrice, self._lowPrice, self._volume)

# sids = sys.argv[1:]
# print(sids)
# for sid in sids:
#     print("ShareClassId= " + sid)
#     parse_content(get_content(sid))

sid = '0P00000003'

parse_content(get_content(sid))



