import socket
import os
from config import SETTINGS
import subprocess
import datetime

print("Waiting for new incomings...")

settings = SETTINGS()

# config
IPADDRESS = '192.168.2.28'  # settings.IPADDRESS
PORT = settings.PORT


# win commands
# os.system('cmd dotnet build ' + PROJECT_DIRECTORY + r'\ascsite.sln -c Release')
# os.system(EXECUTABLE_PATH)


def console_log(*text):
    print(*text)


def kill():
    import os
    if os.path.exists(settings.CURRPID_ADDRESS):
        f = open("../" + settings.CURRPID_ADDRESS, "rt")
        pid = int(f.read())
        f.close()
        os.system("taskkill /pid " + str(pid) + " /f")
        return True
    else:
        return False


encoding_ = "utf8"

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (IPADDRESS, PORT)
sock_.bind(server_address)
sock_.listen(1)

while True:
    conn_, addr_ = sock_.accept()
    try:
        while True:
            received_data = conn_.recv(1024)
            console_log('Got a request! From', datetime.datetime.now())

            # Git pull
            console_log("Pulling...")
            status = subprocess.check_output('cd "' + settings.GIT_DIRECTORY + '" & D: & git pull', shell=True)

            # Check for changes
            if status.startswith(b'Already up to date.'):
                console_log('Repository is up to date, aborting...')
                break

            # Kill process
            if kill():
                console_log("Killed existing process")
            else:
                console_log("No site has been running before")

            # Run project
            console_log("Executing...")
            # subprocess.Popen(EXECUTABLE_PATH)
            os.system('python "' + settings.MANAGE_PATH + '" runserver 0.0.0.0:80')
            break
    except Exception as e_:
        console_log("Error:", e_)
    conn_.close()
