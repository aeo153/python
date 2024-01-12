import cv2 as cv
import os
# rt = cv2.cvRect(0,1,10,10)
# rct = [20, 40, 100, 100]
# print(rct)
# rct += [10, 10]
# print(rct)

def resize_dir_imgs(src_dir, nw, nh, dst_dir):
    if not os.path.exists(src_dir):
        print("src_dir not exists:", src_dir)
        return
    
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    src_list = os.listdir(src_dir)
    for fnm in src_list:
        src_img = cv.imread(src_dir+fnm)
        dst_img = cv.resize(src_img, (nw, nh))
        cv.imwrite(dst_dir + fnm, dst_img)

def roi_dir_imgs(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        print("src_dir not exists:", src_dir)
        return
    
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    
    src_list = os.listdir(src_dir)
    for fnm in src_list:
        src_img = cv.imread(src_dir+fnm)
        dst_img = src_img[0:686, 0:863] #[r0:r1, c0:c1], [h0:h1,w0:w1]
        cv.imwrite(dst_dir+fnm, dst_img)

def cvt_dir(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        print("src_dir not exists:", src_dir)
        return
    
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    
    src_list = os.listdir(src_dir)
    for fnm in src_list:
        src_img = cv.imread(src_dir+fnm)
        dst_img = cv.cvtColor(src_img, code=cv.COLOR_RGB2BGR)
        cv.imwrite(dst_dir+fnm, dst_img)

def video2imgs(video_path, dst_dir):
    if not os.path.exists(video_path):
        print("video_path not exists:", video_path)
        return
    
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    vcap = cv.VideoCapture(video_path)
    if not vcap.isOpened():
        print("failed to open:", video_path)
        return

    idx = 0
    while(True):
        ret, img = vcap.read()
        print(idx)
        if not ret:
            break

        dst_path = str('%s%.5d.png'%(dst_dir, idx))
        idx += 1
        cv.imwrite(dst_path, img)

    print('video2imgs done')

def writemyl(fpth):
    #写文件
    model_settings=cv.FileStorage(fpth,cv.FILE_STORAGE_WRITE)
    model_settings.write('version','v1.0')
    model_settings.write('author','gloomyfish')
    model_settings.write('rows',21.0)
    model_settings.write('cols',22.1)
    model_settings.write('param3','p3str')
    model_settings.release()

def loadyml(fpth):

    if not os.path.exists(fpth):
        return
    
    # 打开YML文件
    fst = cv.FileStorage(fpth, cv.FileStorage_READ)
    print(fst.isOpened())
    print(fst.getFormat())
    print(fst.getFirstTopLevelNode())
    
    # print(fst.getNode('version'))
    # print(fst.getNode('param1').real())
    # print(fst.getNode('param2').real())
    # print(fst.getNode('param3').string())
    
    # 从YML文件中提取图像数据
    r = fst.getNode('rows').real()
    c = fst.getNode('cols').real()
    # img = fst.getNode('data').mat()
    
    print(r, c)
    
    # 关闭YML文件
    fst.release()

    # cv.imshow('yml', img)


if __name__ == '__main__':
    # print('hello world.')
    fpth = r'D:\dobi\doc\disn\tst.yml'
    writemyl(fpth)
    loadyml(fpth)