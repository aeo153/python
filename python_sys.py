
import sys
# 环境变量:Path：D:\Program Files\Python\;D:\Program Files\Python\Scripts\
# install: pip install xxx
# uninstall: pip uninstall xxx
# list: pip list
# upgrade pip: python -m pip install --upgrade pip

if __name__ == '__main__':
    print("正在运行的脚本名称: '{}'".format(sys.argv[0]))
    print("脚本的参数数量: '{}'".format(len(sys.argv)))
    for arg in sys.argv:
        print(arg)