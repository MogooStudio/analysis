import baostock as bs
import akshare as ak
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
import base64
import time

from common import *

# 查询结果保存文件
_log_name = "stock_data.txt"

# 是否发送邮件
is_send_email = True

# 查询日期校验
_date_time_a = datetime.date(2022, 6, 3)
_date_time_b = datetime.date(2022, 6, 6)

today = datetime.date.today()  # 今天日期
if _date_time_b >= today >= _date_time_a:  # 指定日期区间内用左值
    today = _date_time_a

delta = -1
if today.weekday() == 6:  # 如果今天是星期日
    delta = -2
elif today.weekday() == 0:  # 如果今天是星期一
    delta = -3

day = today + datetime.timedelta(days=delta)
STR_DAY = day.strftime('%Y-%m-%d')
print("delta=", delta)
print("今天日期：{0}|{1}，查询日期：{2}|{3}".format(today, today.weekday(), STR_DAY, day.weekday()))


class Test:

    def __init__(self, _data):
        self.start_date = _data
        self.end_date = _data
        self.data_list = []

    # 获取股票市值
    def get_market(self, code):
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=code)
        value = stock_individual_info_em_df.at[4, "value"]
        return round(value)

    # 获取股票指标
    def get_ttm(self, god):
        # peTTM    滚动市盈率
        # psTTM    滚动市销率
        rs = bs.query_history_k_data_plus(god,
                                          "date,code,close,peTTM,pbMRQ",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        if rs.error_code != "0":
            print('query_history_k_data_plus respond error_code:' + rs.error_code)
            print('query_history_k_data_plus respond error_msg:' + rs.error_msg)
        while (rs.error_code == '0') & rs.next():
            self.data_list.append(rs.get_row_data())

    def get_code(self, code):
        god = "sh" if code and code[0] == "6" else "sz"
        return god + "." + code

    def test(self, code):
        god = self.get_code(code)
        rs = bs.query_history_k_data_plus(god,
                                          "date,code,close,peTTM,psTTM",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        print(result)

    def test1(self, code):
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=code)
        print(stock_individual_info_em_df)
        value = stock_individual_info_em_df.at[4, "value"]
        print(value)
        print(round(value))

    def run(self):
        for code, _ in stock_all.items():
            god = self.get_code(code)
            print("获取股票代码数据:{0}".format(god))
            self.get_ttm(god)

        low_code, high_code, mid_code = [], [], []
        for stock_data in self.data_list:
            stock_code = str(stock_data[e_code])
            real_code = stock_code.split('.')[1]
            code_data = stock_all.get(real_code)
            code_name = code_data["name"]
            low_ttm = code_data["low"]
            high_ttm = code_data["high"]
            type_ttm = code_data["type"]
            real_ttm = 0.0
            type_value = ""
            if type_ttm == e_pe:
                real_ttm = stock_data[e_ttm_pe]
                type_value = "PE"
            elif type_ttm == e_pb:
                real_ttm = stock_data[e_ttm_pb]
                type_value = "PB"
            elif type_ttm == e_value:
                real_ttm = self.get_market(real_code)
                type_value = "市值"
            elif type_ttm == e_price:
                real_ttm = stock_data[e_close]
                type_value = "股价"
            real_ttm = float(real_ttm)
            low_ttm = float(low_ttm)
            high_ttm = float(high_ttm)
            diff_low = real_ttm - low_ttm
            diff_high = real_ttm - high_ttm
            if real_ttm <= low_ttm:
                low_code.append({
                    "name": code_name,
                    "code": stock_code,
                    "ttm_current": round(float(real_ttm), 2),
                    "ttm_low": low_ttm,
                    "ttm_diff": round(diff_low, 2),
                    "ttm_type": type_value,
                })
            elif real_ttm >= high_ttm:
                high_code.append({
                    "name": code_name,
                    "code": stock_code,
                    "ttm_current": round(float(real_ttm), 2),
                    "ttm_high": high_ttm,
                    "ttm_diff": round(diff_high, 2),
                    "ttm_type": type_value,
                })
            else:
                mid_code.append({
                    "name": code_name,
                    "code": stock_code,
                    "ttm_current": round(float(real_ttm), 2),
                    "ttm_low": low_ttm,
                    "ttm_diff": round(diff_low, 2),
                    "ttm_type": type_value,
                })

        def takeTTMDiff(elem):
            return elem["ttm_diff"]

        if len(low_code) < 1:
            raise Exception("数据有问题，data=", low_code)

        fw = open(_log_name, "w+", encoding="utf-8")
        fw.write("# 正常估值的股票\n")
        mid_code.sort(key=takeTTMDiff)
        for data in mid_code:
            fw.write("股票:{0}\t代码:{1}\t当前{5}:{2}\t低估:{3}\t还差:{4}\n".format(data["name"], data["code"], data["ttm_current"], data["ttm_low"], data["ttm_diff"], data["ttm_type"]))

        fw.write("\n# 估值低的股票\n")
        low_code.sort(key=takeTTMDiff)
        for data in low_code:
            fw.write("股票:{0}\t代码:{1}\t当前{5}:{2}\t低估:{3}\t低估:{4}\n".format(data["name"], data["code"], data["ttm_current"], data["ttm_low"], data["ttm_diff"], data["ttm_type"]))

        fw.write("\n# 估值高的股票\n")
        high_code.sort(reverse=True, key=takeTTMDiff)
        if len(high_code) > 0:
            for data in high_code:
                fw.write("股票:{0}\t代码:{1}\t当前{5}:{2}\t高估:{3}\t高估:{4}\n".format(data["name"], data["code"], data["ttm_current"], data["ttm_high"], data["ttm_diff"], data["ttm_type"]))
        else:
            fw.write("无")
        fw.close()


def baostock():
    lg = bs.login()
    if lg.error_code != "0":
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)
    ts = Test(STR_DAY)
    ts.run()
    bs.logout()


def email():
    # 信息
    mail_host = 'smtp.163.com'
    mail_user = 'dadalepai'
    mail_pass = str(base64.b64decode("TkNHWUNHUExKSUpWUEpOVw=="), "utf-8")

    sender = 'dadalepai@163.com'
    receivers = ['1040392895@qq.com']

    f = open(_log_name, "r+", encoding="utf-8")
    content = f.read()
    f.close()

    if len(content) < 1:
        raise Exception("内容为空")

    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    _time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message['Subject'] = "[{0}]股票分析".format(_time_now)
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)


if __name__ == '__main__':
    baostock()
    if is_send_email:
        email()
