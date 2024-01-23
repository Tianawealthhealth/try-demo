import pytest

def romanToInt(s):
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}
    # enumerate()是Python的内置函数之一，一般用于for循环。enumerate()在遍历中可以获得索引和元素值。
    # 例如：
    # s = [1, 2, 3, 4, 5]
    # for i, num in enumerate(s):
    #     print(i, num)
    # 输出结果：
    # 0, 1
    # 1, 2
    # 2, 3
    # 3, 4
    # 4, 5

    # dict.get(key,default=None)返回指定键的值，如果值不在字典里，则返回默认值。
    #d.get(k),k为键名且键名存在时，获取对应k的值
    #d.get(k),k为键名且键名不存在时，获取的值为none。此时值为none时说明键名一定不存在。如果键名存在且值为空，则返回值是空。
    #d.get(k，v),k为键名且键名不存在时，获取的值为v的值。

    return sum(d.get(s[ (max(i - 1, 0)) : i + 1 ], d[n]) for i, n in enumerate(s))


#
def test_one():
    assert romanToInt("IV") == 4

@pytest.mark.parametrize('num,expected',[("IV",4),("IX",9),("LVIII",58),("MCMXCIV",1994)])
def test_two(num,expected):
    assert romanToInt(num) == expected