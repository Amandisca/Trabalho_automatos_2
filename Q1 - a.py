(
ALFABETO,
FUNCAO_TRANSICAO,
ESTADO_INICIAL,
ESTADO_FINAL
) = range(4)


def processa_palavra(maquina, palavra):
    if not validate_maquina(maquina) or not validate_palavra(maquina[ALFABETO], palavra):
        return None    # Processamento do automato.
    state = machine[ESTADO_INICIAL]
    for char in string:
        estado = machine[FUNCAO_TRANSICAO][estado][char]

    return (estado in machine[ESTADO_FINAL])



alfabeto = set(['a', 'b', 'c'])
func_trans = {'1' : {'a' : 'q2'},
              '2' : {'b' : 'q3'},
              '3' : {'c' : 'q4', 'b' : 'q3'},
              '4' : {'c' : 'q4', 'a' : 'q2'}}
estado_inicial = 'q1'
estado_final = set(['q1']['q2']['q3']['q4'])
maquina = (alphabet, trans_func, start_state, final_states)
palavras = ['abc', 'aa', 'abac', 'abcd', 'abbbbbb', '']

for palavras in palavras:
        resultado = processa_palavra(maquina, palavras)
        if result != None:
            print ('%s = %s' % (string, result))
