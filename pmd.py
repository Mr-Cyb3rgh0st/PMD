import os
import sys
import marshal,zlib,base64
from colorama import Fore
banner =(Fore.RED +  '''

888b     d888           .d8888b.           888       .d8888b.                  888                .d8888b.  888    
8888b   d8888          d88P  Y88b          888      d88P  Y88b                 888               d88P  Y88b 888    
88888b.d88888          888    888          888           .d88P                 888               888    888 888    
888Y88888P888 888d888  888        888  888 88888b.      8888"  888d888 .d88b.  88888b.  .d8888b  888    888 888888 
888 Y888P 888 888P"    888        888  888 888 "88b      "Y8b. 888P"  d88P"88b 888 "88b 88K      888    888 888    
888  Y8P  888 888      888    888 888  888 888  888 888    888 888    888  888 888  888 "Y8888b. 888    888 888    
888   "   888 888  d8b Y88b  d88P Y88b 888 888 d88P Y88b  d88P 888    Y88b 888 888  888      X88 Y88b  d88P Y88b.  
888       888 888  Y8P  "Y8888P"   "Y88888 88888P"   "Y8888P"  888     "Y88888 888  888  88888P'  "Y8888P"   "Y888 
                                       888                                 888                                     
                                  Y8b d88P                            Y8b d88P                                     
                                   "Y88P"                              "Y88P"                                      
 ''' + Fore.GREEN + '''Python Marshal Decoder(PMD) ''')         
print(banner)
print(Fore.WHITE + "   \nCreated by Mr.Cyb3rgh0st")
def marshal2():
    decode = input(Fore.GREEN + "\n[+]Enter the encrypted code here: " + Fore.WHITE +"")

    z = (marshal.loads(zlib.decompress(base64.b16decode(decode))))
    os.system("touch output.txt")
    from uncompyle6.main import decompile
    decompile(2.7,z,open('output.txt','w'))
    print(Fore.GREEN + "\n\nThe decoded python2 script has been saved in output.txt\n\n"+ Fore.RED + "Please delete the output.txt before using this tool again!")

def marshal3():
    decode = input(Fore.GREEN + "\n[+]Enter the encrypted code here: " + Fore.WHITE + "")

    z = (marshal.loads(zlib.decompress(base64.b16decode(decode))))
    os.system("touch output.txt")
    from uncompyle6.main import decompile
    decompile(3.9,z,open('output.txt','w'))
    print(Fore.GREEN + "\n\nThe decoded python3 script has been saved in output.txt\n\n"+ Fore.RED + "Please delete the output.txt before using this tool again!")
    
def marshal4():
    decode = input(Fore.GREEN + "\n[+]Enter the encrypted code here: " + Fore.WHITE + "")

    z = (marshal.loads(zlib.decompress(base64.b64decode(decode))))
    os.system("touch output.txt")
    from uncompyle6.main import decompile
    decompile(2.7,z,open('output.txt','w'))
    print(Fore.GREEN + "\n\nThe decoded python2 script has been saved in output.txt\n\n"+ Fore.RED + "Please delete the output.txt before using this tool again!")    

def marshal5():
    decode = input(Fore.GREEN + "\n[+]Enter the encrypted code here: " + Fore.WHITE + "")

    z = (marshal.loads(zlib.decompress(base64.b64decode(decode))))
    os.system("touch output.txt")
    from uncompyle6.main import decompile
    decompile(2.7,z,open('output.txt','w'))
    print(Fore.GREEN + "\n\nThe decoded python3 script has been saved in output.txt\n\n"+ Fore.RED + "Please delete the output.txt before using this tool again!")
try:
   if sys.version_info[0] < 2.7:
     print(Fore.RED + "\n\n\nPython2 Interpretor Selected\n")
     choice = int(input(Fore.WHITE + "[+]Select the base64 bits(1.64Bit/2.16Bit): "))
     if choice == 1:
         marshal4()
     elif choice == 2:
         marshal2()

   elif sys.version_info[0] < 3.9:
     print(Fore.RED + "\n\n\nPython3 Interpretor Selected\n")
     choice = int(input(Fore.WHITE + "[+]Select the base64 bits(1.64Bit/2.16Bit): "))
     if choice == 1:
         marshal5()
     elif choice == 2:
         marshal3()
     
   else:
     pass

except KeyboardInterrupt:
    print(Fore.RED + "\n\nCtrl + C detected Exiting!!")