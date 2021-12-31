def main():
    from sys import platform as OS
    from os import system as commandPrompt
    from time import sleep



    __NAME__ = "IP Information Lookup"
    __AUTHOR__ = "Parham"
    __VERSION__ = 1.0
    __LICENSE__ = "MIT"

    try:
        from requests import get as requestsGet
    except ModuleNotFoundError:
        systemOS = OS
        print("Requests Module Was Not Found")
        if systemOS.lower() == "win32":
            sleep(0.1)
            print("You Can Install It With 'pip install requests'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            number = input("[?]> ")
            if number == "1":
                commandPrompt('pip install requests')
                print("\n"*100)
            else:
                exit()
        else:
            sleep(0.1)
            print("You Can Install It With 'pip3 install requests'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            number = input("[?]> ")
            if number == "1":
                commandPrompt('pip3 install requests')
                print("\n"*100)
            else:
                exit()
        

    try:
        from colorama import Fore, Back, Style, init
    except ModuleNotFoundError:
        systemOS = OS
        sleep(0.1)
        print("Colorama Module Was Not Found")
        sleep(0.1)
        if systemOS.lower() == "win32":
            print("You Can Install It With 'pip install colorama'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            sleep(0.1)
            number = input("[?]> ")
            if number == "1":
                sleep(0.1)
                commandPrompt('pip install colorama')
                print("\n"*100)
            else:
                exit()
        else:
            print("You Can Install It With 'pip3 install colorama'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            sleep(0.1)
            number = input("[?]> ")
            if number == "1":
                commandPrompt('pip3 install colorama')
                print("\n"*100)
            else:
                exit()


    try:
        from IPy import IP as IPchecker
    except ModuleNotFoundError:
        systemOS = OS
        print("IPy Module Was Not Found")
        if systemOS.lower() == "win32":
            sleep(0.1)
            print("You Can Install It With 'pip install IPy'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            number = input("[?]> ")
            if number == "1":
                commandPrompt('pip install IPy')
                print("\n"*100)
            else:
                exit()
        else:
            sleep(0.1)
            print("You Can Install It With 'pip3 install IPy'")
            sleep(0.1)
            print("Press Any Key To Escape Or Press '1' To Automatically Install The Module:")
            number = input("[?]> ")
            if number == "1":
                commandPrompt('pip3 install IPy')
                print("\n"*100)
            else:
                exit()
    try:
        init(autoreset=True)

        print(Fore.RED + Style.BRIGHT + 
        """
                            IP Information Lookup
        """)
        sleep(0.1)
        print(Fore.RED + """            #==========================================#""")
        sleep(0.1)
        print(Fore.RED + """                    __NAME__ = IP Information Lookup""")
        sleep(0.1)
        print(Fore.RED + """                    __AUTHOR__ = Parham""")
        sleep(0.1)
        print(Fore.RED + """                    __VERSION__ = 1.0""")
        sleep(0.1)
        print(Fore.RED + """                    __LICENSE__ = MIT""")
        sleep(0.1)
        print(Fore.RED + """            #==========================================#""")
        sleep(0.1)

        print(Fore.WHITE + Style.DIM +"""With Help Of:""")
        sleep(0.1)
        print(Fore.WHITE + Style.DIM +"""   [+] www.ip-api.com""")
        sleep(0.1)
        print(Fore.WHITE + Style.DIM +"""   [+] www.ipify.org""")
        sleep(0.1)
        print(Fore.GREEN + Style.BRIGHT + """                        Services""")
        sleep(0.1)
        print(Fore.GREEN + """[1] IPv4""")
        sleep(0.1)
        print(Fore.GREEN + """[2] IPv6""")
        sleep(0.1)
        print(Fore.GREEN + Style.BRIGHT + "Choose One Of Our Services:")
        sleep(0.1)
        while True:
            serviceNum = input(Fore.YELLOW + "[" + Fore.GREEN + "?" + Fore.YELLOW + "]" + Fore.GREEN + ">" + Fore.RED + " ")
            sleep(0.1)
            if serviceNum == "1" or serviceNum == "2":
                serviceNum = int(serviceNum)
                break
        print("\n")
        sleep(0.1)
        if serviceNum == 1:
            print(Fore.RED + Style.BRIGHT + "                        IPv4\n")
            sleep(0.1)
            print(Fore.GREEN + Style.BRIGHT + "Enter A IPv4 Address:")
            sleep(0.1)
            while True:
                ipv4_unedited = input(Fore.YELLOW + "[" + Fore.GREEN + "?" + Fore.YELLOW + "]" + Fore.GREEN + ">" + Fore.RED + " ")
                sleep(0.1)
                try:
                    IPv4 = IPchecker(ipv4_unedited)
                    break
                except ValueError:
                    sleep(0.1)
                    print(Fore.RED + "Please Enter An" + Style.BRIGHT + " IPv4")
            response  = requestsGet(f"http://ip-api.com/json/{IPv4}?fields=66838527")
            if response.status_code == 200:
                response_json = response.json()
                for i in response_json:
                    sleep(0.1)
                    print(Fore.CYAN + Style.BRIGHT + f"{i}: " + Style.NORMAL + str(response_json[i]))
                input(Fore.YELLOW + "Press Enter To Exit")
                exit()
            else:
                sleep(0.1)
                print(Fore.RED + "Something Went Wrong ")
                exit()
        elif serviceNum == 2:
            print(Fore.RED + Style.BRIGHT + "                        IPv6\n")
            sleep(0.1)
            print(Fore.GREEN + Style.BRIGHT + "Enter A IPv6 Address:")
            sleep(0.1)
            while True:
                ipv6_unedited = input(Fore.YELLOW + "[" + Fore.GREEN + "?" + Fore.YELLOW + "]" + Fore.GREEN + ">" + Fore.RED + " ")
                sleep(0.1)
                try:
                    IPv6 = IPchecker(ipv6_unedited)
                    break
                except ValueError:
                    sleep(0.1)
                    print(Fore.RED + "Please Enter An" + Style.BRIGHT + " IPv6")
            response  = requestsGet(f"http://ip-api.com/json/{IPv6}?fields=66838527")
            if response.status_code == 200:
                response_json = response.json()
                for i in response_json:
                    sleep(0.1)
                    print(Fore.CYAN + Style.BRIGHT + f"{i}: " + Style.NORMAL + str(response_json[i]))
                input(Fore.YELLOW + "Press Enter To Exit")
                exit()
            else:
                sleep(0.1)
                print(Fore.RED + "Something Went Wrong ")
                exit()
        else:
            print(Fore.RED + "Something Went Wrong")
            exit()
    except KeyboardInterrupt:
        sleep(0.1)
        print(Fore.RED + "\nExiting...")
        exit()
    except:
        print(Fore.RED + "\n Something Went Wrong")


if __name__ == '__main__':
    main()
