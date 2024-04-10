import os
import shutil as fop

def list_dir(dir_path):
    if not os.path.exists(dir_path):
        print('dir not exists:', dir_path)
        return
    
    name_list = os.listdir(dir_path)
    for name in name_list:
        print(name)

def copy_dir(src_dir, dst_dir):

    if not os.path.exists(src_dir):
        print('dir not exists:', src_dir)
        return
    
    # if not os.path.exists(dst_dir):
    #     os.mkdir(dst_dir)
    
    fop.copytree(src_dir, dst_dir)

if __name__ == '__main__':
    list_dir(r'd:/temp/test_dcm_double_ten/')
    # copy_dir(r'D:\temp\led_dicom', r'D:\cpdst')