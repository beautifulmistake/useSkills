"""
对多层嵌套列表进行展开
"""


def flat(deep_list, result):
    """
    嵌套类表展平的第一种方法: 使用递归实现
    :param deep_list: 目标list：多层嵌套列表
    :param result:
    :return:
    """
    for element in deep_list:
        if isinstance(element, list):
            flat(element, result)
        else:
            result.append(element)


def flat_(deep_list):
    """
    嵌套列表展平的第二种方法：使用生成器
    :param deep_list: 目标list：多层嵌套列表
    :return:
    """
    for element in deep_list:
        if isinstance(element, list):
            yield from flat_(element)
        else:
            yield element


if __name__ == "__main__":
    a = [1, 2, [3, 4, [5, 6, 7], 8], 9, [10, 11]]
    result = [x for x in flat_(a)]
    print(result)
    # result = list()
    # flat(a, result)
    # print(result)
