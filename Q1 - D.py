(
ALFABETO,
FUNCAO_TRANSICAO,
ESTADO_INICIAL,
ESTADO_FINAL
) = range(4)


def processa_palavra(maquina, palavra):
    estado = maquina[ESTADO_INICIAL]
    for char in palavra:
        if char not in alfabeto:
            return None    # Processamento do automato.
        else:
            estado = maquina[FUNCAO_TRANSICAO][estado][char]

    return (estado in maquina[ESTADO_FINAL])



alfabeto = set(['a', 'b', 'c'])
func_trans = {{'q1' : {'a' : 'q4', 'b' : 'q2'},
             'q2' : {'b' : 'q2', 'a' : 'q3'},
             'q3' : {'c' : 'q3'},
             'q4' : {'a' : 'q4', 'b' : 'q2', 'c' : 'q3'}}}
             
estado_inicial = 'q1'
estado_final = set(['q3']), set(['q4'])
maquina = (alfabeto, func_trans, estado_inicial, estado_final)
palavras = ['abc', 'aa', 'abac', 'abcd', 'abbbbbb', '']

for palavras in palavras:
        resultado = processa_palavra(maquina, palavras)
        if result != None:
            print ('%s = %s' % (string, result))
