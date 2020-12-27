import ctypes
import win32con
import win32gui
import time
import random
import math
import sys
from array import array

hwnd = win32gui.FindWindow("TMainFrm", "运动控制助手")
if hwnd == 0 :
    print("failed to find window.")
    sys.exit(1)

h1 = win32gui.FindWindowEx(hwnd, 0, "TPageControl", "")
#print(h1)
h2 = win32gui.FindWindowEx(h1, 0, "TTabSheet", "Sheet_Manual")
#print(h2)
h3 = win32gui.FindWindowEx(h2, 0, "TScrollBox", "")
#print(h3)
h4 = win32gui.FindWindowEx(h3, 0, "TAxisFrm", "")
#print(h4)
hwndChildList = []
win32gui.EnumChildWindows(h3, lambda hwnd, param: param.append(hwnd),  hwndChildList)
if len(hwndChildList) == 0 :
    print("empty child window")
    sys.exit(1)

def GetWinValue(h_win):
    length = win32gui .SendMessage(h_win, win32con.WM_GETTEXTLENGTH) + 1
    # print('Length: ', length)
    
    buf = win32gui.PyMakeBuffer(length)
    win32gui .SendMessage(h_win, win32con.WM_GETTEXT, length, buf)

    address, result_length = win32gui.PyGetBufferAddressAndLen(buf)
    text = win32gui.PyGetString(address, result_length)
    return text[:-1]

def GetAxisValue(parent_win) :

    hh1 = win32gui.FindWindowEx(parent_win, 0, "TGroupBox", None)
    #print(hh1, win32gui.GetClassName(hh1))
    hh2 = win32gui.FindWindowEx(hh1, 0, "TGroupBox", "状态")
    #print(hh2, win32gui.GetClassName(hh2))

    win_list = []
    win32gui.EnumChildWindows(hh2, lambda hwnd, param: param.append(hwnd),  win_list)
    #print(win_list[3], win32gui.GetClassName(win_list[3]))
    return GetWinValue(win_list[3])

pnts = []
for hw in hwndChildList :
    if win32gui.GetClassName(hw) == "TAxisFrm" :
        # print(hw)
        strval = GetAxisValue(hw)
        # print(strval)
        pnts.append(float(strval))

dist = math.sqrt(pnts[0]*pnts[0] + pnts[1]*pnts[1] + pnts[2]*pnts[2])
print("dist = %.2f" % dist)
pntstr = time.strftime("%Y%m%d:%H:%M:%S", time.localtime())
pntstr += "\t" + str(pnts[2])
pntstr += "\t" + str(pnts[1])
pntstr += "\t" + str(pnts[0])
pntstr += "\t" + str(round(dist,3))+"\n"
print(pntstr)
pf = open("D:/dsyx_doc/surgery_nav/testdata/huatai_dists.txt", "a+")
pf.write(pntstr)
pf.flush()
pf.close()

