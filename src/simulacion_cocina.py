def competencia() :
    rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            },
            'Camila': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Santiago': {
                'judge_1': 6,
                'judge_2': 7,
                'judge_3': 6
            },
            'Lucía': {
                'judge_1': 8,
                'judge_2': 8,
                'judge_3': 8
            }
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Mateo': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Camila': {
                'judge_1': 7,
                'judge_2': 6,
                'judge_3': 7
            },
            'Santiago': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 8
            },
            'Lucía': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            }
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {
                'judge_1': 7,
                'judge_2': 8,
                'judge_3': 7
            },
            'Mateo': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 8
            },
            'Camila': {
                'judge_1': 8,
                'judge_2': 7,
                'judge_3': 9
            },
            'Santiago': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 6
            },
            'Lucía': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 9
            }
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 7,
                'judge_2': 6,
                'judge_3': 7
            },
            'Camila': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 8
            },
            'Santiago': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 7
            },
            'Lucía': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 8
            }
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {
                'judge_1': 9,
                'judge_2': 8,
                'judge_3': 9
            },
            'Mateo': {
                'judge_1': 8,
                'judge_2': 9,
                'judge_3': 8
            },
            'Camila': {
                'judge_1': 7,
                'judge_2': 7,
                'judge_3': 7
            },
            'Santiago': {
                'judge_1': 9,
                'judge_2': 9,
                'judge_3': 9
            },
            'Lucía': {
                'judge_1': 8,
                'judge_2': 8,
                'judge_3': 7
            }
        }
    }
    ]
    tabla = {
        'Valentina' : {'puntaje' : 0, 'rondas_ganadas' : 0, 'mejor_ronda' : 0, 'promedio' : 0},
        'Mateo' : {'puntaje' : 0, 'rondas_ganadas' : 0, 'mejor_ronda' : 0, 'promedio' : 0},
        'Camila' : {'puntaje' : 0, 'rondas_ganadas' : 0, 'mejor_ronda' : 0, 'promedio' : 0},
        'Santiago' : {'puntaje' : 0, 'rondas_ganadas' : 0, 'mejor_ronda' : 0, 'promedio' : 0},
        'Lucía' : {'puntaje' : 0, 'rondas_ganadas' : 0, 'mejor_ronda' : 0, 'promedio' : 0}
        }
    for indice,tema in enumerate(rounds) :
        ronda = {
        'Valentina' : 0 ,
        'Mateo' : 0 ,
        'Camila' : 0 ,
        'Santiago' : 0 ,
        'Lucía' : 0
        }
        print(f'Ronda {indice + 1} - {tema['theme']}')
        for participante in ronda :
            ronda[participante] += sum(tema['scores'][participante].values())
        for indice,participante in enumerate(sorted(ronda, key=ronda.get, reverse=True)): 
            if indice == 0 :
                print(f'Ganador : {participante} ({ronda[participante]} PTS)')
                tabla[participante]['rondas_ganadas'] += 1
            else :
                print(f'Puesto {indice + 1} : {participante} ({ronda[participante]} PTS)')
            tabla[participante]['puntaje'] += ronda[participante]
            if tabla[participante]['mejor_ronda'] < ronda[participante] :
                tabla[participante]['mejor_ronda'] = ronda[participante]
    for participante in tabla :
        tabla[participante]['promedio'] = tabla[participante]['puntaje'] / 5
    print(f'{"Cocinero":<12}{"Puntaje":<10}{"Rondas Ganadas":<18}{"Mejor ronda":<15}{"Promedio":<10}')
    print('--------------------------------------------------------------------')
    for participante in sorted(tabla, key=lambda x: tabla[x]['puntaje'], reverse=True):
        print(f'{participante:<12}{tabla[participante]["puntaje"]:<10}{tabla[participante]["rondas_ganadas"]:<18}{tabla[participante]["mejor_ronda"]:<15}{tabla[participante]["promedio"]:<10}')