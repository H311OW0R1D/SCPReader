import getpass
import random
import webbrowser
print('Welcome to your terminal. Please enter your username and password.')
usr=input('Username: ')
pa=getpass.getpass()
print('Login succesful. Welcome, '+usr)
print("""\
.------------------------------------------------------------------------------------------.
|                                                         ,#############,                  |
|  ____                                                   ##           ##                  |
| / ___|  ___  ___ _   _ _ __ ___                     m####             ####m              |
| \___ \ / _ \/ __| | | | '__/ _ \                 m##*'        mmm        '*##m           |
|  ___) |  __/ (__| |_| | | |  __/_              ###'         mm###mm         '###         |
| |____/ \___|\___|\__,_|_|  \___(_)           ###        m#############m        ###       |
|                                             ##       m####*'  ###  '*####        ##      |
|                                            ##      m####      ###      ####m      ##     |
|   ____            _        _              ##      ####      #######      ####      ##    |
|  / ___|___  _ __ | |_ __ _(_)_ __        m#      ###'        #####        '###      #m   |
| | |   / _ \| '_ \| __/ _` | | '_ \       ##     ####           #           ####     ##   |
| | |__| (_) | | | | || (_| | | | | |_     ##     ###    wwwwwwww wwwwwwww    ###     ##   |
|  \____\___/|_| |_|\__\__,_|_|_| |_(_)    ##     ###m    ######   ######    m###     ##   |
|                                        ,###     '### m#######     #######m ###'     ###, |
|                                        ##'      m######'   *       *   '######m      '## |
|  ____            _            _         ##     *#*'######             ######'*#*     ##  |
| |  _ \ _ __ ___ | |_ ___  ___| |_        ##         '#######m     m#######'         ##   |
| | |_) | '__/ _ \| __/ _ \/ __| __|        *#m          '###############'          m#*    |
| |  __/| | | (_) | ||  __/ (__| |_ _         ##m ,m,        ''*****''        ,m, m##      |
| |_|   |_|  \___/ \__\___|\___|\__(_)         *##'*###m                   m###*'##*       |
|                                                    '*#######m     m#######*'             |
|                                                           '*#######*'                    |
'------------------------------------------------------------------------------------------'
""")
ttd=input('Press RR to generate an SCP file, SS to search, CC to check a file and EE to exit. ')
if ttd=='RR':
    STR=random.randint(1,5999)
    if STR<100:
        link="http://scp-wiki.wikidot.com/scp-00"+str(STR)
    else:
        link="http://scp-wiki.wikidot.com/scp-"+str(STR)
    webbrowser.open(link)
if ttd=='EE':
    exit()
if ttd=='SS':
    tts=input('Search term: ')
    link="http://www.scpwiki.com/search:site/q/"+tts
    webbrowser.open(link)
if ttd=='CC':
    tts=input('File to check: ')
    link="http://scp-wiki.wikidot.com/scp-"+tts
    webbrowser.open(link)
