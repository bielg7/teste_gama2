'''
1 - O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
e dos impostos (aplicados ao custo de fábrica).
Supondo que a porcentagem do distribuidor seja de 8% do preço de fábrica e os impostos de 20% do preço de
fábrica, fazer um programa em Python para ler o
custo de fábrica de um carro e imprimir, o preço de fábrica, o valor do imposto, o valor da porcentagem do
distribuidor custo e ao consumidor. Usar funções.

'''
# custo carro novo = porcentagem do distribuidor + impostos
# dist = fab * 8/100
#imp = fab * 20/100

def fab(custo_fab):
   print("O Preço de Fábrica é: ", custo_fab)
    
    
def porcentagem_distribuidor():
    dist = 8/100
    
    return dist
    
def impostos():
    imp =  20/100
    
    return imp

    
    
    
def main():
    custo_fab = float(input("Digite o valor de Fábrica:\n").strip())
    fab(custo_fab)
    porcentagem_distribuidor()
    impostos()
    
    total = custo_fab + (custo_fab * impostos()) + (custo_fab * porcentagem_distribuidor())
    print("O valor de Fábrica é: \n", custo_fab)
    print("A porcentagem do distribuidor é: \n", (custo_fab * porcentagem_distribuidor()))
    print("O imposto é: \n", (custo_fab * impostos()))
    print("O total que o cliente irá pagar é: ", total)
    
    
    
    
    
    
if __name__ == "__main__":
    main()