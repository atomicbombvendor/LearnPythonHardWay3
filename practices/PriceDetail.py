# coding=utf-8
# 一个类,用来存储数据

class PriceDetail(object):

    __slots__ = ('_endDate', '_closePrice', '_openPrice', '_highPrice', '_lowPrice', '_volume')

    def __init__(self, endDate, closePrice, openPrice, highPrice, lowPrice, volume):
        self._endDate = endDate
        self._closePrice = closePrice
        self._openPrice = openPrice
        self._highPrice = highPrice
        self._lowPrice = lowPrice
        self._volume = volume

    @property
    def EndDate(self):
        return self._endDate

    @EndDate.setter
    def EndDate(self, endDate):
        self._endDate = endDate

    @property
    def ClosePrice(self):
        return self._closePrice

    @ClosePrice.setter
    def ClosePrice(self, closePrice):
        self._closePrice = closePrice

    @property
    def HighPrice(self):
        return self._highPrice

    @HighPrice.setter
    def HighPrice(self, highPrice):
        self._openPrice = highPrice

    @property
    def LowPrice(self):
        return self._lowPrice

    @LowPrice.setter
    def LowPrice(self, lowPrice):
        self._endDate = lowPrice

    @property
    def Volume(self):
        return self._volume

    @Volume.setter
    def Volume(self, volume):
        self._volume = volume

    @property
    def OpenPrice(self):
        return self._openPrice

    @OpenPrice.setter
    def OpenPrice(self, openPrice):
        self._openPrice = openPrice