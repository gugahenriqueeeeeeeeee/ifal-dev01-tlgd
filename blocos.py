def main():
    linha = int(input("qual o tamanho do bloco? "))
    bloco(linha)
def bloco(linha):
    bloco = ("[]" * linha)
    print(f"{bloco}\n" * linha, end = "")

main()
