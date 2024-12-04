def main():
    resposta = input("Você concorda? ").lower()
    concordo(resposta)


def concordo(resposta):
    if resposta == "sim" or resposta == "s":
        print("Eu concordo")
    elif resposta == "não" or resposta == "N" or resposta == "n":
        print("Não concordo")

main()