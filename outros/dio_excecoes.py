
lista = [1,10]

try:
    a=b
    divisao = 10 / 1
    numero = lista[0]
except ZeroDivisionError:
    print("Nao da pra dividir por 0")
except IndexError:
    print("Erro de index")
except Exception as e:
    print("Erro desconhecido: {}" . format(e))


class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message
        
while True:
    try:
        x = int(input("0 a 10: "))
        
        if(x > 10):
           raise InputError("Nota não pode ser > 10")
        
        if(x < 0):
           raise InputError("Nota não pode ser < 0")
#Se as condições forem satisfeitas, essa linha do break é pulada e vai direto pro except
        break
    
    except ValueError:
        print("Valor invalido. Só pode integer\n")
    except InputError as e:
        print(e)




#if __name__=='__main__':
