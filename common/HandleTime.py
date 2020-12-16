import datetime

class TimeData:



    def __init__(self):
        now = datetime.datetime.now()
        self._year = now.year
        self._month = now.month
        self._day = now.day
        self._hour = now.hour
        self._minute = now.minute
        self._second = now.second

    """
        获取当前标准日期  年-月-日 时:分:秒
    """
    def get_current_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    """
        修改当前时间
    """
    def update_current_time(self,year=None,month=None,day=None,hour=None,minute=None,second=None):
        if not year and  not month and not day and not hour and not minute and not second:
            return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__init__()
        if year:
            self._year = self._year + year
        if month:
            self._month = self._month + month
        if day:
            self._day = self._day + day
        if hour:
            self._hour = self._hour + hour
        if minute:
            self._minute = self._minute + minute
        if second:
            self._second =  self._second+second
        return "{}-{}-{} {}:{}:{}".format(self._year,self._month,self._day,self._hour,self._minute,self._second)


    """
        指定时间段
    """
    def update_specified_time(self,year=None,month=None,day=None,hour=None,minute=None,second=None):
        self.__init__()
        if not year and  not month and not day and not hour and not minute and not second:
            return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if year:
            self._year = self._year + year
        if month:
            self._month = self._month + month
        if day:
            self._day = self._day + day
        if self._day < 10:
            self._day = "0" + str(self._day)
        if self._month < 10:
            self._month = "0" + str(self._month)
        return "{}-{}-{} {}:{}:{}".format(self._year,self._month,self._day,hour,minute,second)


    """
        指定时间段
    """
    def update_data_time(self,time,day):
        start_time = time.split(":")[0]
        end_time = int(start_time)+day
        if start_time.strip()[0] == "0":
            end_time = "0"+str(end_time)
        return start_time,end_time


handle_time = TimeData()
