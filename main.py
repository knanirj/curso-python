#coding: utf-8
	
#def script3(vet8):
vet8=[1 , 3.4 , 'A' , " IFSC " ]
vet8_copia = copy(vet8)
print("vetor recebido:", vet8)
pos_in=1
pos_fin=3
del vet8[pos_in:pos_fin]
print(f"vetor com posicao (pos) removido", vet8)
print ("remover por pop")

