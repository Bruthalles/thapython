from classes.Animal import Cat,Dog
animals = ["","","","",""]

#iniciando com string exclusiva para debug
cat = Cat("voidex")
dog = Dog("voidex")

def catordog():

    pet = input("\n Cat or Dog ? ").lower()
   
    if(pet == "cat"):
        print(f"\nOlha o meme gritando miau. MIAAAAAAAAAAAAU")
    
    elif(pet == "dog"):
        print("\nAUUUUUUUUUUUU")
        print("Baby, I'm preyin' on you tonight")
        print("Hunt you down, eat you alive")
        print("Just like animals, animals")
        print("Like Animals-mals")

    else:
        print(f"Por acaso você não sabe escrever ou só tá me testando?")
        print(f"Isso aqui não é bagunça, ou você me obedece ou cai fora >:(")
    
def Pg_animals():
    print("\nExecutando Programa de animais... ")
    Cat.fazer_som(catordog())
    