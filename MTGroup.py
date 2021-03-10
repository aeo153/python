from ctypes import *
import time
import sys
import math

MT_API = windll.LoadLibrary(r"D:/dsyx_doc/huatai/WIN64/MT_API.dll")
MT_API.MT_Open_UART.argtypes = [c_wchar_p]
res = MT_API.MT_Init()
print("init result:", res)
res = MT_API.MT_Open_USB()
print("open result:", res)
res = MT_API.MT_Check()
print("check result:", res)
if res != 0 :
    print("failed to oepn MT.")
    sys.exit()

def GetAxisPosition( axisId ) :
    curSteps = c_int32(5)
    pSteps = pointer(curSteps)
    MT_API.MT_Get_Axis_Software_P_Now(axisId, pSteps)
    MT_API.MT_Help_Step_Line_Steps_To_Real.restype = c_double
    retVal = MT_API.MT_Help_Step_Line_Steps_To_Real(c_double(1.8), 32, c_double(0.5), c_double(1.0), curSteps)
    return retVal

x = GetAxisPosition(0)
y = GetAxisPosition(1)
z = GetAxisPosition(2)

dist = math.sqrt(x*x + y*y + z*z)
pntstr = time.strftime("%Y%m%d:%H:%M:%S", time.localtime())
pntstr += "\t" + str(x)
pntstr += "\t" + str(y)
pntstr += "\t" + str(z)
pntstr += "\t" + str(round(dist,3))+"\n"
print(pntstr)
print("dist = %.2f" % dist)
pf = open("D:/dsyx_doc/surgery_nav/testdata/huatai_test.txt", "a+")
pf.write(pntstr)
pf.flush()
pf.close()

def InitAxis( axisId ):
    MT_API.MT_Set_Axis_Mode_Position_Open(axisId)
    MT_API.MT_Set_Axis_Position_V_Start(axisId, c_int32(8000))
    MT_API.MT_Set_Axis_Position_Acc(axisId, c_int32(2000))
    MT_API.MT_Set_Axis_Position_Dec(axisId, c_int32(2000))
    MT_API.MT_Set_Axis_Position_V_Max(axisId, c_int32(12000))

def SetAxisPosition( axisId, posVal ):
    InitAxis(axisId)
    MT_API.MT_Help_Step_Line_Real_To_Steps.restype = c_int32
    steps = MT_API.MT_Help_Step_Line_Real_To_Steps(c_double(1.8), 32, c_double(0.5), c_double(1.0), posVal)
    curSteps = c_int32(0)
    pCurSteps = pointer(curSteps)
    MT_API.MT_Get_Axis_Software_P_Now(axisId, pCurSteps)
    if curSteps == c_int32(steps) :
        print("steps equal.")
        return
    
    print("start move:", axisId)
    MT_API.MT_Set_Axis_Position_P_Target_Abs(axisId, steps)

SetAxisPosition(0, c_double(0.0))
time.sleep(2)
SetAxisPosition(1, c_double(0.0))
time.sleep(2)
SetAxisPosition(2, c_double(0.0))
time.sleep(2)

MT_API.MT_Close_USB()
MT_API.MT_DeInit()