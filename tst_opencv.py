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


if __name__ == '__main__':
    print('hello world.')