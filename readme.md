# Jogo da Velha (Tic-Tac-Toe)

Este projeto é uma implementação do jogo da velha (Tic-Tac-Toe) em Python, desenvolvido como parte do Checkpoint 4 do curso TADS da FIAP. O jogo pode ser jogado em três modos:

Jogador X vs Jogador O - Dois jogadores humanos jogam um contra o outro.
Jogador X vs Máquina (Fácil) - Um jogador humano enfrenta uma máquina com estratégia fácil.
Jogador X vs Máquina (Difícil) - Um jogador humano enfrenta uma máquina com estratégia difícil.

# Funcionalidades

Iniciar uma nova partida com o tabuleiro 3x3.
Imprimir o tabuleiro para visualização do estado atual do jogo.
Escolher a modalidade de jogo através de um menu interativo.
Jogar contra um adversário humano ou uma máquina com dois níveis de dificuldade.
Verificar se há um vencedor ou se o jogo terminou em empate.


# Funções Principais:
inicializarTabuleiro(): Cria um tabuleiro 3x3 vazio.
imprimirTabuleiro(tabuleiro): Imprime o tabuleiro atual no console.
imprimeMenuPrincipal(): Mostra o menu principal com opções de jogo.
leiaCoordenadaLinha(tamanhoTabuleiro): Lê e valida a entrada da linha do usuário.
leiaCoordenadaColuna(tamanhoTabuleiro): Lê e valida a entrada da coluna do usuário.
imprimePontuacao(pontuacoes): Exibe a pontuação atual dos jogadores.
posicaoValida(tabuleiro, linha, coluna): Verifica se uma posição no tabuleiro é válida.
verificaVencedor(tabuleiro): Verifica se há um vencedor.
verificaVelha(tabuleiro): Verifica se o jogo terminou em empate.
jogar(tabuleiro, linha, coluna, jogador): Realiza uma jogada no tabuleiro.
jogadaUsuario(tabuleiro, jogador): Solicita uma jogada do usuário.
jogadaMaquinaFacil(tabuleiro): Realiza uma jogada da máquina no modo fácil.
jogadaVencedoraOuBloqueio(tabuleiro, jogador): Determina a jogada vencedora ou de bloqueio para a máquina.
jogadaMaquinaDificil(tabuleiro): Realiza uma jogada da máquina no modo difícil.
modoJogador(): Inicia o jogo entre dois jogadores humanos.
modoFacil(): Inicia o jogo entre um jogador humano e a máquina em modo fácil.
modoDificil(): Inicia o jogo entre um jogador humano e a máquina em modo difícil.
main(): Função principal que exibe o menu e gerencia as escolhas do usuário.
