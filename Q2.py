(
ALFABETO,
FUNCAO_TRANSICAO,
ESTADO_INICIAL,
ESTADO_FINAL
) = range(4)

contadorCOMP = 0
contadorESPACO = 0

def processa_palavra(maquina, palavra):
    estado = maquina[ESTADO_INICIAL]
    for char in palavra:
            if estado in maquina[ESTADO_FINAL]:
                print("Palavra encontrada! na posição" + contadorESPACO)
                contadorESPACO++
                contadorCOMP++
            else:
                if char == ' ':
                    contadorESPACO++
                    estado = maquina[ESTADO_INICIAL]
    return null




func_trans = {{'q1' : {'c' : 'q2'},
             'q2' : {'o' : 'q3'},
             'q3' : {'m' : 'q4'},
             'q4' : {'p' : 'q5'},
             'q5' : {'u' : 'q6'},
             'q6' : {'t' : 'q7'},
             'q7' : {'a' : 'q8'},
             'q8' : {'d' : 'q9'},
             'q9' : {'o' : 'q10'},
             'q10' : {'r' : 'q11'},
             'q11' : {' ' : 'q12'}
}}
             
estado_inicial = 'q1'
estado_final = set(['q12'])
maquina = (alfabeto, func_trans, estado_inicial, estado_final)
palavras = ["“O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico"]

for palavras in palavras:
        resultado = processa_palavra(maquina, palavras)


print("Numero de vezes que computador aparece: " + contadorCOMP)
