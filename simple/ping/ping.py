import os #import the os library(integrates operating system features)

print('#' * 30)
ip = input("Digite o ip a ser verificado:\n")
print('#' * 30)
os.system('ping -w 10 {}'.format(ip))
print('#' * 30)