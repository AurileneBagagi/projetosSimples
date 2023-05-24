import random
#==============Caracteres====================
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*()"
line = lowerCase + upperCase + numbers + symbols
#==============Função====================
tamanhoSenha = int(input("Defina o tamanho da senha: "))
passWord = "".join(random.sample(line, tamanhoSenha))
print("senha gerada: {}".format(passWord))