import sys
from unittest import result
import webbrowser
#abs 절댓값(백터에 대한 이해가 필요할 때 절대값으로 처리)
print(abs(-3))

#all, any : iterable 요소 검사 (참, 거짓)
print(all([1,2,3])) #all은 and 연산자 이다.
print(any([1,2,0])) #any는 or 연산자 이다.

print(all({1,2,3})) #all은 and 연산자 이다.
print(any({1,2,0})) #any는 or 연산자 이다.
#사용할 때는 검증할 때 사용한다. 

#아스키 chr : 아스키 -> 문자, ord : 문자 -> 아스키 
print(chr(67))
print(ord('c'))

#enumerator : 인덱스 + iterable 객체 생성

for i, name in enumerate(['abc','bcd','efg']): #enumerator는 for와 i, name과 필수이다.
    print(i, name)
c1 = ['abc','bcd','efg']
print(list(map(lambda x : x ,enumerate(c1))))
#map(function, iterable 자료형)
    
# 0 abc
# 1 bcd
# 2 efg
    
#max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))#아스키 코드 기준으로 y가 제일 크므로 y 출력
print(min([1,2,3]))
print(min('python study'))#아스키 코드 기준으로 " "가 제일 작으므로 " " 출력

#pow 제곱값 반환
print(pow(2,16))

print(list(range(pow(2,3))))
print(list(range(1,-15,-1)))

#round 반올림
print(round(6.5781))
print(round(6.51781))
print(round(6.51781,2))

#sorted : 반복가능한 객체(iterable) 정렬
print(sorted([6,5,4,1,3,2,2,6,7]))

#zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환 (각 객체의 요소를 하나씩 튜플로 묶고 리스트로 출력) return 값이 zip 이므로 list로 받았다.
print(list(zip([10,20,30],[40,30,60],range(10),"12334455")))
#[(10, 40, 0, '1'), (20, 30, 1, '2'), (30, 60, 2, '3')]
#새로운 자료형으로 만드는 것이다.

b = list(zip('abcdefg', range(3), range(4)))
print(b)

#sys
import sys
#print(sys.argv)#함수 이름

#['c:\\Users\\user\\python workspace\\20220410\\function2.py']

#print(sys.path)#파이썬 패키지 path 출력

# ['c:\\Users\\user\\python workspace\\20220410\\function2.py']
# ['c:\\Users\\user\\python workspace\\20220410', 'C:\\Users\\user\\.conda\\envs\\py39\\python39.zip', 
# 'C:\\Users\\user\\.conda\\envs\\py39\\DLLs', 'C:\\Users\\user\\.conda\\envs\\py39\\lib', 'C:\\Users\\user\\.conda\\envs\\py39', 
# 'C:\\Users\\user\\.conda\\envs\\py39\\lib\\site-packages', 'C:\\Users\\user\\.conda\\envs\\py39\\lib\\site-packages\\win32', 
# 'C:\\Users\\user\\.conda\\envs\\py39\\lib\\site-packages\\win32\\lib', 'C:\\Users\\user\\.conda\\envs\\py39\\lib\\site-packages\\Pythonwin']

import os
print(os.environ)#환경변수 다음과 같이 DICTIONARY로 출력 된다.
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\user\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': 
# '\\\\.\\pipe\\crashpad_21276_CIJXWLRFIJUYRLXI', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 
# 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LAPTOP-ETAKVJJP', 
# 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 
# 'HOMEPATH': '\\Users\\user', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-18', 'LOCALAPPDATA': 'C:\\Users\\user\\AppData\\Local', 
# 'LOGONSERVER': '\\\\LAPTOP-ETAKVJJP', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\user\\OneDrive', 
# 'ONEDRIVECONSUMER': 'C:\\Users\\user\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 
# 'PATH': 'C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\dotnet\\;C:\\Program Files\\Bandizip\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\Java\\jdk-18\\bin\\;C:\\Users\\user\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\user\\.dotnet\\tools;C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\user\\AppData\\Local\\atom\\bin;C:\\Users\\user\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 140 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8c01', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\user\\OneDrive\\문서\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\user\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\user\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-ETAKVJJP', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-ETAKVJJP', 'USERNAME': 'user', 'USERPROFILE': 'C:\\Users\\user', 'WINDIR': 'C:\\Windows', 'ZES_ENABLE_SYSMAN': '1', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.66.1', 'LANG': 'ko_KR.UTF-8', 'COLORTERM': 'truecolor', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-9707f5bf03-sock', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'GIT_ASKPASS': 'c:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONUNBUFFERED': '1', 'PYDEVD_USE_FRAME_EVAL': 'NO'})
print(os.environ['USERNAME'])
#결과 > user
print(os.getcwd())
#결과 > C:\Users\user\python workspace

import time

print(time.time())
#결과 > 1649554145.2732928
print(time.localtime(time.time()))
#결과 > time.struct_time(tm_year=2022, tm_mon=4, tm_mday=10, tm_hour=10, tm_min=30, tm_sec=23, tm_wday=6, tm_yday=100, tm_isdst=0)

print(time.ctime())
#결과 > Sun Apr 10 10:30:23 2022

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#결과 > 2022-04-10 10:33:05

import random

print(random.random())
print(random.randint(1,45))
d = [1,2,3,4,5]
random.shuffle(d)
print(d)


c = random.choice(d)
print(c)

# webbrowser.open("https://google.com")
# webbrowser.open_new("https://google.com")
# webbrowser.open_new_tab("https://google.com")

import pickle
#pickle 객체 파일 쓰기 pickle이라는 객체를 이용해서 읽기 쓰기가 가능한다.

f = open("test.txt","wb")
obj = {1:'python', 2:'study',3:'basic'}
pickle.dump(obj,f)
f.close()

f = open("test.txt", "rb")
data = pickle.load(f)
print(data)
f.close()








