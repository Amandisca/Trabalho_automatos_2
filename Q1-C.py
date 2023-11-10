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



alfabeto = set(['a', 'b'])
func_trans = {{'q1' : {'a' : 'q2',},
             'q2' : {'a' : 'q3', 'b': 'q5'},
             'q3' : {'a' : 'q3', 'b': 'q4'},
             'q5' : {'a' : 'q6', 'b': 'q5'}}
    
}
estado_inicial = 'q1'
estado_final = set(['q4']), set(['q6'])
maquina = (alfabeto, func_trans, estado_inicial, estado_final)
palavras = ['abc', 'aa', 'abac', 'abcd', 'abbbbbb', '']

for palavras in palavras:
        resultado = processa_palavra(maquina, palavras)
        if result != None:
            print ('%s = %s' % (string, result))
