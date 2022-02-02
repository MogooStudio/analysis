import baostock as bs
import akshare as ak
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
import base64


unit = 100000000.0  # 市值单位
h_value = 1000000 * unit  # 高估值的默认值
e_pe, e_pb, e_value = range(3)  # 指标枚举
e_data, e_code, e_close, e_ttm_pe, e_ttm_pb = range(5)  # 数据枚举
e_threshold = {  # 低估值指标阈值
    e_pe: 5,
    e_pb: 0.5,
    e_value: 100 * unit,
}
_log_name = "stock_data.txt"
is_send_email = True

# 指定日期
_date_time = datetime.date(2022, 1, 29)

today = datetime.date.today()  # 今天日期
if today > _date_time:
    today = _date_time
delta = -1
if today.weekday() == 6:
    delta = -2  # 如果今天是星期日
elif today.weekday() == 0:
    delta = -3  # 如果今天是星期一
day = today + datetime.timedelta(days=delta)  # 查询日期
STR_DAY = day.strftime('%Y-%m-%d')
print("delta=", delta)
print("今天日期：{0}|{1}，查询日期：{2}|{3}".format(today, today.weekday(), STR_DAY, day.weekday()))


stock_all = {  # 股票数据
        # wx
        "002714": {"name": "牧原股份", "type": e_value, "low": 2500*unit, "high": 6000*unit},
        "600036": {"name": "招商银行", "type": e_pb, "low": 1.5, "high": h_value},
        "603899": {"name": "晨光文具", "type": e_pe, "low": 32, "high": h_value},
        "601100": {"name": "恒立液压", "type": e_pe, "low": 34, "high": h_value},
        "603195": {"name": "公牛集团", "type": e_pe, "low": 30, "high": h_value},
        "601636": {"name": "旗滨集团", "type": e_pe, "low": 9, "high": h_value},
        "600276": {"name": "恒瑞医药", "type": e_pe, "low": 50, "high": h_value},
        "000661": {"name": "长春高新", "type": e_pe, "low": 30, "high": h_value},
        "002230": {"name": "科大讯飞", "type": e_pe, "low": 60, "high": h_value},
        "300999": {"name": "金龙鱼", "type": e_pe, "low": 50, "high": h_value},
        "601888": {"name": "中国中免", "type": e_pe, "low": 30, "high": h_value},
        "300759": {"name": "康龙化成", "type": e_pe, "low": 60, "high": h_value},
        "002241": {"name": "歌尔股份", "type": e_pe, "low": 35, "high": h_value},
        "300347": {"name": "泰格医药", "type": e_pe, "low": 48, "high": h_value},
        "300274": {"name": "阳光电源", "type": e_pe, "low": 34, "high": h_value},
        "600887": {"name": "伊利股份", "type": e_pe, "low": 25, "high": 35},
        "603486": {"name": "科沃斯", "type": e_pe, "low": 40, "high": h_value},
        "002475": {"name": "立讯精密", "type": e_pe, "low": 32, "high": h_value},
        "002415": {"name": "海康威视", "type": e_pe, "low": 24, "high": h_value},
        "603259": {"name": "药明康德", "type": e_pe, "low": 60, "high": h_value},
        "000333": {"name": "美的集团", "type": e_pe, "low": 15, "high": 25},
        "600438": {"name": "通威股份", "type": e_pe, "low": 20, "high": h_value},
        "002027": {"name": "分众传媒", "type": e_pe, "low": 17, "high": h_value},
        "601012": {"name": "隆基股份", "type": e_pe, "low": 20, "high": h_value},
        "300015": {"name": "爱尔眼科", "type": e_pe, "low": 70, "high": h_value},
        "601155": {"name": "新城控股", "type": e_pe, "low": 4.5, "high": h_value},
        "600298": {"name": "安琪酵母", "type": e_pe, "low": 27, "high": h_value},
        "002352": {"name": "顺丰控股", "type": e_pe, "low": 30, "high": h_value},
        "601877": {"name": "正泰电器", "type": e_pe, "low": 14, "high": h_value},
        "000858": {"name": "五粮液", "type": e_pe, "low": 28, "high": h_value},
        "601225": {"name": "陕西煤业", "type": e_pe, "low": 6.7, "high": h_value},
        # "601225": {"name": "陕西煤业", "type": e_value, "low": 1100, "high": h_value},
        "601615": {"name": "明阳智能", "type": e_pe, "low": 18, "high": h_value},
        "002271": {"name": "东方雨虹", "type": e_pe, "low": 20, "high": h_value},
        "600085": {"name": "同仁堂", "type": e_pe, "low": 36, "high": h_value},
        "002304": {"name": "洋河股份", "type": e_pe, "low": 24, "high": h_value},
        "000538": {"name": "云南白药", "type": e_pe, "low": 24, "high": h_value},
        "603369": {"name": "今世缘", "type": e_pe, "low": 23, "high": h_value},
        "600332": {"name": "白云山", "type": e_pe, "low": 14, "high": h_value},
        "300595": {"name": "欧普康视", "type": e_pe, "low": 48, "high": h_value},
        "600905": {"name": "三峡能源", "type": e_pe, "low": 35, "high": h_value},
        "603127": {"name": "昭衍新药", "type": e_pe, "low": 60, "high": h_value},
        "601166": {"name": "兴业银行", "type": e_pb, "low": 0.75, "high": h_value},
        "600989": {"name": "宝丰能源", "type": e_pe, "low": 16, "high": h_value},
        "600383": {"name": "金地集团", "type": e_pe, "low": 6, "high": h_value},
        "600309": {"name": "万华化学", "type": e_pe, "low": 13, "high": h_value},
        "002372": {"name": "伟星新材", "type": e_pe, "low": 20, "high": h_value},
        "603087": {"name": "甘李药业", "type": e_pe, "low": 24, "high": h_value},
        "600763": {"name": "通策医疗", "type": e_pe, "low": 60, "high": h_value},
        "300529": {"name": "健帆生物", "type": e_pe, "low": 38, "high": h_value},
        "002555": {"name": "三七互娱", "type": e_pe, "low": 19, "high": h_value},
        "000786": {"name": "北新建材", "type": e_value, "low": 500, "high": h_value},
        "600030": {"name": "中信证券", "type": e_pb, "low": 1.3, "high": h_value},
        "603019": {"name": "中科曙光", "type": e_pe, "low": 42, "high": h_value},
        "300144": {"name": "宋城演艺", "type": e_value, "low": 360, "high": h_value},
        "600570": {"name": "恒生电子", "type": e_pe, "low": 46, "high": h_value},
        "600201": {"name": "生物股份", "type": e_pe, "low": 42, "high": h_value},
        "002236": {"name": "大华股份", "type": e_pe, "low": 16, "high": h_value},
        "002216": {"name": "三全食品", "type": e_pe, "low": 22, "high": h_value},
        "600585": {"name": "海螺水泥", "type": e_pe, "low": 6, "high": h_value},
        "600436": {"name": "片仔癀", "type": e_pe, "low": 50, "high": h_value},
        "000568": {"name": "泸州老窖", "type": e_pe, "low": 26, "high": h_value},
        "603606": {"name": "东方电缆", "type": e_pe, "low": 25, "high": h_value},
        "603288": {"name": "海天味业", "type": e_pe, "low": 50, "high": h_value},
        "600809": {"name": "山西汾酒", "type": e_pe, "low": 34, "high": h_value},
        # self
        "002597": {"name": "金禾实业", "type": e_pe, "low": 22, "high": h_value},
        "000963": {"name": "华东医药", "type": e_pe, "low": 21, "high": h_value},
        "002594": {"name": "比亚迪", "type": e_pe, "low": 155, "high": h_value},
        "603236": {"name": "移远通信", "type": e_pe, "low": 85, "high": h_value},
        "002791": {"name": "坚朗五金", "type": e_pe, "low": 46, "high": h_value},
        "601658": {"name": "邮储银行", "type": e_pb, "low": 0.8, "high": h_value},
        "603833": {"name": "欧派家居", "type": e_pe, "low": 28, "high": h_value},
        "002920": {"name": "德赛西威", "type": e_pe, "low": 72, "high": h_value},
        "600745": {"name": "闻泰科技", "type": e_pe, "low": 44, "high": h_value},
        "600600": {"name": "青岛啤酒", "type": e_pe, "low": 33, "high": h_value},
        "002311": {"name": "海大集团", "type": e_pe, "low": 38, "high": h_value},
        "600885": {"name": "宏发股份", "type": e_pe, "low": 28, "high": h_value},
        "002410": {"name": "广联达", "type": e_pe, "low": 60, "high": h_value},
        "002032": {"name": "苏泊尔", "type": e_pe, "low": 22, "high": h_value},
        "600845": {"name": "宝信软件", "type": e_pe, "low": 38, "high": h_value},
        "002557": {"name": "洽洽食品", "type": e_pe, "low": 23, "high": h_value},
        # "600754": {"name": "锦江酒店", "type": e_pe, "low": 18, "high": h_value},
        "603939": {"name": "益丰药房", "type": e_pe, "low": 38, "high": h_value},
        "000049": {"name": "德赛电池", "type": e_pe, "low": 18, "high": h_value},
        "000651": {"name": "格力电器", "type": e_pe, "low": 9, "high": h_value},
        "000002": {"name": "万科A", "type": e_pe, "low": 6, "high": h_value},
    }


class Test:

    def __init__(self, _data):
        self.start_date = _data
        self.end_date = _data
        self.data_list = []

    # 获取股票市值
    def get_market(self, god):
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=god)
        value = stock_individual_info_em_df.head(1).get("value")
        return round(float(value), 6)

    # 获取股票指标
    def get_TTM(self, god):
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

    def getCode(self, code):
        god = "sh" if code and code[0] == "6" else "sz"
        return god + "." + code

    def test(self, code):
        god = self.getCode(code)
        rs = bs.query_history_k_data_plus(god,
                                          "date,code,close,peTTM,psTTM",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        print(result)

    def run(self):
        for code, _ in stock_all.items():
            god = self.getCode(code)
            print("获取股票代码数据:{0}".format(god))
            self.get_TTM(god)

        low_code, high_code = [], []
        for stock_data in self.data_list:
            stock_code = str(stock_data[e_code])
            real_code = stock_code.split('.')[1]
            code_data = stock_all.get(real_code)
            code_name = code_data["name"]
            low_ttm = code_data["low"]
            high_ttm = code_data["high"]
            type_ttm = code_data["type"]
            value_low = e_threshold[type_ttm]
            if type_ttm == e_pe:
                real_ttm = stock_data[e_ttm_pe]
            elif type_ttm == e_pb:
                real_ttm = stock_data[e_ttm_pb]
            elif type_ttm == e_value:
                real_ttm = self.get_market(real_code)
            diff_low = float(real_ttm) - float(low_ttm)
            diff_high = float(real_ttm) - float(high_ttm)
            if diff_low <= value_low:
                low_code.append({
                    "name": code_name,
                    "code": stock_code,
                    "ttm_current": round(float(real_ttm), 2),
                    "ttm_low": low_ttm,
                    "ttm_diff": round(diff_low, 2),
                })
            elif diff_high >= 0:
                high_code.append({
                    "name": code_name,
                    "code": stock_code,
                    "ttm_current": round(float(real_ttm), 2),
                    "ttm_high": high_ttm,
                    "ttm_diff": round(diff_high, 2),
                })

        def takeTTMDiff(elem):
            return elem["ttm_diff"]

        if len(low_code) < 1:
            raise Exception("数据有问题，data=", low_code)

        fw = open(_log_name, "w+", encoding="utf-8")
        fw.write("# 筛选低估值的股票\n")
        low_code.sort(key=takeTTMDiff)
        for data in low_code:
            fw.write("股票:{0}\t代码:{1}\t当前值:{2}\t低估值:{3}\t还差:{4}\n".format(data["name"], data["code"], data["ttm_current"], data["ttm_low"], data["ttm_diff"]))

        fw.write("\n# 剔除估值高的股票\n")
        high_code.sort(reverse=True, key=takeTTMDiff)
        if len(high_code) > 0:
            for data in high_code:
                fw.write("股票:{0}\t代码:{1}\t当前值:{2}\t高估值:{3}\t高出:{4}\n".format(data["name"], data["code"], data["ttm_current"], data["ttm_high"], data["ttm_diff"]))
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
    # ts.test("600887")
    bs.logout()


def email():
    # 信息
    mail_host = 'smtp.163.com'
    mail_user = 'dadalepai'
    mail_pass = str(base64.b64decode("TkNHWUNHUExKSUpWUEpOVw=="), "utf-8")

    sender = 'dadalepai@163.com'
    receivers = ['1040392895@qq.com']

    fr = open(_log_name, "r+", encoding="utf-8")
    content = fr.read()
    fr.close()

    if len(content) < 1:
        raise Exception("读取内容错误")

    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = "[{0}]股票分析".format(today)
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
        print('error', e)  # 打印错误


if __name__ == '__main__':
    baostock()
    if is_send_email:
        email()
