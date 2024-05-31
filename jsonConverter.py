from json import loads, load, dumps, dump

with open("db.json", encoding="UTF-8") as arquivo:
    arquivo_livros = load(arquivo)
    array_livros = []
    for livro in arquivo_livros["livros"]:
        array_livros.append(str(livro))

with open("livros.txt", "w", encoding="utf-8") as textFile:
    c = 1
    for livro in array_livros:
        textFile.write(f"Livro {c} = {livro}\n")
        c+=1



