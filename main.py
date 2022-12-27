import requests 
from random import choice 
from bs4 import BeautifulSoup 
import codecs
import base64
O00OO00000OOOO00=codecs.decode("nygnqrsvavmvbar", "rot13")
O0000OOOOO0000O0=codecs.decode("pbzzhavgl", "rot13")
class OOO0O0O00O0O00O00 ():
    def __init__ (O000000000O0OOOO0 ,O0OOOOOOOOOOOO000 ):
        O000000000O0OOOO0 .token =O0OOOOOOOOOOOO000 
        O000000000O0OOOO0 .headers :dict ={'Authorization':f'Bearer {O000000000O0OOOO0.token}',}
class O0OO0OO00OOOOO0O0 :
    def __init__ (O0OO0000000O000O0 ):
        O0OO0000000O000O0 .updated_domain =O0OO0000000O000O0 .new_domain ()
    def new_domain (O00O0000OOOO0OO0O ):
        OOOO0O0000OO00O0O =requests .get (f'https://{O00OO00000OOOO00}-nuovo.click/').content 
        O00OO0O0OO0O0OO00 =BeautifulSoup (OOOO0O0000OO00O0O ,'html.parser')
        OOOO0O00O0O000O0O =O00OO0O0OO0O0OO00 .select ('h2 > a')[0 ].text .split ('.')[-1 ]
        return OOOO0O00O0O000O0O 
    def O0OOO0O0OOOOO00O0 (OOOO000OOO0OOOOOO ):
        OO00OOOOO0O0OOO00 =''.join ([choice ('abcdefghijklmnopqrstuvwxyz0123456789%')for _O00000OO00O0O0O00 in range (10 )])
        return f"{OO00OOOOO0O0OOO00}@{''.join([choice('abcdefghijklmnopqrstuvwxyz') for _O00OOOO0O00O0O00O in range(4)])}.{''.join([choice('abcdefghijklmnopqrstuvwxyz') for _O0OO000OO0000OO00 in range(2)])}"
    def O0OO0OOO0OO0O00OO (O0OO0OOOOOOOO000O ,OO0OOO0O000OO00O0 ,O0O000O00OOO00OO0 ,O00OOO0OOO00O0O0O ):
        requests .get (f'https://{O00OO00000OOOO00}{O0000OOOOO0000O0}.{O0OO0OOOOOOOO000O.updated_domain}/api/verify/email/{OO0OOO0O000OO00O0}/{O0O000O00OOO00OO0}',headers =OOO0O0O00O0O00O00 (O00OOO0OOO00O0O0O ).headers )
    def OOOO0O0O000OOO000 (O00O00000000O00O0 ):
        O0OO00OO00O0OO0O0 =''.join ([choice ('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)')for _O0O00000O000000OO in range (10 )])
        O00O000O000OO00O0 =O00O00000000O00O0 .O0OOO0O0OOOOO00O0 ()
        OOO0O0OO00OOOOO0O =requests .post (f'https://{O00OO00000OOOO00}{O0000OOOOO0000O0}.{O00O00000000O00O0.updated_domain}/api/register',json ={"email":O00O000O000OO00O0 ,"password":O0OO00OO00O0OO0O0 ,"password_confirmation":O0OO00OO00O0OO0O0 ,"fingerprint":1117459144040421 ,"selected_plan":1 }).json ()
        try :
            return {'token':OOO0O0OO00OOOOO0O ['token'],'email':O00O000O000OO00O0 ,'ver_code':OOO0O0OO00OOOOO0O ['user']['verification_code'],'id':OOO0O0OO00OOOOO0O ['user']['id'],'password':O0OO00OO00O0OO0O0 }
        except Exception:
            pass
    def OO0O0O00OO0O0O0O0 (OOO0O0OO00OOOO0O0 ):
        O0O000OOOOO0OOO0O =OOO0O0OO00OOOO0O0 .OOOO0O0O000OOO000 ()
        OOO0O0OO00OOOO0O0 .O0OO0OOO0OO0O00OO (O0O000OOOOO0OOO0O ['id'],O0O000OOOOO0OOO0O ['ver_code'],O0O000OOOOO0OOO0O ['token'])
        return O0O000OOOOO0OOO0O ['token']
if __name__ =='__main__':
    OOO00OOO0O0O0OOOO =O0OO0OO00OOOOO0O0()
    O0OOOOOOOOO0O0000 =OOO00OOO0O0O0OOOO.OO0O0O00OO0O0O0O0()
    with open ("O0O0000000000O0O0.txt",'w',encoding ='utf-8')as OOO00OO0O0OOO00O0:
        OOO00OO0O0OOO00O0.write (base64.b64encode(bytes(O0OOOOOOOOO0O0000, 'utf-8')).decode("utf-8"))
