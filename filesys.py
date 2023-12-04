import os

def list_dir(dir_path):
    if not os.path.exists(dir_path):
        print('dir not exists:', dir_path)
        return
    
    name_list = os.listdir(dir_path)
    for name in name_list:
        print(name)


if __name__ == '__main__':
    list_dir(r'Z:\00个人文件夹\季利伟-工作交接-2021.5\多波段')