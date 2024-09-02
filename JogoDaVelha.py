"""
*********************************************************************
 ** FIAP **/
/** TADS - 2o semestre de 2024 **/
/** <Fernando Almeida> **/
/** **/
/** Checkpoint 4 I **/
/** Arquivo: <ErikJenniferJulio> **/
/** **/
/** <RM554854 Erik Paschoalatto dos Santos> **/
/** <RM557137 Jennifer Eduarda Vieira Daleffi> **/
/** <RM557298 Julio Cesar Conceição Rodrigues> **/
/** **/
/** <data da entrega 01/09/2024> **/
/*********************************************************************/
"""
 
import random

def inicializarTabuleiro():
    # define o tamanho padrao do tabuleiro como 3x3
    tamanhoTabuleiro = 3
    
    # cria uma lista vazia que ira conter as linhas do tabuleiro
    tabuleiro = []

    # loop para criar cada linha do tabuleiro
    for linha in range(tamanhoTabuleiro):
        # cria uma lista que representa uma linha com três espaços vazios
        linha = [' '] * tamanhoTabuleiro
        
        # adiciona a linha criada a lista do tabuleiro
        tabuleiro.append(linha)

    # retorna o tabuleiro completo 
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
    # obtém o tamanho do tabuleiro (número de linhas)
    tamanhoTabuleiro = len(tabuleiro)
 
    # loop para percorrer por cada linha do tabuleiro
    for linha in range(tamanhoTabuleiro):
        # junta os elementos da linha em uma string separada por " | " e imprime
        print(f"{' | '.join(tabuleiro[linha])}")
       
        # imprime uma linha de separação entre as linhas do tabuleiro, menos após a última linha
        if linha <= tamanhoTabuleiro - 1:
            print("-" * 9)

def imprimeMenuPrincipal():
    print("Escolha a modalidade desejada: ")
    print("1 - JogadorX vs JogadorO")
    print("2 - JogadorX vs maquina (Fácil)")
    print("3 - JogadorX vs maquina (Difícil)")
    print("4 - Sair")

def leiaCoordenadaLinha(tamanhoTabuleiro):
    # inicia um loop infinito para garantir que a entrada do usuário seja válida
    while True:
        # pede ao usuário que insira o número da linha desejada
        linha = int(input("Linha desejada (1, 2, 3): "))
        
        # ajusta o índice da linha para a base 0 (subtrai 1)
        linha = linha - 1

        # verifica se a linha está dentro dos limites do tabuleiro
        if linha in range(tamanhoTabuleiro):
            # se for válida, retorna a linha ajustada (base 0)
            return linha
        else:
            # se a linha não estiver dentro dos limites, exibe uma mensagem de erro
            print("Essa linha não existe")

def leiaCoordenadaColuna(tamanhoTabuleiro):
    # inicia um loop infinito para garantir que a entrada do usuário seja válida
    while True:
        # solicita ao usuário que insira o número da coluna desejada
        coluna = int(input("Coluna desejada (1, 2, 3): "))
        
        # ajusta o índice da coluna para a base 0 (subtrai 1)
        coluna = coluna - 1

        # verifica se a coluna está dentro dos limites do tabuleiro
        if coluna in range(tamanhoTabuleiro):
            # se for válida, retorna a coluna ajustada (base 0)
            return coluna
        else:
            # se a coluna não estiver dentro dos limites, exibe uma mensagem de erro
            print("Essa coluna não existe")


def imprimePontuacao(pontuacoes):
    # cria uma lista para armazenar as strings de pontuação dos jogadores
    pontuacaoJogadores = []

    # verifica se há uma pontuação registrada para o Jogador X
    if 'jogadorX' in pontuacoes:
        # adiciona a pontuação do Jogador X a lista de jogadores
        pontuacaoJogadores.append(f"Jogador X: {pontuacoes['jogadorX']}")
    
    # verifica se há uma pontuação registrada para o Jogador O
    if 'jogadorO' in pontuacoes:
        # adiciona a pontuação do Jogador O a lista de jogadores
        pontuacaoJogadores.append(f"Jogador O: {pontuacoes['jogadorO']}")
    
    # verifica se há uma pontuação registrada para a maquina
    if 'maquina' in pontuacoes:
        # adiciona a pontuação da maquina a lista de jogadores
        pontuacaoJogadores.append(f"maquina: {pontuacoes['maquina']}")

    # imprime a pontuação total, juntando as entradas da lista com " | " como separador
    print("Pontuação - " + " | ".join(pontuacaoJogadores))



def posicaoValida(tabuleiro, linha, coluna):
    # pega o tamanho do tabuleiro (número de linhas ou colunas)
    tamanhoTabuleiro = len(tabuleiro)

    # verifica se a linha está dentro dos limites válidos
    if linha >= 0 and linha < tamanhoTabuleiro:
        # verifica se a coluna está dentro dos limites válidos
        if coluna >= 0 and coluna < tamanhoTabuleiro:
            # verifica se a posição no tabuleiro está vazia (ou seja, ainda não foi ocupada)
            if tabuleiro[linha][coluna] == ' ':
                # se todas as condições forem atendidas, a posição é válida
                return True

    # se qualquer condição não for atendida, a posição não é válida
    return False


def verificaVencedor(tabuleiro):
    # obtém o tamanho do tabuleiro (número de linhas)
    tamanhoTabuleiro = len(tabuleiro)

    # verifica vencedor por linha
    for linha in range(tamanhoTabuleiro):
        # verifica se todos os elementos da linha são iguais e não vazios
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2]:
            if tabuleiro[linha][0] != ' ':
                # retorna o símbolo do vencedor (X ou O)
                return tabuleiro[linha][0]

    # Verifica vencedor por coluna
    for coluna in range(tamanhoTabuleiro):
        # verifica se todos os elementos da coluna são iguais e não vazios
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            if tabuleiro[0][coluna] != ' ':
                # retorna o símbolo do vencedor (X ou O)
                return tabuleiro[0][coluna]

    # verifica vencedor na diagonal principal (esquerda superior para direita inferior)
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[0][0] != ' ':
            # retorna o símbolo do vencedor (X ou O)
            return tabuleiro[0][0]

    # verifica vencedor na diagonal secundaria (direita superior para esquerda inferior)
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        if tabuleiro[0][2] != ' ':
            # retorna o símbolo do vencedor (X ou O)
            return tabuleiro[0][2]

     # se não houver vencedor, retorna None
    return None

def verificaVelha(tabuleiro):
    # pega o tamanho do tabuleiro (número de linhas ou colunas)
    tamanhoTabuleiro = len(tabuleiro)

    # percorre todas as linhas do tabuleiro
    for linha in range(tamanhoTabuleiro):
        # percorre todas as colunas da linha atual
        for coluna in range(tamanhoTabuleiro):
            # verifica se a posição atual está vazia
            if tabuleiro[linha][coluna] == ' ':
                # se encontrar uma posição vazia, retorna False (jogo não terminou)
                return False

    # se não encontrar nenhuma posição vazia, retorna True (velha/empate)
    return True

def jogar(tabuleiro, linha, coluna, jogador):
    # define uma mensagem padrao indicando que a posição é inválida
    resultado = "Posição inválida."

    # verifica se a posição (linha, coluna) é válida para uma jogada
    if posicaoValida(tabuleiro, linha, coluna):
        # se a posição for válida, coloca o símbolo do jogador na posição especificada
        tabuleiro[linha][coluna] = jogador
        # atualiza a mensagem de resultado para indicar que o movimento foi realizado com sucesso
        resultado = "Movimento realizado com sucesso."
    
    # retorna a mensagem de resultado (indica se o movimento foi realizado ou se a posição era inválida)
    return resultado

def jogadaUsuario(tabuleiro, jogador):
    # pega o tamanho do tabuleiro (número de linhas ou colunas)
    tamanhoTabuleiro = len(tabuleiro)

    # loop para solicitar ao usuário uma jogada até que uma posição válida seja fornecida
    while True:
        # solicita ao usuário a coordenada da linha desejada
        linha = leiaCoordenadaLinha(tamanhoTabuleiro)
        # solicita ao usuário a coordenada da coluna desejada
        coluna = leiaCoordenadaColuna(tamanhoTabuleiro)
        
        # verifica se a posição fornecida é válida para uma jogada
        if posicaoValida(tabuleiro, linha, coluna):
            # se a posição for válida, sai do loop
            break
        else:
            # se a posição for inválida, informa ao usuário e solicita uma nova jogada
            print("Posição inválida.")

    # realiza a jogada do usuário na posição fornecida
    jogar(tabuleiro, linha, coluna, jogador)
    
    # armazena as coordenadas da jogada em uma tupla
    coordenadaJogada = (linha, coluna)

    # retorna as coordenadas da jogada realizada
    return coordenadaJogada



def jogadaMaquinaFacil(tabuleiro):
    # pega o tamanho do tabuleiro (número de linhas ou colunas)
    tamanhoTabuleiro = len(tabuleiro)

    # seleciona aleatoriamente uma linha e uma coluna dentro dos limites do tabuleiro
    linha = random.randint(0, tamanhoTabuleiro - 1)
    coluna = random.randint(0, tamanhoTabuleiro - 1)

    # verifica se a posição selecionada é válida
    while not posicaoValida(tabuleiro, linha, coluna):
        # se a posição não for válida, seleciona novas coordenadas aleatórias
        linha = random.randint(0, tamanhoTabuleiro - 1)
        coluna = random.randint(0, tamanhoTabuleiro - 1)

    # realiza a jogada da maquina na posição selecionada
    jogar(tabuleiro, linha, coluna, 'O')

    # armazena as coordenadas da jogada em uma tupla
    coordenadaJogada = (linha, coluna)

    # retorna as coordenadas da jogada realizada
    return coordenadaJogada



def jogadaVencedoraOuBloqueio(tabuleiro, jogador):
    # pega o tamanho do tabuleiro (número de linhas ou colunas)
    tamanho = len(tabuleiro)

    # percorre todas as posições do tabuleiro para verificar possíveis jogadas
    for linha in range(tamanho):
        for coluna in range(tamanho):
            # verifica se a posição atual é válida para uma jogada
            if posicaoValida(tabuleiro, linha, coluna):
                # simula a jogada do jogador na posição
                tabuleiro[linha][coluna] = jogador
                # verifica se a jogada resultaria em uma vitória
                if verificaVencedor(tabuleiro) == jogador:
                    # se a jogada resulta em vitória, desfaz a jogada e retorna a posição
                    tabuleiro[linha][coluna] = ' '
                    return (linha, coluna)
                # desfaz a jogada, pois não resultou em vitória
                tabuleiro[linha][coluna] = ' '
    
    # retorna None se nenhuma jogada de vitória ou bloqueio foi encontrada
    return None



def jogadaMaquinaDificil(tabuleiro):
    # realiza jogada seguindo o raciocinio da jogada perfeita na seguinte ordem de prioridade:

    # 1. Centro: Jogue no centro se estiver disponível
    if posicaoValida(tabuleiro, 1, 1):
        jogar(tabuleiro , 1, 1, 'O')
        return

    # 2. Ganhar: Se a máquina tem duas peças numa linha, ponha a terceira
    jogada = jogadaVencedoraOuBloqueio(tabuleiro, 'O')
    if jogada:
        jogar(tabuleiro, jogada[0], jogada[1], 'O')
        return

    # 3. Bloquear: Se o oponente tiver duas peças em linha, ponha a terceira para bloqueá-lo
    jogada = jogadaVencedoraOuBloqueio(tabuleiro, 'X')
    if jogada:
        jogar(tabuleiro, jogada[0], jogada[1], 'O')
        return

    # 4. Canto vazio: Jogue num canto que esteja vazio, preferencialmente com o canto inverso também vazio
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    cantos_disponiveis = [canto for canto in cantos if posicaoValida(tabuleiro, canto[0], canto[1])]
    
    # verificar se há um canto com seu canto inverso vazio
    for canto in cantos_disponiveis:
        inverso = (2 - canto[0], 2 - canto[1])
        if posicaoValida(tabuleiro, inverso[0], inverso[1]):
            jogar(tabuleiro, canto[0], canto[1], 'O')
            return
    
    # se nenhum canto com o inverso disponível, jogar em qualquer canto vazio
    if cantos_disponiveis:
        jogar(tabuleiro, cantos_disponiveis[0][0], cantos_disponiveis[0][1], 'O')
        return

    # 5. borda vazia: Jogue em uma borda que esteja vazia
    bordas = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for linha, coluna in bordas:
        if posicaoValida(tabuleiro, linha, coluna):
            jogar(tabuleiro, linha, coluna, 'O')
            return


def modoJogador():
    # define os símbolos dos jogadores e inicializa o turno para o primeiro jogador (X)
    jogadores = ['X', 'O']
    turno = 0
    # inicializa o dicionário de pontuações para os jogadores X e O
    pontuacoes = {'jogadorX': 0, 'jogadorO': 0}

    # loop principal do jogo que continua enquanto nenhum jogador alcançar 3 vitórias
    while pontuacoes['jogadorX'] < 3 and pontuacoes['jogadorO'] < 3:
        # inicializa um novo tabuleiro para cada partida
        tabuleiro = inicializarTabuleiro()
        
        # loop para a jogabilidade da partida atual
        while True:
            # imprime o tabuleiro atual
            imprimirTabuleiro(tabuleiro)
            # informa de quem é a vez de jogar
            print(f"É a vez do jogador {jogadores[turno]}")
            # obtém a jogada do jogador atual
            jogadaUsuario(tabuleiro, jogadores[turno])

            # verifica se há um vencedor após a jogada
            vencedor = verificaVencedor(tabuleiro)
            if vencedor:
                # se houver um vencedor, exibe a mensagem e atualiza a pontuação
                print(f"Jogador {vencedor} venceu!")
                pontuacoes[f'jogador{vencedor}'] += 1
                break

            # verifica se o tabuleiro está cheio (empate)
            if verificaVelha(tabuleiro):
                # se for um empate, exibe a mensagem e troca o turno
                print("Empate!")
                turno = 1 - turno 
                break

            # alterna o turno entre os jogadores
            turno = 1 - turno
        
        # imprime as pontuações atualizadas após o término da partida
        imprimePontuacao(pontuacoes)
    
    # exibe uma mensagem quando a partida termina (quando um jogador atinge 3 vitórias)
    print("Partida encerrada!")



def modoFacil():
    # define os símbolos dos jogadores e inicializa o dicionário de pontuações
    jogador = 'X'
    maquina = 'O'
    pontuacoes = {'jogadorX': 0, 'maquina': 0}

    # continua jogando enquanto nenhum dos jogadores alcançar 3 vitórias
    while pontuacoes['jogadorX'] < 3 and pontuacoes['maquina'] < 3:
        # inicializa o tabuleiro para uma nova partida
        tabuleiro = inicializarTabuleiro()
        while True:
            # exibe o tabuleiro atual
            imprimirTabuleiro(tabuleiro)
            # informa que é a vez do usuário e solicita a jogada
            print("Sua vez!")
            jogadaUsuario(tabuleiro, jogador)
            # verifica se o usuário venceu após a jogada
            if verificaVencedor(tabuleiro) == jogador:
                print("Você venceu!")
                pontuacoes['jogadorX'] += 1
                break
            # verifica se o jogo terminou em empate (tabuleiro cheio)
            elif verificaVelha(tabuleiro):
                print("Empate!")
                break
            # realiza a jogada da maquina no modo fácil
            jogadaMaquinaFacil(tabuleiro)
            # verifica se a maquina venceu após a jogada
            if verificaVencedor(tabuleiro) == maquina:
                print("maquina venceu!")
                pontuacoes['maquina'] += 1
                break
        # exibe a pontuação atual após o término da partida
        imprimePontuacao(pontuacoes)
    # informa o encerramento da partida após atingir o número necessário de vitórias
    print("Partida encerrada!")



def modoDificil():
    # define os símbolos dos jogadores e inicializa o dicionário de pontuações
    jogador = 'X'
    maquina = 'O'
    pontuacoes = {'jogadorX': 0, 'maquina': 0}

    # continua jogando enquanto nenhum dos jogadores alcançar 3 vitórias
    while pontuacoes['jogadorX'] < 3 and pontuacoes['maquina'] < 3:
        # inicializa o tabuleiro para uma nova partida
        tabuleiro = inicializarTabuleiro()
        while True:
            # exibe o tabuleiro atual
            imprimirTabuleiro(tabuleiro)
            # informa que é a vez do usuário e solicita a jogada
            print("Sua vez!")
            jogadaUsuario(tabuleiro, jogador)
            # verifica se o usuário venceu após a jogada
            if verificaVencedor(tabuleiro) == jogador:
                print("Você venceu!")
                pontuacoes['jogadorX'] += 1
                break
            # verifica se o jogo terminou em empate (tabuleiro cheio)
            elif verificaVelha(tabuleiro):
                print("Empate!")
                break
            # realiza a jogada da maquina no modo difícil
            jogadaMaquinaDificil(tabuleiro)
            # verifica se a maquina venceu após a jogada
            if verificaVencedor(tabuleiro) == maquina:
                print("maquina venceu!")
                pontuacoes['maquina'] += 1
                break
        # exibe a pontuação atual após o término da partida
        imprimePontuacao(pontuacoes)
    # informa o encerramento da partida após atingir o número necessário de vitórias
    print("Partida encerrada!")



def main():
    # loop principal do programa que continuará rodando até que o usuário escolha sair
    while True:
        # exibe o menu principal com as opções disponíveis
        imprimeMenuPrincipal()
        # recebe a opção escolhida pelo usuário
        escolha = input("Escolha uma opção: ")
        
        # executa a ação correspondente a escolha do usuário
        if escolha == '1':
            # inicia o modo de jogo entre dois jogadores humanos
            modoJogador()
        elif escolha == '2':
            # inicia o modo de jogo onde o jogador humano enfrenta a maquina em modo fácil
            modoFacil()
        elif escolha == '3':
            # inicia o modo de jogo onde o jogador humano enfrenta a maquina em modo difícil
            modoDificil()
        elif escolha == '4':
            # encerra o programa se o usuário escolher a opção de sair
            break
        else:
            # informa ao usuário que a opção escolhida é inválida
            print("Opção inválida.")

# chama a função main para iniciar o programa
main()