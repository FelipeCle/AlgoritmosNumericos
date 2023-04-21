import numpy as np

def imprimir(A,n):
  for i in range(n):
    for j in range(n+1):
      if j==(n-1):
        print(A[i][j],end="|")
      else:
        print(A[i][j],end="\t\t")
    print("\n")
  
n=int(input("Digite a ordem da sua matriz : "))
matriz_solucao = np.zeros(n)
matriz = np.zeros((n,n+1))
#Inserindo matriz
for i in range(n):
  for j in range(n):
    matriz[i][j] = float(input(f"Insira o numero da : Linha {i},Coluna {j}\n"))
#Inserindo vetor dos valores de b
for i in range(n):
  matriz[i][n]= float(input('Digite o vetor b , de solução:\n'))
print("Matriz inicial :\n")
imprimir(matriz,n)

#Solução por gaus
for i in range(n):
  for j in range(i+1,n):
    multiplicador_linha = matriz[j][i]/matriz[i][i]
    #print(f'Multiplicador de:{matriz[j][i]},é igual a:{multiplicador_linha}')
    for k in range(n+1):
      matriz[j][k] = matriz[j][k] - multiplicador_linha * matriz[i][k]
      
print("Matriz resolvida:\n")
imprimir(matriz,n)

#Resolvendo a matriz final
matriz_solucao[n-1] = matriz[n-1][n]/matriz[n-1][n-1]
for i in range(n-2,-1,-1):
    matriz_solucao[i] = matriz[i][n]
    
    for j in range(i+1,n):
        matriz_solucao[i] = matriz_solucao[i] - (matriz[i][j]*matriz_solucao[j])
    
    matriz_solucao[i] = matriz_solucao[i]/matriz[i][i]


print('\nSolução para as variáveis: ')
for i in range(n):
    print('X%d = %0.2f' %(i,matriz_solucao[i]), end = '\t')
