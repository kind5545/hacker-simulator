#modules
import time

#vars
WifiNetwork = "No Wifi Connection."
#setup
print("welcome to...")
print('''
  ▄▄                                                                                         
 ▄██                                                 ▀████▀                                  
  ██                                                   ██                                    
  ██▄████▄ ▀██▀   ▀██▀████████▄ ▄█▀██▄  ▄██▀███▄██▀███ ██       ▄██▀██▄ ▄█▀█████     █▄▄▄▄▄▄ 
  ██    ▀██  ██   ▄█   ██   ▀████   ██  ██   ▀▀██   ▀▀ ██      ██▀   ▀████  ██      ▄█       
  ██     ██   ██ ▄█    ██    ██ ▄█████  ▀█████▄▀█████▄ ██     ▄██     ███████▀      █████▄▄  
  ██▄   ▄██    ███     ██   ▄████   ██  █▄   ███▄   ██ ██    ▄███▄   ▄███                ▀██ 
  █▀█████▀     ▄█      ██████▀ ▀████▀██▄██████▀██████▀█████████ ▀█████▀ ███████     █     ██ 
             ▄█        ██                                              █▀     ██   ███  ▄██  
           ██▀       ▄████▄                                            ██████▀      █████    
''')
print("please login")
name = input("username ")
pw = input("password ")
print("welcome,",name,".")
print("\n")
print("type cmd() for help.")
 #functions
def cmd():
     print("wifiDump() removes wifi connection from client.")
     print("wifiJoin() allows client to join discoverable networks.")
     print("logOut() sign the user out and closes the client.")
     print("help() displays this menu.")
     print("remoteDesk() allows client to connect to an external ip adress.")
     print("rdClose() disconects from remote desktop.")
     print("main() returns to the {main} directory.")
     print("newSession() makes a new session.")
     print("apps() opens a list of apps for client to choose from.")
     print("sysData() fetches data about the client.")
     print("more commands coming soon!")
  
def wifiDump():
  print("starting wifi dump...")
  time.sleep(0.3)
  print("...")
  time.sleep(0.2)
  print("wifi dump complete.")

def wifiJoin():
  print('loading discoverable networks...')
  time.sleep(0.5)
  print('''5GHz networks:
  > JoeWifi
  > Fios-dJqv8
  > homeWifi5
  > McDonalds Wifi''')
  WifiNetwork = input("type in network to join. ")
  time.sleep(1)
  print("joining",WifiNetwork,"...")
  time.sleep(0.7)
  print("sucessffuly joined",WifiNetwork,".")
  

def logOut():
  pass

def remoteDesk():
  pass

def rdClose():
  pass

def newSession():
  pass

def apps():
  pass

def main():
  pass
#start for realzies
while True:
  user_input = input("> ")
  if user_input == "cmd()":
    cmd()
  elif user_input == "wifiDump()":
      wifiDump()
  elif user_input == "wifiJoin()":
    wifiJoin()
  elif user_input == "logOut()":
    logOut()
  elif user_input == "help()":
   cmd()
  elif user_input == "remoteDesk()":
   remoteDesk()
  elif user_input == "rdClose()":
    rdClose()
  elif user_input == "main()":
    main()
  elif user_input == "newSession()":
    newSession()
  elif user_input == "apps()":
   apps()
  elif user_input == "sysData()":
    print("username:",name)
    print("password:",pw)
    print("network:",WifiNetwork)
  else:
    print("command not found.")
