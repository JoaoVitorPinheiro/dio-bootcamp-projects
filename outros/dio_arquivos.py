import shutil

def escrever(texto):
    arquivo = open('notas.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar(texto):
    arquivo = open('notas.txt','a')
    arquivo.write(texto)
    arquivo.close()

def ler(nome_file):
    arquivo = open(nome_file,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_file):
    arquivo = open(nome_file,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split("\n")
    #print(aluno_nota)
    lista_media =[]
    for x in aluno_nota:
        lista = x.split(",")
        aluno = lista[0]
        lista.pop(0)
        print(aluno)
        print(lista)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista))
        lista_media.append({aluno:media(lista)})

    return lista_media

def copia(nome_file):
    shutil.copy(nome_file,'C:/Users/joaov/Desktop/notas2.txt')

def move(nome_file):
    shutil.move(nome_file,'C:/Users/joaov/Desktop/Consulta/notas3.txt')

    
if __name__=='__main__':

    lista_media = media_notas('notas1.txt')
    print(lista_media)
    copia("notas1.txt")
    move("notas2.txt")
    
    
