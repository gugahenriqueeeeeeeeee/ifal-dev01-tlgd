def main():
    altura = int(input("informe o tamanho da coluna:"))
    coluna(altura)

def coluna(tamanho):
    print("[]\n" * tamanho, end = '')


main()