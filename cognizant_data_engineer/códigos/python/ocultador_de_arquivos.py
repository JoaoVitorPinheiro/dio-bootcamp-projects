import ctypes

# Pode ocultar arquivos ou até pastas
# C:/pasta
text = input('Texto do arquivo : ')
file = "arquivo_oculto.txt"

with open(file, "w", newline='') as f:
    f.write(text)
    
atributo_ocultar = 0x02      # FILE_ATTRIBUTE_HIDDEN 
# https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileattributesw

retorno = ctypes.windll.kernel32.SetFileAttributesW(file, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
    
else:
    print("Arquivo não foi ocultado")
