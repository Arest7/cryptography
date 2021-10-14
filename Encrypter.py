from cryptography.fernet import Fernet
import os
from rich import print
from art import *

key = "yvDgHpSNhl84yClVdPQmbi4p-T8Yi7Q_T3tdJ0awu08="
f = Fernet(key)
os.system("clear")
tprint("Encrypter", font="random")
print("[bold red]Github: https://github.com/Arest7 [/bold red]")

text = input("Enter text to encrypting: ")
b_text = bytes(text, 'UTF-8')
token = f.encrypt(b_text)
print(token)
