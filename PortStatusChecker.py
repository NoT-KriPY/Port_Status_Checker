import socket
print("                                         WELCOME, Do you want to Check the Port?")
wanna_check = str(input("Press Y for Yes, Press N for No:  ")).strip()
while True:    
    if wanna_check == 'Y' or wanna_check == 'y':
        Target_Ip = str(input("Please Input Your IP address:   ").strip())
        Target_Port = int(input("Please Input The Port Number:   ").strip())
        s_object = socket.socket()
        s_object.settimeout(2)    
        try:
            (s_object.connect((Target_Ip,Target_Port)))
            print("Port is Open")
            s_object.close()
            break
        except:
            print("Port is Closed")
            break

    elif wanna_check == 'N' or wanna_check == 'n':
        break
    else:
        print("Invalid Input, Please re-evaluate your answer")