import ctypes

ntdll=ctypes.windll.ntdll
SetShutdownPrivilege = 19

def GetNtError(err):
    return ntdll.RtlNtStatusToDosError(err)

def BSOD(stop_code):
    enabled = ctypes.c_bool()
    res = ntdll.RtlNtStatusToDosError(SetShutdownPrivilege,True,False,ctypes.pointer(enabled))

    if not res:
        print("Privileges adjusted succcesfully!")
    else:
        print("Privilages could not be adjusted!")
        raise ctypes.WinError(GetNtError(res))
    
    respone = ctypes.c_ulong()
    res = ntdll.NtRaiseHardError(stop_code,0,0,0,6, ctypes.byref(respone))

    if not res:
        print("Bluescreen successful, and somehow you are reading this x)")
    else:
        print("Bluescreen failed")
        raise ctypes.WinError(GetNtError(res))