import win32gui 
import win32con
import win32api
import time

def get_focus_window_text():
    pos = win32api.GetCursorPos()
    print('GetCursorPos: ', pos)
    
    hWnd = win32gui.WindowFromPoint(pos)
    print('WindowFromPoint: ', hWnd)

    length = win32gui .SendMessage(hWnd, win32con.WM_GETTEXTLENGTH) + 1
    print('Length: ', length)
    
    buf = win32gui.PyMakeBuffer(length)
    print('get: ', win32gui .SendMessage(hWnd, win32con.WM_GETTEXT, length, buf))

    address, result_length = win32gui.PyGetBufferAddressAndLen(buf)
    text = win32gui.PyGetString(address, result_length)
    print('text: ', text)

while True:
    get_focus_window_text()

    time.sleep(0.5)