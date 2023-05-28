import subprocess

def run_simple_scan(target):
    command = f'nmap {target}'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def run_detailed_scan(target):
    command = f'nmap -v {target}'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Print ASCII art
ascii_art = """
                                                                                                   
                    ,----..                            ,--.              ,----..             ,--. 
   ,---,           /   /   \                         ,--.'|    ,---,    /   /   \          ,--.'| 
  '  .' \         /   .     :           ,--,     ,--,:  : | ,`--.' |   /   .     :     ,--,:  : | 
 /  ;    '.      .   /   ;.  \        ,'_ /|  ,`--.'`|  ' : |   :  :  .   /   ;.  \ ,`--.'`|  ' : 
:  :       \    .   ;   /  ` ;   .--. |  | :  |   :  :  | | :   |  ' .   ;   /  ` ; |   :  :  | | 
:  |   /\   \   ;   |  ; \ ; | ,'_ /| :  . |  :   |   \ | : |   :  | ;   |  ; \ ; | :   |   \ | : 
|  :  ' ;.   :  |   :  | ; | ' |  ' | |  . .  |   : '  '; | '   '  ; |   :  | ; | ' |   : '  '; | 
|  |  ;/  \   \ .   |  ' ' ' : |  | ' |  | |  '   ' ;.    ; |   |  | .   |  ' ' ' : '   ' ;.    ; 
'  :  | \  \ ,' '   ;  \; /  | :  | | :  ' ;  |   | | \   | '   :  ; '   ;  \; /  | |   | | \   | 
|  |  '  '--'    \   \  ',  /  |  ; ' |  | '  '   : |  ; .' |   |  '  \   \  ',  /  '   : |  ; .' 
|  :  :           ;   :    /   :  | : ;  ; |  |   | '`--'   '   :  |   ;   :    /   |   | '`--'   
|  | ,'            \   \ .'    '  :  `--'   \ '   : |       ;   |.'     \   \ .'    '   : |       
`--''               `---`      :  ,      .-./ ;   |.'       '---'        `---`      ;   |.'       
                                `--`----'     '---'                                 '---'         
                                                                                                       
    www.github.com/aouni0n
"""

print(ascii_art)

# Prompt the user for inputs
target_ip = input("Enter the target IP address or hostname: ")
scan_type = input("Enter the type of scan (detailed/simple): ")

# Run the Nmap scan based on the scan type
if scan_type == "detailed":
    run_detailed_scan(target_ip)
else:
    run_simple_scan(target_ip)
