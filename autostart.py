import winreg

# Добавить в автозагрузку
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0,
                     winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, 'Date Time', 0, winreg.REG_SZ, 'check_time.exe')
key.Close()

""" # Удалить из авто загрузки
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                     'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_ALL_ACCESS)
winreg.DeleteValue(key, 'Date Time')
key.Close()
"""
