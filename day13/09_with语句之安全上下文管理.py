
# with open('/tmp/passwd') as f:
#     print(f.read())



class Myopen(object):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode

    def __enter__(self):
    # 当with语句进入并开始执行时， 执行的内容, 需要返回一个对象， 在执行结束之后用来关闭或者其他操作；;
        self.f = open(self.name, self.mode)
        print("正在打开文件%s......" %(self.name))
        return  self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
    # 当with语句执行结束后， 做什么操作
        self.f.close()
        print("文件正在关闭..........")


with Myopen('/tmp/passwd') as f:
    print(f.read())

