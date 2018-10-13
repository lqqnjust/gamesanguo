# coding:utf-8


def level(exp):
    """
    计算当前经验对应的等级
    :param exp:
    :return:
    """
    if exp < 20:
        return 1
    elif exp < 40:
        return 2
    elif exp < 70:
        return 3
    elif exp < 100:
        return 4
    elif exp < 150:
        return 5
    elif exp < 200:
        return 6
    elif exp < 300:
        return 7
    else:
        return 8

def army_layout(wuli, level):
    """
    获取部队兵种分布
    :param wuli: 武力
    :param level: 等级
    :return:
    """