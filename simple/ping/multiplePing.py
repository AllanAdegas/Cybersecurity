import os
import time

with open("./hosts.txt") as file:
    dump = file.read()
    dump= dump.splitlines()
    
    print(dump) 
    
    for ip in dump:
        print(('-'*15)+ ip + ('-' * 15))
        os.system('ping -c 2 {}'.format(ip))
        print(('-'*15)+ ip + ('-' * 15)) 
        time.sleep(5)
        