import pyAesCrypt
import os
from getpass import getpass
from faker import Faker
import time
import socket
import random
from pyfiglet import Figlet
import requests
import termcolor

time.sleep(0)
os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана



while True:
    print("⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿")
    print("⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿")
    print("⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿")
    print("⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿")
    print("⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿")
    print("⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿")
    print("⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿")
    print("⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿")
    print("⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿")
    print("⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿")
    print("⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿")
    print("⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿")
    print("⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿")
    print("⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿")
    print("⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿")
    print("⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿")
    print("⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛")
    print("⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀")
    print("⠀⠀ ⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀")
    print("⠀⠀ ⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀")
    print("")


    print(" 1 - фейковые данные\n",
        "2 - шифратор деректорий\n",
        "3 - IP-адрес сайта\n"
        " 4 - местоположение по IP\n"
        " 5 - генератор пароля"
        )
    print("")
    resh = input(termcolor.colored(("[*] Введите цифру: "), 'green'))

    time.sleep(0)
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана

    if resh == '1':
        a = input(termcolor.colored(("[*] Введите RU для получение данных для росии "), 'green'))
        print("")
        
        faker = Faker(a)

        name = faker.name()
        address = faker.address()
        email = faker.email()
        job = faker.job()
        num = faker.phone_number()
        print(f'ФИО: {name}\nАдрес: {address}\nПочта: {email}\nПрофессия: {job}\nНомер телефона: {num}')
        print("")
    elif resh == '2':
        a = input(termcolor.colored(("[*] Введите sh/de "), 'green'))

        if a == "sh":
        #функция шифрования
            def encryption(file, password):
            #задаем размер буфера
                buffer_size = 512 * 1024

            #вызываем метод шифрования
                pyAesCrypt.encryptFile(
                    str(file),
                    str(file) + ".crp",
                    password,
                    buffer_size
                )

            #вывод собшениее о удачном шифровании 
                print("[файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

            #удаление исходного файла
                os.remove(file)

        #функция для сканирования деректории
            def walking_by_dirs(dir, password):
                #подбор всех подиректорий в указаной директории
                    for name in os.listdir(dir):
                        path = os.path.join(dir, name)

                    #если находит файл, то шифруем его
                        if os.path.isfile(path):
                            try:
                                encryption(path, password)
                            except Exception as ex:
                                print(ex)
                        #если находит директорию, то повторяет цикл в поисках файлов
                        else:
                            walking_by_dirs(path, password)


            def lol(lol):
                print("⣸⠒⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⡇⠀⠀⠀⠑⠄⡀⠀⠀⠀⣀⠀⠀⠀")
                print("⠃⠀⠀⠀⠀⠀⢈⣵⣦⢸⣿⡧⠀⠀")
                print("     ⠀⠀⣼⣿⣿⣾⢏⠀⠀⠀")
                print("   ⠀⠀⢿⣼⣿⢟⣷⣷⣆⠀ ")
                print("  ⠀⠀⠀⣾⣿⣿⣿⣿⡿⠈⢆ ")
                print("     ⢰⢸⣿⣿⣿⣿⠇⠀⠈")
                print("  ⠀⠀⠀⢸⢸⣿⣿⣿⡇⠀⠀⠀")
                print(" ⠀⠀⠀⠀⡈⣼⣿⣿⣿⡇⠀⠀⠀")
                print("      ⣿⣿⣿⣿⣿⡇⠀⠀⠀")
                print("   ⠀⠀⣸⣿⣿⣿⣿⣿⣿⠀⠀⠀")
                print("   ⠀⠾⢿⣿⣿⠿⠿⣿⡿⠀⠀⠀")


            lol(print())

        

            pyt = input(termcolor.colored(("[*] Введите путь: "), 'green'))
            walking_by_dirs(pyt, password)
            print("")
        
                


        elif a == "de":
            #функция дешифрования
            def decryption(file, password):
            #задаем размер буфера
                buffer_size = 512 * 1024

                #вызываем метод дешифрования
                pyAesCrypt.decryptFile(
                    str(file),
                    str(os.path.splitext(file)[0]),
                    password,
                    buffer_size
                )

            #вывод собшениее о удачном дешифровании 
                print("[файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

            #удаление исходного файла
                os.remove(file)

        #функция для сканирования деректории
            def walking_by_dirs(dir, password):
                #подбор всех подиректорий в указаной директории
                    for name in os.listdir(dir):
                        path = os.path.join(dir, name)

                    #если находит файл, то дешифруем его
                        if os.path.isfile(path):
                            try:
                                decryption(path, password)
                            except Exception as ex:
                                print(ex)
                    #если находит директорию, то повторяет цикл в поисках файлов
                        else:
                            walking_by_dirs(path, password)


            def lol(lol):
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣛⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⡝⢛⠛⣩⣿⣿⣿⡟⠙⣿⣿⣿⣿⣿")
                print("⣿⡿⢿⠄⢣⠄⢸⣿⣿⡟⣱⠞⢳⡜⣿⣿⣿⠇⠄⠏⢀⡿⢿⣿")
                print("⣿⣇⠈⠄⠄⠄⠄⢿⣿⡇⣿⡀⣸⡇⢻⣿⠿⠇⠄⠏⢀⡿⢿⣿")
                print("⣿⡈⠓⠄⠄⠄⠂⢀⣸⡗⠙⢯⠽⠋⡺⣅⠄⠄⠄⠊⠄⠊⢀⣿")
                print("⣿⡉⠁⠄⠌⠄⠄⢰⠁⢘⠓⠚⠃⠺⡁⠙⡂⠄⠄⠠⠄⠈⢉⣿")
                print("⣿⣿⣅⣀⠄⠔⣀⡇⠄⢸⠄⠄⠄⠄⡅⠄⢡⠐⠄⢀⣀⣩⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⣻⡞⣴⠚⠄⢀⣮⣿⣽⣾⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⡬⠝⢿⡀⣠⢿⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⢋⠃⠁⢀⡔⠋⢠⢳⠘⣿⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⡏⠈⠶⠞⠋⠄⣰⣿⠐⠇⠹⣿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣧⣀⣀⡀⣴⡞⠄⣿⡄⢩⡄⢿⣿⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⡿⢡⠋⠉⠁⡙⠁⠄⢠⢡⠄⢣⠈⠻⣿⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⡟⣠⠏⠄⠄⢀⣷⠄⠄⠸⠸⠆⠄⣧⠄⠹⣿⣿⣿⣿")
                print("⣿⣿⣿⡋⣰⠃⠄⠄⠄⡜⡝⠄⠄⠄⡇⢻⡀⠘⣧⠄⢘⣿⣿⣿")
                print("⣿⣿⣿⣿⠁⠄⠄⠄⣰⢧⠃⠄⠄⠄⢸⠈⡅⠄⠘⣦⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣷⣶⣶⣴⣿⡜⠄⠄⠄⠄⢰⣇⣸⣀⣀⣼⣿⣿⣿⣿")
                print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")

            lol(print())


            
            pyt = input(termcolor.colored(("[*] Введите путь: "), 'green'))
            walking_by_dirs(pyt, password)
            print("")



    elif resh == '3':
        def get_ip_by_hostname():
            hostname = input(termcolor.colored(('[*] Введите домен: '), 'green'))
            
            try:
                return f'IP address: {socket.gethostbyname(hostname)}'
            except socket.gaierror as error:
                return f'Invalid Hostname - {error}'


        def main():
            print(get_ip_by_hostname())
            print("")
            
            
        if __name__ == '__main__':
            main()

    elif resh == '4':
        def get_info_by_ip(ip='127.0.0.1'):
            try:
                response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                
                data = {
                    '[IP]': response.get('query'),
                    '[Int prov]': response.get('isp'),
                    '[Org]': response.get('org'),
                    '[Country]': response.get('country'),
                    '[Region Name]': response.get('regionName'),
                    '[City]': response.get('city'),
                    '[ZIP]': response.get('zip'),
                    '[Lat]': response.get('lat'),
                    '[Lon]': response.get('lon'),
                }
                
                for k, v in data.items():
                    print(f'{k} : {v}')
                
            except requests.exceptions.ConnectionError:
                print(termcolor.colored(('[!] Пожалуйста, проверьте подключение!'), 'red'))
                
                
        def main():
            preview_text = Figlet(font='slant')
            print(preview_text.renderText('IP INFO'))
            ip = input(termcolor.colored(('[*] Введите целевой IP-адрес: '), 'green'))
            
            get_info_by_ip(ip=ip)
            
            
        if __name__ == '__main__':
            main()

        print("")
    elif resh == '5':
        preview_text = Figlet(font='slant') #задаем шрифт
        print(preview_text.renderText('Password generator'))

        vvod = int(input(termcolor.colored(("[*] Ведидите длину пароля: "), 'green')))
        str1 = '1234567890qwertyuiopasdfghjklzxcvbnm-_;:QWERTYUIOPASDFGHJKLZXCVBNM'
        str2 = '-_;:'
        str3 = "QWERTYUIOPASDFGHJKLZXCVBNM"
        str4 = str1+str2+str3.upper()
        psw = ''.join([random.choice(str4) for x in range(vvod)])
        print(psw)

        proverka = input(termcolor.colored(("[!] напишите + если хотите сохранить пароль "), 'green'))

        if proverka == "+":
            with open('pasword.txt', 'a') as f:
                f.write(str(psw) + "\n")
                print("")
        else:
            time.sleep(0)
            os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана



