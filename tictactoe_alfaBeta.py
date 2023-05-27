import math

def print_tablero(tablero):
    print('  1   2   3')
    print(' ---|---|---')
    for i in range(3):
        print(f'{i+1} {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]}')
        if i != 2:
            print(' ---|---|---')

def movimientos_posibles(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                movimientos.append((i, j))
    return movimientos

def gano_jugador(tablero, jugador):
    # Revisar filas
    for fila in tablero:
        if fila == [jugador, jugador, jugador]:
            return True
    # Revisar columnas
    for j in range(3):
        if tablero[0][j] == jugador and tablero[1][j] == jugador and tablero[2][j] == jugador:
            return True
    # Revisar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def juego_terminado(tablero):
    return gano_jugador(tablero, 'X') or gano_jugador(tablero, 'O') or len(movimientos_posibles(tablero)) == 0

def minimax(tablero, profundidad, es_maximizador, alfa, beta):
    if juego_terminado(tablero) or profundidad == 0:
        if gano_jugador(tablero, 'O'):
            return 1
        elif gano_jugador(tablero, 'X'):
            return -1
        else:
            return 0

    if es_maximizador:
        mejor_valor = -math.inf
        for movimiento in movimientos_posibles(tablero):
            tablero[movimiento[0]][movimiento[1]] = 'O'
            valor = minimax(tablero, profundidad - 1, False, alfa, beta)
            tablero[movimiento[0]][movimiento[1]] = ' '
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, valor)
            if beta <= alfa:
                break # poda beta
        return mejor_valor
    else:
        mejor_valor = math.inf
        for movimiento in movimientos_posibles(tablero):
            tablero[movimiento[0]][movimiento[1]] = 'X'
            valor = minimax(tablero, profundidad - 1, True, alfa, beta)
            tablero[movimiento[0]][movimiento[1]] = ' '
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, valor)
            if beta <= alfa:
                break # poda alfa
        return mejor_valor
    
def IA_movimiento(tablero):
    mejor_movimiento = None
    mejor_valor = -math.inf
    for movimiento in movimientos_posibles(tablero):
        tablero[movimiento[0]][movimiento[1]] = 'O'
        valor = minimax(tablero, 5, False, -math.inf, math.inf)
        tablero[movimiento[0]][movimiento[1]] = ' '
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
    return mejor_movimiento

def jugar_partida():
    tablero = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    turno_jugador = True
    while not juego_terminado(tablero):
        print_tablero(tablero)
        print()
        if turno_jugador:
            fila = int(input('Ingresa la fila (1-3): ')) - 1
            columna = int(input('Ingresa la columna (1-3): ')) - 1
            while (fila < 0 or fila > 2 or columna < 0 or columna > 2 or tablero[fila][columna] != ' '):
                print('Movimiento inválido. Inténtalo de nuevo.')
                fila = int(input('Ingresa la fila (1-3): ')) - 1
                columna = int(input('Ingresa la columna (1-3): ')) - 1
            tablero[fila][columna] = 'X'
        else:
            print('Turno de la IA...')
            movimiento_IA = IA_movimiento(tablero)
            tablero[movimiento_IA[0]][movimiento_IA[1]] = 'O'
        turno_jugador = not turno_jugador

    print_tablero(tablero)
    if gano_jugador(tablero, 'X'):
        print('¡Gana el jugador!')
    elif gano_jugador(tablero, 'O'):
        print('¡Gana la IA!')
    else:
        print('Empate.')

jugar_partida()
