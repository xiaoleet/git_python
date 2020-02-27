# 从12306爬取全部火车站信息，能按照汉字、全拼或简拼查询
#来源：https://blog.csdn.net/weixin_43625577/article/details/86185026
import datetime
import requests
import json
from prettytable import PrettyTable
from colorama import init, Fore
init(autoreset=False)
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9077'
r = requests.get(url)
print("欢迎进入火车票查询系统！".center(60, "*"))
# 将文本信息以@进行切片
tlist = r.text.split('@')[1:]  # 切完片后是list，删除tlist[0]
tlist[-1] = tlist[-1][:-2]  # 去除多余的元素
station_all = []
for i in tlist:
    i = i.split('|')
    station_all += [i]  # 将以'|'分隔开的信息以列表的形式添加到station_all里面
while 1:
    from_info = input("请输入出发地（汉字/全拼）:")
    for j in station_all:
        if from_info in j:
            from_sta = j[2]
    to_info = input("请输入目的地（汉字/全拼）:")
    for j in station_all:
        if to_info in j:
            to_sta = j[2]
    cf_date = input("请输入出发日期(输入格式2019-01-01):")
    tianshu = input("请输入要查询的天数(15天内):")
    now = datetime.date.today()  # 获取当天时间
    last = now + datetime.timedelta(days=14)  # 15天后的日期
    tra_date = datetime.date(int(cf_date[:4]), int(cf_date[5:7]), int(cf_date[8:]))  # 将输入的出发日期转换成datetime类型
    if tra_date >= now and tra_date <= last:  # 判断输入的时间是否在正确范围内
        for i in range(int(tianshu)):
            train_date = tra_date + datetime.timedelta(days=i)
            # 格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}、{2}、...，
            url1 = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
                train_date, from_sta, to_sta)
            r1 = requests.get(url1)
            print(r1.text)
            json_data = r1.json()['data']
            json_result = json_data['result']
            result = []
            for i in json_result:
                i = i.split('|')
                result += [i]
            table = PrettyTable(
                ['车次', '出发站/到达站', '出发时间/到达时间', '历时', '商务座', '一等座', '二等座', '高级软座', '软卧一等座', '动卧', '硬卧二等座', '硬座', '无座'])
            # 将 "  " 替换成 "--"
            for checi_info in result:
                for i in range(34):
                    if checi_info[i] == '':
                        checi_info[i] = "--"
                checi = checi_info[3]
                chufa_sta = checi_info[6]
                daoda_sta = checi_info[7]
                chufa_time = checi_info[8]
                daoda_time = checi_info[9]
                times = checi_info[10]
                shw_seat = checi_info[32]
                yd_seat = checi_info[31]
                ed_seat = checi_info[30]
                gjrw = checi_info[21]
                rw_yd = checi_info[23]
                dw = checi_info[33]
                yw_ed = checi_info[28]
                yz = checi_info[29]
                wz = checi_info[26]
                # 将读取下来的车站代码 改成 汉字 形式
                for i in station_all:
                    if chufa_sta in i:
                        CHUFA_sta = j[1]
                for j in station_all:
                    if daoda_sta in j:
                        DAODA_sta = j[1]
                list = [Fore.LIGHTBLUE_EX + checi + Fore.RESET,
                        Fore.LIGHTRED_EX + CHUFA_sta + Fore.RESET + '\n' + Fore.LIGHTGREEN_EX + DAODA_sta + Fore.RESET + '\n',
                        Fore.LIGHTRED_EX + chufa_time + Fore.RESET + '\n' + Fore.LIGHTGREEN_EX + daoda_time + Fore.RESET,
                        times, shw_seat, yd_seat, ed_seat, gjrw, rw_yd, dw, yw_ed, yz, wz]
                table.add_row(list)
            print(table)
        break
    else:
        print("输入时间有误，请输入未来15天内的日期进行查询！")