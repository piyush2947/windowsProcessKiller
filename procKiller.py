import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")
u_handle = ctypes.WinDLL("User32.dll")

PROCESS_ALL_ACCESS = ( 0x0000F0000 | 0x00100000 | 0xFFF)

#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindowa
lpWindowName = ctypes.c_char_p(input("Enter Window Name To Kill: ").encode('utf-8'))

print(lpWindowName)




hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    print("Error Code: {0} - Could Not grab Handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got Handle..")


#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid


lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
    print("Error Code: {0} - Could Not grab PID".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got the PID!")






dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if hProcess <= 0:
    print("Error Code: {0} - Could Not grab Priv Handle".format(k_handle.GetLastError()))
else:
    print("Got our Handle...")




uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)


if response <= 0:
    print("Error Code: {0} - Could Not terminate process".format(k_handle.GetLastError()))
else:
    print("process went bye bye")
