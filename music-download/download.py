import os
import requests
# Create the output folder
os.makedirs('./output/', exist_ok=True)


chaper_url = 'https://m701.music.126.net/20191129103913/e519c17370d375e782bd2a461adeda6b/jdyyaac/010c/0558/0453/6f576f14fe22c846586339a48b9ed65a.m4a'

def getMusix():
    session = requests.Session()
    session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
    session.get('https://m7.music.126.net')
    r = session.get(chaper_url)
    with open('./output/image3.m4a', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

def getName():
    session = requests.Session()
    session.headers = {
            'cookie': '_iuqxldmzr_=32; _ntes_nnid=faa99add6872dc827d0a984746a67c70,1572838516186; _ntes_nuid=faa99add6872dc827d0a984746a67c70; WM_TID=PX8LkGm3N4FFAEUQFBd8uA41O88ctx%2B4; mail_psc_fingerprint=de75917b3096c35d9c8ee269fc1e0b74; ntes_kaola_ad=1; P_INFO=a20160403@126.com|1573195438|1|mail126|00&99|hongkong&1572918303&mail126#hongkong&810000#10#0#0|&0|mail126|a20160403@126.com; WM_NI=x%2Ba5%2Fi0twGPpyZ%2BfCDxjhv93%2Bi7jvuhGaiE5RM9nWWGuNdB9ONNxDxogxa1p9sSEynB8cf2a%2BkM4lr3iQn9BJ83TwbQV7npPCnKelTuhEOfIJr9PgaIJWez4MAlLXdLgcUM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea7d02583b5aaaef925edb88aa7c15a829e8eaaee7e8bb0a88bf647a38c978ffb2af0fea7c3b92abcf5afd6ae63f4acb9a8d37cbb86e587c250bcb6a897bc39e9b7f98bf57fac99af8ac83f9293f78fd65d85ab8285c1338d928299c774adb9b882b47cfbad9da6fc6682e8ad87b16be9b583d5ef7af1b79f8fbc4a8ae8fdb5f66a938af98ff35c81b28586ef60b7b88bb0e5438aaef7b1e66b8b969986f9408f9fa4addb7090b9adb6d037e2a3; playerid=61320530; JSESSIONID-WYYY=diHqIdu%2BpguQkqCZ%2BjbUciStk%2BKBCo6M6%2F7%2Fm8y0umk6HaiXtR5Boe%2Fei8QaN%2Fev2qJFyoQ%2Bgyb1BV3SBtsRmNeEHoXgjP4eqZRfaRWIeNnCJIq9d5SJHgaJVFpspwmPC3HAdmxQQjpF5eTfNIlHt3P%2BEllTdjjJSz2Er5Jk3SBBxoOm%3A1574996559987; MUSIC_U=f1fbb405b1c47161508e17c4c971acc4488eef5137ac28457a6d6add001eade644a001edbc79a233c2ea4ce0a9a3ae247955a739ab43dce1; __remember_me=true; __csrf=d22e36da94daa1cc766bdfde0e35cfdc',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
    
    session.get('https://music.163.com')
    r = session.get('https://music.163.com/#/song?id=360311')
    with open('./output/image3.html', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

getName()