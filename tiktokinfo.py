import requests

def tiktok():
    logo = ("""
     
 ██░ ██ ▓█████ ▒██   ██▒    █     █░ ▄▄▄    ██▒   █▓▓█████ 
▓██░ ██▒▓█   ▀ ▒▒ █ █ ▒░   ▓█░ █ ░█░▒████▄ ▓██░   █▒▓█   ▀ 
▒██▀▀██░▒███   ░░  █   ░   ▒█░ █ ░█ ▒██  ▀█▄▓██  █▒░▒███   
░▓█ ░██ ▒▓█  ▄  ░ █ █ ▒    ░█░ █ ░█ ░██▄▄▄▄██▒██ █░░▒▓█  ▄ 
░▓█▒░██▓░▒████▒▒██▒ ▒██▒   ░░██▒██▓  ▓█   ▓██▒▒▀█░  ░▒████▒
 ▒ ░░▒░▒░░ ▒░ ░▒▒ ░ ░▓ ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░
 ▒ ░▒░ ░ ░ ░  ░░░   ░▒ ░     ▒ ░ ░    ▒   ▒▒ ░░ ░░   ░ ░  ░
 ░  ░░ ░   ░    ░    ░       ░   ░    ░   ▒     ░░     ░   
 ░  ░  ░   ░  ░ ░    ░         ░          ░  ░   ░     ░  ░
                     FaceBook-"Hex Wave"
                     Github  -"HEX-WAVE" 
  
     """)                                                                                                    """)
    print(logo)
    
    user_input = input('Enter Tiktok Username: ')
    url = f'http://localhost:8080/tiktok-info.php?username={user_input}'
    
    try:
        req = requests.get(url).json()
        
        print(req)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

tiktok()
