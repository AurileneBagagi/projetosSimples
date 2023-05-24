import random
#==============Caracteres====================
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*()"
#==============Caracteres====================
line = lowerCase + upperCase + numbers + symbols

tamanhoSenha = int(input("Defina o tamanho da senha: "))

passWord = "".join(random.sample(line, tamanhoSenha))

print("senha gerada: {}".format(passWord))