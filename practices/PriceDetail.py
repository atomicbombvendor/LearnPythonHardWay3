# coding=utf-8
# 一个类,用来存储数据

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

    def __str__(self) -> str:
       return "%s, %s, %s, %s, %s, %s, %s\n" % (self._shareClassId, self._endDate, self._closePrice, self._openPrice, self._highPrice, self._lowPrice, self._volume)