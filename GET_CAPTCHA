import urllib.request    
from urllib.error import URLError
import time
from retry import retry

@retry(tries=50, delay=2)
def getcap():
        CaptchaUrl = "http://202.118.201.228/academic/getCaptcha.do"
        f1 = open('cap.txt', 'r', encoding='utf-8')
        x = int(f1.read())
        while(x<=250000):
                if (x % 10) == 0:
                        time.sleep(2)                        
                urllib.request.urlretrieve(CaptchaUrl,'C:\\Users\\Gaz\\Desktop\\Captcha\\%s.jpg' % x)
                time.sleep(0.3)
                print(x)
                x+=1
                with open("cap.txt","w") as f2:
                        f2.write("%s" %x)
                        

getcap()
