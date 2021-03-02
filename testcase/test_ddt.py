import ddt
import unittest

@ddt.ddt()
class MyTestCase(unittest.TestCase):
    # 读取元组数据-单组元素
    @ddt.data(1, 2, 3)
    def test1(self, value):
        print(value)

    # 读取元组数据-多组元素
    @ddt.data([1,2,3],[2,3,4])
    # def test100(self,a,b,c):
    #     print(a,b,c)
    def test100(self,a):
        print(a[0],a[1],a[2])

    @ddt.data((1, 2, 3), (4, 5, 6))
    def test2(self, value):
        print(value)

    # 读取元组数据-拆分数据
    @ddt.data((1, 2, 3), (4, 5, 6))
    @ddt.unpack  # 拆分数据
    def test3(self, value1, value2, value3):
        print(value1, value2, value3)

    # 列表
    @ddt.data([{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}])
    def test4(self, value):
        print(value)

    # 字典
    @ddt.data({'name': 'tom', 'age': '20'}, {'name': 'kite', 'age': '30'})
    def test5(self, value):
        print(value)

    # 字典-拆分
    @ddt.data({'name': 'tom', 'age': '20'}, {'name': 'kite', 'age': '30'})
    @ddt.unpack
    def test6(self, name, age):
        print(name, age)

if __name__ == '__main__':
    unittest.main()
