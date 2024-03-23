def file_creator():
    file = input("Digite o nome do arquivo que deseja criar: " )
    print(f"Arquivo {file}.txt criado com Sucesso")
    open(file + ".txt", "x")

def sentence():
    file = input("Digite o nome do arquivo que deseja abrir: ")
    with open(file + ".txt", "a")as file:
        frase = input("Digite a frase que deseja inserir: ")
        file.write(frase)
        print("A frase foi adicionada com Sucesso")

def read():
    file = input("Digite o nome do arquivo que deseja abrir: ")
    with open(file + ".txt", "r")as file:
        print(file.read())


file_creator()
sentence()
read()
