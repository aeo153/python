
x_axis = win32gui.FindWindowEx(hwnd, 71174986, "TEdit", "")
print(x_axis)
length = win32gui .SendMessage(x_axis, win32con.WM_GETTEXTLENGTH) + 1
print('Length: ', length)
buf = win32gui.PyMakeBuffer(length)
print('get: ', win32gui .SendMessage(x_axis, win32con.WM_GETTEXT, length, buf))

address, result_length = win32gui.PyGetBufferAddressAndLen(buf)
text = win32gui.PyGetString(address, result_length)
print('text: ', text)

# buf_size = win32gui.SendMessage(x_axis, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节
# print(buf_size)
# str_buffer = win32gui.PyMakeBuffer(buf_size)  # 生成buffer对象
# win32gui.SendMessage(x_axis, win32con.WM_GETTEXT, buf_size, str_buffer)  # 获取buffer
# str = str(str_buffer[:-1])  # 转为字符串
# print(float(str))

# buffer_len = win32gui.SendMessage(x_axis, win32con.WM_GETTEXTLENGTH, 0, 0) + 1
# print(buffer_len)
# text = array('b', b'\x00\x00' * buffer_len)
# text_len = win32gui.SendMessage(x_axis, win32con.WM_GETTEXT, buffer_len, text)
# print(text_len)
# print(text)

# buffer = '0' *64
# len = win32gui.SendMessage(x_axis, win32con.WM_GETTEXTLENGTH, 0, 0)+1
# print(len)
# win32gui.SendMessage(x_axis, win32con.WM_GETTEXT, 64, buffer)
# print(buffer)

# buff =ctypes.create_unicode_buffer(64)
# win32gui.SendMessage(x_axis, win32con.WM_GETTEXT, 32, buff)
# print (buff.value)

# get time
import time
print (time.strftime("%Y-%m-%d:%H:%M:%S", time.localtime()))

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print (time.strftime("%Y%m%d:%H:%M:%S", time.localtime()))
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-"))+"".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)

get_time_stamp()