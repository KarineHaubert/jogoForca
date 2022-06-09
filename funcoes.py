import os;
import sys;

def boasVindas():
    print("Bem-vinde ao ")
    print("""
    
     ██╗██████╗ ██████╗ ██████╗     ██████╗ █████╗     ███████╗██████╗██████╗ ██████╗█████╗ 
     ████╔═══████╔════╝██╔═══██╗    ██╔══████╔══██╗    ██╔════██╔═══████╔══████╔════██╔══██╗
     ████║   ████║  █████║   ██║    ██║  █████████║    █████╗ ██║   ████████╔██║    ███████║
██   ████║   ████║   ████║   ██║    ██║  ████╔══██║    ██╔══╝ ██║   ████╔══████║    ██╔══██║
╚█████╔╚██████╔╚██████╔╚██████╔╝    ██████╔██║  ██║    ██║    ╚██████╔██║  ██╚████████║  ██║
 ╚════╝ ╚═════╝ ╚═════╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═════╝╚═╝  ╚═╝╚═════╚═╝  ╚═╝
                                                                                            
    """)

    


def limparTela():
    os.system("cls")

def continuar():
    os.system("pause")
 
def mostraPalavra(palavra, chutes):
    for i in range(len(palavra)): 
        if (palavra[i] in chutes):
            sys.stdout.write(palavra[i])
        else: 
            sys.stdout.write('_')
        sys.stdout.write(' ')


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/    ")
        print(" |       |     ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |     ")
        print(" |      /     ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \    ")

    

    print(" |            ")
    print("_|___         ")
    print()
    



def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    return

def perdeu(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
