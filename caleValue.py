# 市值 totalValue
# 股价 value
# 利润 profit
# 净利润率 pm

lzlj = {
    "name": "泸州老窖",
    "totalValue": 2301.41,
    "value": 156.35,
    "profit": 102,
    "pm": 20,
}

wly = {
    "name": "五粮液",
    "totalValue": 5181.95,
    "value": 133.5,
    "profit": 270,
    "pm": 20,
}

stock_list = [lzlj, wly]

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
    ret = {}

    for info in stock_list:
        cale(info)

    #
    # print(ret1, ret2)


if __name__ == '__main__':
    run()
