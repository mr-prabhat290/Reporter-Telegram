import time, os, platform
try:
    from prettytable import PrettyTable
except:
    os.system("pip install prettytable")
    from prettytable import PrettyTable

# Colors
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)

banner = f"""
                                                                 
{k}                                                                
                              -     -                            
                            .+       +.                          
                           :#         #:                         
                          =%           %-                        
      {lrd}REPORTER{k}     -*%.  {g}Innocent Aatma{k}  .%+   {be}TELEGRAM      {k}       
                        #@:             -@#                      
                     :  #@:             :@*  :                   
                    -=  *@:             -@*  =-                  
                   -%   *@-             =@+   %-                 
                  -@=  .*@+             +@+.  =@-                
                 =@%   .+@%-    :.:    -@@+.   #@:               
                =@@#:     =%%-+@@@@@+-%%=     .#@@=              
                 .+%@%+:.   -#@@@@@@@#-   .:=#@%=                
                    -##%%%%%#*@@@@@@@*#%%%%%##-                  
                  .*#######%@@@@@@@@@@@%#######*.                
               .=#@%*+=--#@@@@@@@@@@@@@@@#--=+*%@#=.             
            .=#@%+:     *@@@@@+.   .+@@@@@*     :+%@#=.          
          :*@@=.    .=#@@@@@@@       @@@@@@@#=.    .=@@*.        
            =@+    .%@@*%@@@@@*     *@@@@@%*@@%.    +@=          
             :@=    +@# :@@@@@#     #@@@@%. #@+    =@:           
              .#-   :@@  .%@@#       #@@#.  @@:   -#.            
                +:   %@:   =%         %=   :@%   -+              
                 -.  +@+                   +@+  .-               
                  .  :@#                   #@:  .                
                      %@. {cn}@EsFelurm{k} | {lgn}Innocent Aatma{k} .@%                    
                      :+@:               =@+:                    
                        =@:             :@-                      
                         -%.           .%:                       
                          .#           #.                        
                            +         +                          
                             -       -                     
"""

def show_menu():
    re(banner)
    print(f"{lrd}\n")
    re(f"""{yw}
╔══════════════════════════════════════════════╗
║ {rd}WARNING! {pe}Use this script only for educational use.  ║
║ Any misuse is the user's responsibility. 
  innocent aatma 
╚══════════════════════════════════════════════╝
""")
    print(f"{lrd}")
    t = PrettyTable([f'{cn}Option{lrd}', f'{cn}Description{lrd}'])
    t.add_row([f'{lgn}1{lrd}', f'{gn}Report a Telegram Channel{lrd}'])
    t.add_row([f'{lgn}2{lrd}', f'{gn}Report a Telegram User Account{lrd}'])
    t.add_row([f'{lgn}3{lrd}', f'{gn}Report a Group (Coming Soon){lrd}'])
    t.add_row([f'{lgn}0{lrd}', f'{gn}Exit Program{lrd}'])
    print(t)

# File paths
channel_script = "report/reporter.py"
account_script = "report/report.py"

def start():
    clear()
    show_menu()
    try:
        choice = input(f"\n{lrd}[{lgn}?{lrd}] {gn}Enter your option: {cn}")
        if choice == "1":
            if os.path.exists(channel_script):
                os.system(f"python {channel_script}")
            else:
                print(f"{rd}Script not found: {channel_script}")
        elif choice == "2":
            if os.path.exists(account_script):
                os.system(f"python {account_script}")
            else:
                print(f"{rd}Script not found: {account_script}")
        elif choice == "3":
            print(f"{yw}\n[!] Group reporter is under development. Coming soon!")
        elif choice == "0":
            print(f"{lgn}Exiting. Thank you!\n")
            exit(0)
        else:
            print(f"{rd}Invalid input. Please enter 1, 2, 3, or 0.")
    except Exception as e:
        print(f"{rd}Error: {str(e)}")

# Main loop
while True:
    start()
    input(f"\n{gn}Press Enter to return to main menu...")
    clear()
