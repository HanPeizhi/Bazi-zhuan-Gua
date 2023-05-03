# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# 五行生数，干支阳取生数，即奇数
wxds = {
    '水': 1,
    '火': 7,
    '木': 3,
    '金': 9,
    '土': 5
}

# 五行成数，干支阴取成数，即偶数
wxss = {
    '水': 6,
    '火': 2,
    '木': 8,
    '金': 4,
    '土': 10
}

# 天干之五行
tgwx = {
    '甲': '木',
    '乙': '木',
    '丙': '火',
    '丁': '火',
    '戊': '土',
    '己': '土',
    '庚': '金',
    '辛': '金',
    '壬': '水',
    '癸': '水'
}

# 地支之五行
dzwx = {
    '子': '水',
    '丑': '土',
    '寅': '木',
    '卯': '木',
    '辰': '土',
    '巳': '火',
    '午': '火',
    '未': '土',
    '申': '金',
    '酉': '金',
    '戌': '土',
    '亥': '水'
}

# 天干地支的阴阳，1为阳，0为阴
# 巳午亥子小心，反的
# 干支顺序
gzsx = ['空', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸',  # 10
        '亥', '丑', '寅', '卯', '辰', '午', '巳', '未', '申', '酉', '戌', '子'  # 22
        ]


# 干支阳取奇数，阴取偶数
# z为输入的一个字，先判断是天干还是地支
# 干支对应的数
def gzs(z):
    # 干支序数
    gzxs = gzsx.index(z)

    # 先判断是天干还是地支，根据干支的序数判断是阴还是阳，然后根据阴阳取生数还是成熟
    if 0 < gzxs <= 10:  # 则为天干
        yys = gzxs % 2
        if yys == 1:
            return wxds[tgwx[z]]
        elif yys == 0:
            return wxss[tgwx[z]]
        else:
            print('天干阴阳错误！')

    elif 11 <= gzxs <= 22:  # 则为地支
        yys = gzxs % 2
        if yys == 1:
            return wxds[dzwx[z]]
        elif yys == 0:
            return wxss[dzwx[z]]
        else:
            print('地支阴阳错误！')

    else:
        print('错误干支序数！')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 年干支
    ngz = input('年干支：')
    g = ngz[0]
    z = ngz[1]
    six = (gzs(g) + gzs(z)) % 8

    # 月干支
    ygz = input('月干支：')
    g = ygz[0]
    z = ygz[1]
    five = gzs(z) % 8
    four = gzs(g) % 8

    # 日干支
    rgz = input('日干支：')
    g = rgz[0]
    z = rgz[1]
    three = (gzs(g) + gzs(z)) % 8

    # 时干支
    sgz = input('时干支：')
    g = sgz[0]
    z = sgz[1]
    two = gzs(z) % 8
    one = gzs(g) % 8

    print('奇为阳爻，偶为阴爻，1为阳动，8为阴动')
    print(six)
    print(five)
    print(four)
    print(three)
    print(two)
    print(one)
