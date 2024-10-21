#coding: utf-8
'''
def Insercao_dado(): 
	vC = [1 , 3.4 , 'A' , " IFSC " ]
	print("Vetor Original:", vC)
	#input("Digite enter para prosseguir: ")
	vC.insert(0,56) #Adiciona na posição 0 o inteiro 56.
	print("Insercao de 56 na posicao 0:", vC)
	#input("Digite enter para prosseguir: ")
	vC.insert(3,'B')
	print("Insercao de B na posicao 3:", vC)
	#input("Digite enter para prosseguir: ")
	vC.append(11)	
	print("Inserção no final do valor 11: ", vC) 
	#input("Digite enter para prosseguir: ")
	print("Impressao por coluna do vetor:")
	for i in vC :
		print ( i )
	print("Fim da funcao Insercao_dado()")
	return vC 	
def Remocao_dado(vet): 
	print("Vetor recebido: ", vet)
	print("Elemento 'A' removido")
	vet.remove('A') 
	print("Vetor alterado: ", vet)
	input("Digite enter para prosseguir")
	
	print("Fim da função Remocao_dado()")

def script02(vetA)
    print("vetor recebido:", vet(A))
	
if __name__ == "__main__": 
	vet = script02()	
	Remocao_dado(vet)
'''


vetA= [1 , 3.4 , 'A' , " IFSC " ]
print (vetA)
vetA.remove(3.4)
print ('escolha a remecao de A')
escolha = input ("pression 1 para remove a primera .. muito tecla para todo")
if (escolha == "1" ):
   vetA.remove("A")
else :
   while "A" in vetA :
      vetA.remove("A")
      print("vetor final": vetA)


	
