#Calculadora de C pra Python
print("Welcome the Calculation")
print()
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um segundo numero: "))
escolha = input("Digite a operaçao selecionada: ")
print()
soma = (num1 + num2 )
subtracao = (num1 - num2)
multiplicacao = (num1 * num2)
divisao = (num1 / num2)
rest_div = (num1 % num2)
potencia = (num1 ** num2)
if(escolha == '+'):
    print("A soma de %.1f com %.1f e igual a %.1f " % (num1, num2, soma))
elif(escolha == '-'):
    print("A subtração de %.1f com %.1f e igual a %.1f " % (num1, num2, subtracao))
elif(escolha == '*'):
    print("A multiplicação entre %.1f e %.1f e igual a %.1f " % (num1, num2, multiplicacao))
elif(escolha == '/'):
    print("A divisão entre %.1f e %.1f e igual a %.1f " % (num1, num2, divisao))
elif(escolha == '%'):
    print("O resto da divisão de %.1f e %.1f e igual a %.1f" % (num1, num2, rest_div))
elif(escolha == '**'):
    print("A potência entre %.1f e %.1f e igual a %.1f" % (num1, num2, potencia))
elif(escolha == "help"):
    print()
    print("Sinais das operações")
    print("Para somar use: '+'")
    print("Para subtrair use: '-'")
    print("Para multiplicar use: '*'")
    print("Para dividir use: '/'")
    print("Para obter o resto da divisão use: '%'")
    print("Para ter a potência use: '**'")
    print("Para todas as operações suportadas use: 'todas'")
    print()
elif( escolha == "todas"):
    print("A soma de %.1f com %.1f e igual a %.1f " % (num1, num2, soma))
    print("A subtraçao de %.1f com %.1f e igual a %.1f " % (num1, num2, subtracao))
    print("A multiplicaçao entre %.1f e %.1f e igual a %.1f " % (num1, num2, multiplicacao))
    print("A divisao entre %.1f e %.1f e igual a %.1f " % (num1, num2, divisao))
    print("O resto da divisao de %.1f e %.1f e igual a %.1f" %(num1, num2, rest_div))
    print("A potencia entre %.1f e %.1f e igual a %.1f" % (num1, num2, potencia))
else:
    print("Voce nao digitou uma operaçao valida, se quiser ajuda digite help no local da operaçao!")
    print()
    print("Obrigado Por Usar Nossa Calculadora!")
