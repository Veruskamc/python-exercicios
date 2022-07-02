print('**************************\n*******BEM VINDO AO*******\n***JOGO DA ADIVINHAÇÃO****\n**************************\n')


numero_secreto = 50
numero = 0
for c in range(1,10):
   if c == 10: break
   numero = int(input("Digite um número: "))

   print ('Você digitou ' , numero)
   acertou = numero == numero_secreto
   maior = numero > numero_secreto
   menor = numero < numero_secreto

   if (acertou):
    print ("\nPARABÉNS!! VOCÊ ACERTOU O NÚMERO SECRETO!")
    break
   elif (maior):
    print ("Errou! O número secreto é menor do que", numero,".\n")
   else:
    print ("Errou!O número secreto é maior do que", numero,".\n")

else:
    print ("\nVocê excedeu o número de tentativas. Tente outra vez!")
    

print("JOGUE OUTRA VEZ!")
    
