p=float(input("Qual o valor do produto?: "))
print("Qual a forma de pagamento? ")
print("1- À vista dinheiro/cheque")
print("2- À victa no cartão")
print("3- Até 2X no cartão")
print("4- 3X ou mais no cartão")
f=int(input())
if f == 1:
  print("O valor final do Produto é R${:.2f}, devido aos 20% de desconto".format(p-((p*10)/100)))
if f == 2:
  print("O valor final do Produto é R${:.2f}, devido aos 5% de desconto".format(p-((p*5)/100)))
if f == 3:
  print("O valor final do Produto é R${:.2f}".format(p))
if f == 4:
  print("O valor final do Produto é R${:.2f}, você pagara juros de 20%".format(p+((p*20)/100)))    