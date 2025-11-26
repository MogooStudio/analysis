
unit = 100000000.0  # 市值单位
h_value = 1000000 * unit  # 高估值的默认值
e_pe, e_pb, e_value, e_price = range(4)  # 指标枚举
e_data, e_code, e_close, e_ttm_pe, e_ttm_pb = range(5)  # 数据枚举

stock_all = {  # 股票数据
        # wx
        "600036": {"name": "招商银行", "type": e_pb, "low": 0.9, "high": 2.1},
        "603195": {"name": "公牛集团", "type": e_pe, "low": 20, "high": h_value},
        "600276": {"name": "恒瑞医药", "type": e_pe, "low": 40, "high": h_value},
        "600887": {"name": "伊利股份", "type": e_pe, "low": 22, "high": 35},
        "002415": {"name": "海康威视", "type": e_pe, "low": 20, "high": h_value},
        "000333": {"name": "美的集团", "type": e_pe, "low": 13, "high": 25},
        "002027": {"name": "分众传媒", "type": e_pe, "low": 17, "high": h_value},
        "600519": {"name": "贵州茅台", "type": e_pe, "low": 20, "high": h_value},
        "000858": {"name": "五粮液", "type": e_pe, "low": 15, "high": h_value},
        "601225": {"name": "陕西煤业", "type": e_value, "low": 1500*unit, "high": 2000*unit},
        "600085": {"name": "同仁堂", "type": e_pe, "low": 36, "high": h_value},
        "000538": {"name": "云南白药", "type": e_pe, "low": 22, "high": h_value},
        "601166": {"name": "兴业银行", "type": e_pb, "low": 0.6, "high": h_value},
        "600309": {"name": "万华化学", "type": e_pe, "low": 13, "high": h_value},
        "002372": {"name": "伟星新材", "type": e_pe, "low": 20, "high": h_value},
        "600436": {"name": "片仔癀", "type": e_pe, "low": 40, "high": h_value},
        "000568": {"name": "泸州老窖", "type": e_price, "low": 115, "high": h_value},
        "603288": {"name": "海天味业", "type": e_pe, "low": 34, "high": h_value},
        "600176": {"name": "中国巨石", "type": e_pe, "low": 15, "high": h_value},
        "600660": {"name": "福耀玻璃", "type": e_pe, "low": 15, "high": h_value},
        "600900": {"name": "长江电力", "type": e_pe, "low": 16, "high": h_value},
        "601088": {"name": "中国神华", "type": e_pb, "low": 1, "high": h_value},
        "600690": {"name": "海尔智家", "type": e_pe, "low": 13, "high": h_value},
        "600612": {"name": "老凤祥", "type": e_pe, "low": 12, "high": h_value},
        "000651": {"name": "格力电器", "type": e_pe, "low": 7.5, "high": h_value},
        "601899": {"name": "紫金矿业", "type": e_pe, "low": 11, "high": h_value},
        "000338": {"name": "潍柴动力", "type": e_pe, "low": 10, "high": h_value},
        "000001": {"name": "平安银行", "type": e_price, "low": 10, "high": h_value},
        "002064": {"name": "华峰化学", "type": e_price, "low": 7, "high": h_value},
        "603259": {"name": "药明康德", "type": e_price, "low": 50, "high": h_value},
        "300760": {"name": "迈瑞医疗", "type": e_pe, "low": 30, "high": h_value},
        "600938": {"name": "中国海油", "type": e_pe, "low": 7, "high": h_value},
        "603605": {"name": "珀莱雅", "type": e_pe, "low": 20, "high": h_value},
        "002714": {"name": "牧原股份", "type": e_value, "low": 2500*unit, "high": 6000*unit},
        "300750": {"name": "宁德时代", "type": e_pe, "low": 18, "high": h_value},
        # "03690": {"name": "美团", "type": e_value, "low": 7500*unit, "high": h_value},
        # "09988": {"name": "阿里巴巴", "type": e_pe, "low": 15, "high": h_value},
        # "00700": {"name": "腾讯控股", "type": e_pe, "low": 20, "high": h_value},
        # "06160": {"name": "百济神州", "type": e_price, "low": 1400, "high": h_value},
    }
