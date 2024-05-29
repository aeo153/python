import cv2 as cv
import os
import numpy as np
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
    r = fst.getNode('rows')
    c = fst.getNode('cols')
    img = fst.getNode('data')
    nt = fst.getNode('nt')
    
    print(r, c, img, nt)
    
    # 关闭YML文件
    fst.release()

    # cv.imshow('yml', img)

def tst_norm():
    mat1 = np.array([[1, 2, 3], [4, 5, 6]])
    mat2 = np.array([[0, 0, 0], [0, 0, 0]])
    print(mat1)
    print(mat2)
    print(cv.norm(mat1, mat2, cv.NORM_L2))

def tst_rotate():
    theta = np.pi / 4
    rvec = np.array([[theta, theta, theta]])
    print(rvec.shape)
    rmat, _ = cv.Rodrigues(rvec)
    print(rmat)

if __name__ == '__main__':
    tst_rotate()