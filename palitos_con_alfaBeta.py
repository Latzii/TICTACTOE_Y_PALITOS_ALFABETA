def minimax(palitos_restantes, turno_max, memorizacion):
    # Si no hay más palitos, el jugador que juega pierde.
    if palitos_restantes <= 0:
        return 1 if turno_max else -1
    # Si la jugada ya está memorizada, devolver el valor memorizado.
    if (palitos_restantes, turno_max) in memorizacion:  #Memorizacion sirve para que almacene la mejor jugada y no la este consultando a cada rato.
        return memorizacion[(palitos_restantes, turno_max)]
    # Calcular el valor de cada jugada posible y guardar el mejor valor.
    if turno_max:
        mejor_valor = float('-inf')
        for i in range(1, 4):
            mejor_valor = max(mejor_valor, minimax(palitos_restantes - i, not turno_max, memorizacion))
    else:
        mejor_valor = float('inf')
        for i in range(1, 4):
            mejor_valor = min(mejor_valor, minimax(palitos_restantes - i, not turno_max, memorizacion))
            # Memorizar el mejor valor para la jugada actual y devolverlo.
    memorizacion[(palitos_restantes, turno_max)] = mejor_valor
    return mejor_valor

def IA_movimiento(palitos_restantes): # Inicializar variables para buscar el mejor movimiento.
    mejor_movimiento = None
    mejor_valor = float('-inf')
    memorizacion = {}
    # Calcular el valor de cada movimiento posible y guardar el mejor valor y movimiento.
    for i in range(1, 4):
        valor = minimax(palitos_restantes - i, False, memorizacion)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = i
    return mejor_movimiento

def jugar_partida():
    palitos_restantes = int(input('¿Cuántos palitos hay en la partida? '))
    primer_jugador = input('¿Quién inicia la partida? (1: IA, 2: Jugador) ')
    while primer_jugador != '1' and primer_jugador != '2':
        primer_jugador = input('Por favor ingresa un número válido (1 o 2): ')
    turno_IA = primer_jugador == '1'
    while palitos_restantes > 0:
        print('Quedan ' + str(palitos_restantes) + ' palitos: ' + ' I ' * palitos_restantes)
        if palitos_restantes == 1:
            print('¡Gana el jugador 2!' if turno_IA else '¡Gana el jugador IA!')
            break
        if turno_IA:
            IA_mov = IA_movimiento(palitos_restantes)
            print('El jugador IA toma ' + str(IA_mov) + ' palitos')
            palitos_restantes -= IA_mov
        else:
            jugador_movimiento = int(input('Jugador 2: ¿Cuántos palitos tomas? (1-3) '))
            while jugador_movimiento < 1 or jugador_movimiento > 3:
                jugador_movimiento = int(input('Por favor ingresa un número válido (1-3): '))
            palitos_restantes -= jugador_movimiento
        turno_IA = not turno_IA

jugar_partida()