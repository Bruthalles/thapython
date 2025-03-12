import getpass
from classes import Cadastro
from classes import ContaBancaria

usr = Cadastro.Usuario()
count = ContaBancaria.Contabancaria(0,0)

def option():
    result = int(input("\nEscolha uma ação: "))

    if(result== 1):
        count.show_balance()
        option()

    elif(result==2):
        valor = input("\nQuanto irá depositar? ")
        count.fill(valor)
        option()

    elif(result==3):
        valor = input("\nDigite valor para saque: ")
        count.empty(valor)
        option()

    else: 
        print("\nOPÇÃO INDISPONÍVEL!")
        option()

def menu():
    
    print("\nDigite 1 para ver saldo |")
    print("\nDigite 2 para depositar |")
    print("\nDigite 3 para resgatar  |")
    option()

'''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'''
def login():

    check_name = input("\nInsira nome de usuário: ")
    check_passw = getpass.getpass("\nInsira sua senha: ")

    if(check_name == usr.name and check_passw == usr.passw):
        print(f"\n=======Bem-vindo, {usr.name}=======")
        menu()

    else: print("\nNOME DE USUÁRIO OU SENHA INCORRETOS")

if __name__ == "__main__":
    if (usr.name == None):
        usr.name = input("\nCadastre um nome de usuário para entrar na conta: ")

    if(usr.passw == None):
        usr.passw = getpass.getpass("\nCadastre sua senha para passar: ")
        login()

    else:
        login()