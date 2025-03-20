'''Permita que a Pessoa tenha mais de um endereço e imprima todos.'''
from classes.Relationship import *

#iniciando atributos com qualquer conteúdo exclusivo para melhorar debug
people = People("voidex","voidex","voidex")

def make_lista():

    choose = input("\nAdicionar mais um endereço ? S/N: ").upper()
    if(choose == "S"):
        
        people.location.street = input("\nNome da rua: ")
        people.location.city = input("\nCidade: ")
        region = f"{people.location.street}, {people.location.city}" 
        people.add_location(region)
        make_lista()

    else: return 0

def Pg_enderecos():

    print("\nExecutando Programa de endereços... ")
    people.name = input("\nNome do(a) morador(a): ")
    people.age = input("\nidade do(a) morador(a): ")
    people.location.street = input("\nNome da rua: ")
    people.location.city = input("\nCidade: ")
    region = f"{people.location.street}, {people.location.city}" 
    people.list.append(region)
    make_lista()

    