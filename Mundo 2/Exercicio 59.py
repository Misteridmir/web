flags=True
while flags==True:
 print("="*20)
 num1=int(input("Valor 1: "))
 num2=int(input("Valor 2: "))
 print("[1] Somar")
 print("[2] Subtrair")
 print("[3] Multiplicar")
 print("[4] Dividir")
 print("[5] Sair do programa")
 op=int(input("Qual das opções vc quer?: "))
 if op ==1:
  print("A soma de {} + {} = {}".format(num1,num2,num1+num2))   
 elif op ==2:
   print("A subtração de {} + {} = {}".format(num1,num2,num1-num2))   
 elif op ==3:
  print("A multiplicação de {} + {} = {}".format(num1,num2,num1*num2))     
 elif op ==4:
  print("A divisão de {} + {} = {}".format(num1,num2,num1/num2))     
 elif op ==5:
  print("Fechando programa!")
  flags=False       
 print("="*20)