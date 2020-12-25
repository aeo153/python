from ctypes import *
import time

MT_API = windll.LoadLibrary(r"D:\tools\MTGroup\MT_API.dll")
MT_API.MT_Open_UART.argtypes = [c_wchar_p]
MT_API.MT_Init()
MT_API.MT_Open_USB()
iR = MT_API.MT_Check()
print("iR=", iR)
iPos = c_int32(0)
pPos = pointer(iPos)
MT_API.MT_Get_Axis_Software_P_Now(0, pPos)
print("iPos=", iPos)
d = iPos / c_long(6400)
print(d)