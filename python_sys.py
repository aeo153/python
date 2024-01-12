
import sys

if __name__ == '__main__':
    print("正在运行的脚本名称: '{}'".format(sys.argv[0]))
    print("脚本的参数数量: '{}'".format(len(sys.argv)))
    for arg in sys.argv:
        print(arg)