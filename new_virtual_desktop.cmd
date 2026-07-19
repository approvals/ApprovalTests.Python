@echo off
REM Creates a new Windows virtual desktop by simulating the Win+Ctrl+D shortcut.
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$sig = '[DllImport(\"user32.dll\")]public static extern void keybd_event(byte bVk, byte bScan, int dwFlags, int dwExtraInfo);';" ^
    "$win32 = Add-Type -MemberDefinition $sig -Name Win32 -Namespace WinAPI -PassThru;" ^
    "$VK_LWIN = 0x5B; $VK_CONTROL = 0x11; $VK_D = 0x44; $KEYEVENTF_KEYUP = 0x2;" ^
    "$win32::keybd_event($VK_LWIN, 0, 0, 0);" ^
    "$win32::keybd_event($VK_CONTROL, 0, 0, 0);" ^
    "$win32::keybd_event($VK_D, 0, 0, 0);" ^
    "Start-Sleep -Milliseconds 50;" ^
    "$win32::keybd_event($VK_D, 0, $KEYEVENTF_KEYUP, 0);" ^
    "$win32::keybd_event($VK_CONTROL, 0, $KEYEVENTF_KEYUP, 0);" ^
    "$win32::keybd_event($VK_LWIN, 0, $KEYEVENTF_KEYUP, 0);"
