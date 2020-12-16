from common.HandleTime import  handle_time

class MockData():

    def __init__(self):
        self.data =[]
    """
        
        生成24小时数据  参数为1 即从1点开始
        
        ['2020-12-15 01:00:00', '2020-12-15 02:00:00', '2020-12-15 03:00:00', '2020-12-15 04:00:00', '2020-12-15 05:00:00', '2020-12-15 06:00:00', '2020-12-15 07:00:00', '2020-12-15 08:00:00', '2020-12-15 09:00:00', '2020-12-15 10:00:00', '2020-12-15 11:00:00', '2020-12-15 12:00:00', '2020-12-15 13:00:00', '2020-12-15 14:00:00', '2020-12-15 15:00:00', '2020-12-15 16:00:00', '2020-12-15 17:00:00', '2020-12-15 18:00:00', '2020-12-15 19:00:00', '2020-12-15 20:00:00', '2020-12-15 21:00:00', '2020-12-15 22:00:00', '2020-12-15 23:00:00', '2020-12-16 00:00:00', '2020-12-16 01:00:00']
        
    """
    def mock_history_time(self,start_time):
        self.generate_current_day(start_time)
        self.generate_after_day(start_time)
        return self.data

    def generate_current_day(self,start_time):
        for item in range(start_time, 24):
            if item < 10:
                item = "0" + str(item)
            self.data.append(handle_time.update_specified_time(day=-1, hour=item, minute="00", second="00"))

    def generate_after_day(self,start_time):
        for i in range(0, start_time + 1):
            if i < 10:
                i = "0" + str(i)
            self.data.append(handle_time.update_specified_time(hour=i, minute="00", second="00"))



mock_data =MockData()
