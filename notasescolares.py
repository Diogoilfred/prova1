'''
3 - Elabore um programa em Python que leia as duas notas de prova (P1 e P2) e 
duas notas de trabalho (T1 e T2) e posteriormente exiba a mensagem ‘Aprovado’ 
ou ‘Não aprovado’ dependendo dos valores obtidos, conforme as regras de 
cálculo definidas a seguir:

Média de provas: MP = (P1 + P2)/2
Média de trabalhos: MT = (T1 + T2)/2
Média final: MF = 0,6MP + 0,4MT
Situação:
Se MF ≥ 6,0 → aprovado
Se MF < 6,0 → não aprovado
Usar funções.

'''
# ARMAZENA OS DADOS
def calcular_nota(p1,  p2, t1, t2):
# FAZ OS CÁLCULOS   
    mp = (p1 + p2)/2
    mt = (t1 + t2)/2
    mf = 0.6*mp + 0.4*mp
    return mf
# VERIFICA SE ESTA APROVADO OU REPROVADO
def verificar_situacao(mf):
        
    if mf >= 6.0:
        return "Aprovado"
    else: 
        return "Reprovado"
    
def main():
#RECEBE OS DADOS
    print(" Cálculo da média final: ")
    p1 =  float(input("Nota da 1° prova: "))
    p2 =  float(input("Nota da 2° prova: "))  
    t1 =  float(input("Nota do 1° trabalho: "))
    t2 =  float(input("Nota do 2° trabalho: "))

    mf = calcular_nota(p1, p2, t1, t2)
    situacao = verificar_situacao(mf)
# EXIBE NA TELA A NOTA E SE ESTA APROVADO OU REPROVADO
    print(f"\nMédia Final: {mf:.2f}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()