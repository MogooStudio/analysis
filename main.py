import baostock as bs
import akshare as ak
import pandas as pd
import os
import datetime

root = "C:/Users/Administrator/Desktop/"
unit = 100000000.0
e_pe, e_pb, e_value = range(3)
e_data, e_code, e_close, e_ttm_pe, e_ttm_pb = range(5)
e_threshold = {
    e_pe: 5,
    e_pb: 1,
    e_value: 100 * unit,
}
STR_DAY = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
print(STR_DAY)


stock_all = {
        # wx
        "002714": {"name": "牧原股份", "class": "sz", "valid": True, "type": e_value, "low": 2500*unit},
        "600036": {"name": "招商银行", "class": "sh", "valid": True, "type": e_pb, "low": 1.5},
        "603899": {"name": "晨光文具", "class": "sh", "valid": True, "type": e_pe, "low": 32},
        "601100": {"name": "恒立液压", "class": "sh", "valid": True, "type": e_pe, "low": 34},
        "603195": {"name": "公牛集团", "class": "sh", "valid": True, "type": e_pe, "low": 30},
        "601636": {"name": "旗滨集团", "class": "sh", "valid": True, "type": e_pe, "low": 9},
        "600276": {"name": "恒瑞医药", "class": "sh", "valid": True, "type": e_pe, "low": 50},
        "000661": {"name": "长春高新", "class": "sz", "valid": True, "type": e_pe, "low": 30},
        "002230": {"name": "科大讯飞", "class": "sz", "valid": True, "type": e_pe, "low": 60},
        "300999": {"name": "金龙鱼", "class": "sz", "valid": False, "type": e_pe, "low": 50},
        "601888": {"name": "中国中免", "class": "sh", "valid": True, "type": e_pe, "low": 30},
        "300759": {"name": "康龙化成", "class": "sz", "valid": False, "type": e_pe, "low": 60},
        "002241": {"name": "歌尔股份", "class": "sz", "valid": True, "type": e_pe, "low": 35},
        "300347": {"name": "泰格医药", "class": "sz", "valid": False, "type": e_pe, "low": 48},
        "300274": {"name": "阳光电源", "class": "sz", "valid": False, "type": e_pe, "low": 34},
        "600887": {"name": "伊利股份", "class": "sh", "valid": True, "type": e_pe, "low": 25},
        "603486": {"name": "科沃斯", "class": "sh", "valid": True, "type": e_pe, "low": 40},
        "002475": {"name": "立讯精密", "class": "sz", "valid": True, "type": e_pe, "low": 32},
        "002415": {"name": "海康威视", "class": "sz", "valid": True, "type": e_pe, "low": 24},
        "603259": {"name": "药明康德", "class": "sh", "valid": True, "type": e_pe, "low": 60},
        "000333": {"name": "美的集团", "class": "sz", "valid": True, "type": e_pe, "low": 15},
        "600438": {"name": "通威股份", "class": "sh", "valid": True, "type": e_pe, "low": 20},
        "002027": {"name": "分众传媒", "class": "sz", "valid": True, "type": e_pe, "low": 17},
        "601012": {"name": "隆基股份", "class": "sh", "valid": True, "type": e_pe, "low": 20},
        "300015": {"name": "爱尔眼科", "class": "sz", "valid": True, "type": e_pe, "low": 70},
        "601155": {"name": "新城控股", "class": "sh", "valid": True, "type": e_pe, "low": 4.5},
        "600298": {"name": "安琪酵母", "class": "sh", "valid": True, "type": e_pe, "low": 0},
        "002352": {"name": "顺丰控股", "class": "sz", "valid": True, "type": e_pe, "low": 30},
        "601877": {"name": "正泰电器", "class": "sh", "valid": True, "type": e_pe, "low": 14},
        "000858": {"name": "五粮液", "class": "sz", "valid": True, "type": e_pe, "low": 28},
        "601225": {"name": "陕西煤业", "class": "sh", "valid": True, "type": e_pe, "low": 6.7},
        "601615": {"name": "明阳智能", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        "002271": {"name": "东方雨虹", "class": "sz", "valid": True, "type": e_pe, "low": 20},
        # self
        "002597": {"name": "金禾实业", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "002698": {"name": "博实股份", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "002594": {"name": "比亚迪", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "603236": {"name": "移远通信", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "002791": {"name": "坚朗五金", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "603986": {"name": "兆易创新", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "603833": {"name": "欧派家居", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "002920": {"name": "德赛西威", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600745": {"name": "闻泰科技", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "603288": {"name": "海天味业", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "000538": {"name": "云南白药", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600600": {"name": "青岛啤酒", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "002311": {"name": "海大集团", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600885": {"name": "宏发股份", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "002410": {"name": "广联达", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "002032": {"name": "苏泊尔", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600845": {"name": "宝信软件", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "002557": {"name": "洽洽食品", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600754": {"name": "锦江酒店", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "603939": {"name": "益丰药房", "class": "sh", "valid": True, "type": e_pe, "low": 18},
        # "000049": {"name": "德赛电池", "class": "sz", "valid": True, "type": e_pe, "low": 18},
        # "600085": {"name": "同仁堂", "class": "sh", "valid": True, "type": e_pe, "low": 18},
    }


def link(filename):
    return os.path.join(root, filename)


class Test:

    def __init__(self, _data):
        self.start_date = _data
        self.end_date = _data
        self.data_list = []
        self.rs = None

    def get_market(self, god):
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=god)
        value = stock_individual_info_em_df.head(1).get("value")
        return round(float(value), 6)

    def get_peTTM(self, god):
        # peTTM    滚动市盈率
        # psTTM    滚动市销率
        rs = bs.query_history_k_data_plus(god,
                                          "date,code,close,peTTM,psTTM",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        if rs.error_code != "0":
            print('query_history_k_data_plus respond error_code:' + rs.error_code)
            print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
        while (rs.error_code == '0') & rs.next():
            self.data_list.append(rs.get_row_data())
        self.rs = rs

    def test(self, god):
        rs = bs.query_history_k_data_plus(god,
                                          "date,code,close,peTTM,psTTM",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")  # frequency="d"取日k线，adjustflag="3"默认不复权
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        print(result)

    def run(self):
        for code, data in stock_all.items():
            god = data["class"] + "." + code
            print("获取股票代码数据:{0}".format(god))
            self.get_peTTM(god)

        print("########################################################################")
        print("#                           筛选低估值的股票                              #")
        print("########################################################################")
        for stock_data in self.data_list:
            stock_code = str(stock_data[e_code])
            real_code = stock_code.split('.')[1]
            code_data = stock_all.get(real_code)
            code_name = code_data["name"]
            valid = code_data["valid"]
            low_ttm = code_data["low"]
            type_ttm = code_data["type"]
            threshold_value = e_threshold[type_ttm]
            if not valid:
                continue
            if type_ttm == e_pe:
                real_ttm = stock_data[e_ttm_pe]
            elif type_ttm == e_pb:
                real_ttm = stock_data[e_ttm_pb]
            elif type_ttm == e_value:
                real_ttm = self.get_market(real_code)
            diff = float(real_ttm) - float(low_ttm)
            if 0 < diff <= threshold_value:
                print("\t股票:{0}\t代码:{1}\t当前值:{2}\t最小值:{3}\t差值:{4}".format(code_name, stock_code, round(float(real_ttm), 2), low_ttm, round(diff, 2)))
        print("########################################################################")


def baostock():
    lg = bs.login()
    if lg.error_code != "0":
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)
    ts = Test(STR_DAY)
    ts.run()
    ts.test("sz.002271")
    bs.logout()


if __name__ == '__main__':
    baostock()

