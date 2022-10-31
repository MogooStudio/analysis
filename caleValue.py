
# 估计计算

lzlj = {
    "name": "泸州老窖",
    "totalValue": 2301.41,  # 市值
    "value": 156.35,        # 股价
    "profit": 102,          # 净利润
    "pm": 20,               # 10年平均净利润率
}

wly = {
    "name": "五粮液",
    "totalValue": 5181.95,
    "value": 133.5,
    "profit": 270,
    "pm": 20,
}

ymkd = {
    "name": "药明康德",
    "totalValue": 2261.77,
    "value": 76.4,
    "profit": 99.5,
    "pm": 25,
}

hkws = {
    "name": "海康威视",
    "totalValue": 2680.92,
    "value": 28.42,
    "profit": 174,
    "pm": 20,
}

ylgf = {
    "name": "伊利股份",
    "totalValue": 1615.2,
    "value": 25.24,
    "profit": 98,
    "pm": 20,
}

stock_list = [lzlj, wly, ymkd, hkws, ylgf]

# PE
pe_dict = {
    5: [8.7, 14.5],
    10: [10, 16.6],
    15: [11.4, 19],
    20: [13, 21.6],
    25: [14.6, 24.4],
}


def cale(info):
    totalValue = info["totalValue"]
    value = info["value"]
    profit = info["profit"]
    pm = info["pm"]
    name = info["name"]

    rate = totalValue / value * 1.0

    pe1 = pe_dict[pm][0]
    pe2 = pe_dict[pm][1]

    temp1 = pe1 * profit
    temp2 = pe2 * profit

    # 结果
    ret1 = temp1 / rate
    ret2 = temp2 / rate

    print(name, str(pm) + "%", ret1, ret2)


def run():
    for info in stock_list:
        cale(info)


if __name__ == '__main__':
    run()
