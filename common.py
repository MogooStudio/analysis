
unit = 100000000.0  # 市值单位
h_value = 1000000 * unit  # 高估值的默认值
e_pe, e_pb, e_value = range(3)  # 指标枚举
e_data, e_code, e_close, e_ttm_pe, e_ttm_pb = range(5)  # 数据枚举
e_threshold = {  # 低估值指标阈值
    e_pe: 5,
    e_pb: 0.5,
    e_value: 10 * unit,
}

stock_all = {  # 股票数据
        # wx
        "002714": {"name": "牧原股份", "type": e_value, "low": 2500*unit, "high": 6000*unit},
        "600036": {"name": "招商银行", "type": e_pb, "low": 1.5, "high": 2.1},
        "603899": {"name": "晨光文具", "type": e_pe, "low": 32, "high": h_value},
        "601100": {"name": "恒立液压", "type": e_pe, "low": 34, "high": h_value},
        "603195": {"name": "公牛集团", "type": e_pe, "low": 30, "high": h_value},
        "600276": {"name": "恒瑞医药", "type": e_pe, "low": 50, "high": h_value},
        "000661": {"name": "长春高新", "type": e_pe, "low": 18, "high": h_value},
        "002230": {"name": "科大讯飞", "type": e_pe, "low": 50, "high": h_value},
        "300999": {"name": "金龙鱼", "type": e_pe, "low": 50, "high": h_value},
        "601888": {"name": "中国中免", "type": e_pe, "low": 30, "high": h_value},
        "300759": {"name": "康龙化成", "type": e_pe, "low": 45, "high": h_value},
        "002241": {"name": "歌尔股份", "type": e_pe, "low": 26, "high": h_value},
        "300347": {"name": "泰格医药", "type": e_pe, "low": 30, "high": h_value},
        "300274": {"name": "阳光电源", "type": e_pe, "low": 34, "high": h_value},
        "600887": {"name": "伊利股份", "type": e_pe, "low": 22, "high": 35},
        "002475": {"name": "立讯精密", "type": e_pe, "low": 28, "high": h_value},
        "002415": {"name": "海康威视", "type": e_pe, "low": 20, "high": h_value},
        "603259": {"name": "药明康德", "type": e_pe, "low": 30, "high": h_value},
        "000333": {"name": "美的集团", "type": e_pe, "low": 12, "high": 25},
        "600438": {"name": "通威股份", "type": e_pe, "low": 16, "high": h_value},
        "002027": {"name": "分众传媒", "type": e_pe, "low": 17, "high": h_value},
        "601012": {"name": "隆基绿能", "type": e_pe, "low": 24, "high": h_value},
        "300015": {"name": "爱尔眼科", "type": e_pe, "low": 70, "high": h_value},
        "601155": {"name": "新城控股", "type": e_pe, "low": 4.5, "high": h_value},
        "600298": {"name": "安琪酵母", "type": e_pe, "low": 27, "high": 43},
        "002352": {"name": "顺丰控股", "type": e_pe, "low": 32, "high": h_value},
        "601877": {"name": "正泰电器", "type": e_pe, "low": 14, "high": h_value},
        "000858": {"name": "五粮液", "type": e_pe, "low": 25, "high": h_value},
        "601225": {"name": "陕西煤业", "type": e_value, "low": 1100*unit, "high": 2000*unit},
        "002271": {"name": "东方雨虹", "type": e_pe, "low": 20, "high": h_value},
        "600085": {"name": "同仁堂", "type": e_pe, "low": 36, "high": h_value},
        "002304": {"name": "洋河股份", "type": e_pe, "low": 24, "high": h_value},
        "000538": {"name": "云南白药", "type": e_pe, "low": 24, "high": h_value},
        "603369": {"name": "今世缘", "type": e_pe, "low": 23, "high": h_value},
        "300595": {"name": "欧普康视", "type": e_pe, "low": 48, "high": h_value},
        "601166": {"name": "兴业银行", "type": e_pb, "low": 0.75, "high": h_value},
        "600989": {"name": "宝丰能源", "type": e_pe, "low": 16, "high": h_value},
        "600383": {"name": "金地集团", "type": e_pe, "low": 6, "high": h_value},
        "600309": {"name": "万华化学", "type": e_pe, "low": 13, "high": h_value},
        "002372": {"name": "伟星新材", "type": e_pe, "low": 20, "high": h_value},
        "603087": {"name": "甘李药业", "type": e_pe, "low": 24, "high": h_value},
        "600763": {"name": "通策医疗", "type": e_pe, "low": 60, "high": h_value},
        "300529": {"name": "健帆生物", "type": e_pe, "low": 26, "high": h_value},
        "000786": {"name": "北新建材", "type": e_value, "low": 500*unit, "high": h_value},
        "600570": {"name": "恒生电子", "type": e_pe, "low": 42, "high": h_value},
        "002236": {"name": "大华股份", "type": e_pe, "low": 16, "high": h_value},
        "002216": {"name": "三全食品", "type": e_pe, "low": 22, "high": h_value},
        "600585": {"name": "海螺水泥", "type": e_pe, "low": 6, "high": h_value},
        "600436": {"name": "片仔癀", "type": e_pe, "low": 50, "high": h_value},
        "000568": {"name": "泸州老窖", "type": e_pe, "low": 25, "high": h_value},
        "603288": {"name": "海天味业", "type": e_pe, "low": 50, "high": h_value},
        "600809": {"name": "山西汾酒", "type": e_pe, "low": 34, "high": h_value},
        "600176": {"name": "中国巨石", "type": e_pe, "low": 15, "high": h_value},
        "600660": {"name": "福耀玻璃", "type": e_pe, "low": 15, "high": h_value},
        "601865": {"name": "福莱特", "type": e_pe, "low": 30, "high": h_value},
        "002410": {"name": "广联达", "type": e_pe, "low": 70, "high": h_value},
        "300059": {"name": "东方财富", "type": e_pb, "low": 4.5, "high": h_value},
        "002821": {"name": "凯莱英", "type": e_pe, "low": 20, "high": h_value},
        "600900": {"name": "长江电力", "type": e_pe, "low": 15, "high": h_value},
        "300896": {"name": "爱美客", "type": e_pe, "low": 80, "high": h_value},
        "002791": {"name": "坚朗五金", "type": e_pe, "low": 28, "high": h_value},
        "000002": {"name": "万科A", "type": e_pe, "low": 6, "high": h_value},
        "000049": {"name": "德赛电池", "type": e_pe, "low": 15, "high": h_value},
        "600323": {"name": "瀚蓝环境", "type": e_pe, "low": 13, "high": h_value},
        "603127": {"name": "昭衍新药", "type": e_pe, "low": 30, "high": h_value},
        "601088": {"name": "中国神华", "type": e_pe, "low": 8.5, "high": h_value},
        "002677": {"name": "浙江美大", "type": e_pe, "low": 13, "high": h_value},
        "300750": {"name": "宁德时代", "type": e_pe, "low": 40, "high": h_value},
        "600690": {"name": "海尔智家", "type": e_pe, "low": 15, "high": h_value},
        "002507": {"name": "涪陵榨菜", "type": e_pe, "low": 22, "high": h_value},
        "002508": {"name": "老板电器", "type": e_pe, "low": 14, "high": h_value},
        "603517": {"name": "绝味食品", "type": e_pe, "low": 20, "high": h_value},
        "000001": {"name": "平安银行", "type": e_pb, "low": 1, "high": h_value},
        "002557": {"name": "洽洽食品", "type": e_pe, "low": 23, "high": 35},
        "600612": {"name": "老凤祥", "type": e_pe, "low": 12, "high": h_value},
        "603486": {"name": "科沃斯", "type": e_pe, "low": 25, "high": h_value},
        "601615": {"name": "明阳智能", "type": e_pe, "low": 12, "high": h_value},
        "600332": {"name": "白云山", "type": e_pe, "low": 14, "high": h_value},
        "600905": {"name": "三峡能源", "type": e_pe, "low": 33, "high": h_value},
        "600030": {"name": "中信证券", "type": e_pb, "low": 1.3, "high": h_value},
        "600305": {"name": "恒顺醋业", "type": e_pe, "low": 32, "high": h_value},
        "601966": {"name": "玲珑轮胎", "type": e_pe, "low": 18, "high": h_value},
        "688169": {"name": "石头科技", "type": e_pe, "low": 22, "high": h_value},
        "002240": {"name": "盛新锂能", "type": e_pe, "low": 18, "high": h_value},
        "002460": {"name": "赣锋锂业", "type": e_pe, "low": 20, "high": h_value},
        "603658": {"name": "安图生物", "type": e_pe, "low": 22, "high": h_value},
        "000876": {"name": "新希望", "type": e_value, "low": 600, "high": h_value},
        "300285": {"name": "国瓷材料", "type": e_pe, "low": 36, "high": h_value},
        "300699": {"name": "光威复材", "type": e_pe, "low": 33, "high": h_value},
        "002709": {"name": "天赐材料", "type": e_pe, "low": 18, "high": h_value},
        "600196": {"name": "复星医药", "type": e_pe, "low": 21, "high": h_value},
        "300014": {"name": "亿纬锂能", "type": e_pe, "low": 40, "high": h_value},
        "000848": {"name": "承德露露", "type": e_pe, "low": 15, "high": h_value},
        "300760": {"name": "迈瑞医疗", "type": e_pe, "low": 40, "high": h_value},
        "603606": {"name": "东方电缆", "type": e_pe, "low": 25, "high": h_value},
        "002007": {"name": "华兰生物", "type": e_pe, "low": 30, "high": h_value},
        "300144": {"name": "宋城演艺", "type": e_value, "low": 360*unit, "high": h_value},
        "000830": {"name": "鲁西化工", "type": e_pe, "low": 8, "high": h_value},
        "601636": {"name": "旗滨集团", "type": e_pe, "low": 9, "high": h_value},
        "002555": {"name": "三七互娱", "type": e_pe, "low": 19, "high": h_value},
        "603019": {"name": "中科曙光", "type": e_pe, "low": 42, "high": h_value},
        "600183": {"name": "生益科技", "type": e_pe, "low": 20, "high": h_value},
        "600137": {"name": "浪姿股份", "type": e_pe, "low": 36, "high": h_value},
        "600201": {"name": "生物股份", "type": e_pe, "low": 42, "high": h_value},
        "603986": {"name": "兆易创新", "type": e_pe, "low": 24, "high": h_value},
        "603866": {"name": "桃李面包", "type": e_pe, "low": 25, "high": h_value},
        "600741": {"name": "华域汽车", "type": e_pe, "low": 8, "high": h_value},
        "603501": {"name": "韦尔股份", "type": e_pe, "low": 30, "high": h_value},
        "600845": {"name": "宝信软件", "type": e_pe, "low": 36, "high": h_value},
        "600771": {"name": "广誉远", "type": e_value, "low": 100, "high": h_value},
        "600511": {"name": "国药股份", "type": e_pe, "low": 11, "high": h_value},
        "600406": {"name": "国电南瑞", "type": e_pe, "low": 22, "high": h_value},
        "300037": {"name": "新宙邦", "type": e_pe, "low": 17, "high": h_value},
        "002139": {"name": "拓邦股份", "type": e_pe, "low": 26, "high": h_value},
        "300003": {"name": "乐普医疗", "type": e_pe, "low": 20, "high": h_value},
        "603027": {"name": "千禾味业", "type": e_pe, "low": 38, "high": h_value},
        "603605": {"name": "珀莱雅", "type": e_pe, "low": 50, "high": h_value},
        "000651": {"name": "格力电器", "type": e_pe, "low": 8, "high": h_value},
        "601899": {"name": "紫金矿业", "type": e_pe, "low": 11, "high": h_value},
        "600089": {"name": "特变电工", "type": e_pe, "low": 6, "high": h_value},
        "000895": {"name": "双汇发展", "type": e_pe, "low": 15, "high": h_value},
        "300122": {"name": "智飞生物", "type": e_pe, "low": 18, "high": h_value},
        "300957": {"name": "贝泰妮", "type": e_pe, "low": 50, "high": h_value},
        "002049": {"name": "紫光国微", "type": e_pe, "low": 36, "high": h_value},
        "600745": {"name": "闻泰科技", "type": e_pe, "low": 24, "high": h_value},
        "002050": {"name": "三花智控", "type": e_pe, "low": 30, "high": h_value},
        "002812": {"name": "恩捷股份", "type": e_pe, "low": 27, "high": h_value},
        "002371": {"name": "北方华创", "type": e_pe, "low": 50, "high": h_value},

        # self
        # "600009": {"name": "上海机场", "type": e_pe, "low": 0, "high": h_value},
        # "600754": {"name": "锦江酒店", "type": e_pe, "low": 0, "high": h_value},
        "002597": {"name": "金禾实业", "type": e_pe, "low": 22, "high": h_value},
        "000963": {"name": "华东医药", "type": e_pe, "low": 21, "high": h_value},
        "002594": {"name": "比亚迪", "type": e_pe, "low": 155, "high": h_value},
        "002920": {"name": "德赛西威", "type": e_pe, "low": 72, "high": h_value},
        "600600": {"name": "青岛啤酒", "type": e_pe, "low": 30, "high": 50},
        "002311": {"name": "海大集团", "type": e_pe, "low": 38, "high": h_value},
        "600885": {"name": "宏发股份", "type": e_pe, "low": 28, "high": h_value},
        "002032": {"name": "苏泊尔", "type": e_pe, "low": 22, "high": h_value},
        "002841": {"name": "视源股份", "type": e_pe, "low": 30, "high": h_value},
        "603589": {"name": "口子窖", "type": e_pe, "low": 16, "high": h_value},
        "600048": {"name": "保利发展", "type": e_pe, "low": 6, "high": h_value},
        "002056": {"name": "横店东磁", "type": e_pe, "low": 18, "high": h_value},
        "603939": {"name": "益丰药房", "type": e_pe, "low": 38, "high": h_value},
        "603882": {"name": "金域医学", "type": e_pe, "low": 17, "high": h_value},
        "002318": {"name": "久立特材", "type": e_pe, "low": 15, "high": h_value},
    }
