from random import randint
cont=0
status=False  
while status!=True:
 num=int(input("Digite um valor entre 0 e 10: "))
 ip=str(input("Escolha impar ou par[I/P]:")).strip().upper()[0] # impar True , par False
 if ip == "I" :
  ip_log=1
 else:
  ip_log=0
 pc_num=randint(0,10)
 total= pc_num+num
 cont+=1
 if total%2 == ip_log:
     print(f"Você jogou {num}, o pc jogou {pc_num} somado {total}, parabén você venceu!")
     
 else:
      print(f"Você jogou {num}, o pc jogou {pc_num} somado {total}, Você perdeu... ")
      status=True
print(f"Você jogou {cont} vezes até perder!")

