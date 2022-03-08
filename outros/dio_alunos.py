n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = round((n1*2+n2*3+n3*4+n4)/10,1)
print('Media: %.1f' %media)

if(media==7): 
    n1=n1
elif(media>7):
    print('Aluno aprovado.')
elif(media<5):
    print('Aluno reprovado.')
elif(media<=6.9 and media>=5):
    print('Aluno em exame.')
    n5 = float(input())
    final = (n5+media)/2
    print('Nota do exame: %.1f' %n5)
    
    if(float('%.1f' %final) >= 5):
        print('Aluno aprovado.')
        print('Media final: %.1f' %final)
        #print('Media final: \n', round(final,1))
    else:
        print('Aluno reprovado')
        print('Media final: %.1f' %final)
        #print('Media final: \n', round(final,1))
