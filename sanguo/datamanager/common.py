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
    :return: 骑弓步比例
    """
    if wuli < 50:
        if level == 1:
            return 0, 3, 7
        elif level == 2:
            return 0, 4, 6
        elif level == 3:
            return 1, 4, 5
        elif level == 4:
            return 2, 3, 5
        elif level == 5:
            return 2, 4, 4
        elif level == 6:
            return 3, 4, 3
        elif level == 7:
            return 4, 3, 3
        elif level == 8:
            return 4, 4, 2
    elif wuli < 80:
        if level == 1:
            return 1, 2, 7
        elif level == 2:
            return 1, 3, 6
        elif level == 3:
            return 2, 3, 5
        elif level == 4:
            return 2, 3, 5
        elif level == 5:
            return 3, 3, 4
        elif level == 6:
            return 4, 3, 3
        elif level == 7:
            return 5, 3, 2
        elif level == 8:
            return 5, 4, 1
    else:
        if level == 1:
            return 2, 3, 5
        elif level == 2:
            return 2, 4, 4
        elif level == 3:
            return 3, 3, 4
        elif level == 4:
            return 4, 3, 3
        elif level == 5:
            return 5, 3, 2
        elif level == 6:
            return 5, 4, 1
        elif level == 7:
            return 6, 3, 1
        elif level == 8:
            return 6, 4, 0
