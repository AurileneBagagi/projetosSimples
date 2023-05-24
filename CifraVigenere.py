A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def VeriNumero(valor):
    try:
        float(valor)
        return True
    except: return False

def RetirarCar(Mensagem):
    Nov = ''
    for a in Mensagem:
        if a != ' ' and VeriNumero(a) == False: Nov+=a
    return Nov
        
def VeriChave(Men, Chave):
    NovaChave = ''
    if Men >= len(Chave):
        divisao = Men // len(Chave)
        NovaChave = Chave*divisao
        for a in range(Men%len(Chave)): NovaChave+=Chave[a]
    else:
        for a in range(Men): NovaChave+=Chave[a]
    return NovaChave
'''        
Mensagem = input('Insira a Mensagem: ').lower()
Chave = input('Insira a chave: ').lower()

NovMensagem = RetirarCar(Mensagem)
NovaChave = VeriChave(len(NovMensagem),Chave)

Mensagem = ''
for a in range(len(NovMensagem)):
    Mensagem+=A[(A.index(NovMensagem[a])+A.index(NovaChave[a]))%26]
print(Mensagem)
'''
#---------------------Descriptografar------------------

Cifra = input('Insira a Mensagem: ').lower()
Llave = input('Insira a chave: ').lower()

NuevMen = RetirarCar(Cifra)
NuevaLlave = VeriChave(len(Cifra),Llave)

Mensaje = ''
for a in range(len(NuevMen)):
    Mensaje+=A[(A.index(NuevMen[a])-A.index(NuevaLlave[a]))%26]
print(Mensaje)
