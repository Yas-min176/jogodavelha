
visu = [0,1,2,3,4,5,6,7,8] #array responsável pelo display
jogo = [0,0,0,0,0,0,0,0,0] #array responsável por armazenar as escolhas dos jogadores
vitorias = [[1,1,1,0,0,0,0,0,0] , [0,0,0,1,1,1,0,0,0] , [0,0,0,0,0,0,1,1,1] , [1,0,0,1,0,0,1,0,0], [0,1,0,0,1,0,0,1,0] , [0,0,1,0,0,1,0,0,1] , [0,0,1,0,1,0,1,0,0] , [1,0,0,0,1,0,0,0,1] ] #array responsável por armazenar quais jogos são vitorias

def malha(): #função responsável pela exibição do display e armazenar as jogadas no array jogo
    print(
    """
    {} | {} | {}
    --------------
    {} | {} | {}
    --------------
    {} | {} | {}
    """.format(visu[0],visu[1],visu[2],visu[3],visu[4],visu[5],visu[6],visu[7],visu[8])) #formatação dos dados inseridos no display

def jogada(numero, simbolo): #Função que gerencia as jogadas
    while(1):                #loop que mantém a primeira jogada até que uma nova seja feita
        jogada = input("Jogador {}, faça sua jogada. Você é o {}\n".format(numero, simbolo))
        try:                 
            #sugestão do programa para avaliar as ações do jogador caso o loop não seja quebrado
            if int(jogada) < 0 or int(jogada) > 8: #condição em que o jogador não seleciona um espaço válido
                print("Você deve jogar um número entre 0 e 8")
            elif jogo[int(jogada)] != 0: #condição em que o espaço já foi preenchido
                print("Esse local já foi jogado alguma vez") 
            else:                 
                jogo[int(jogada)] = numero  #pegando o dado no array e jogando na variavel numero
                visu[int(jogada)] = simbolo #pegando o dado no array e jogando na varialvel simbolo
                malha() #executando a função malha e exibindo o display
                break
        except: #condição em que não foi inserido um número
            print("Você deve escrever um NUMERO!")
    
    return verificaVitoria(jogo) #após a jogada é verificado qual o resultado do jogo atual

def verificaVitoria(jogo): #função que analisa cada possibilidade de vitória ou velha e compara com o jogo atual
    for vitoria in vitorias:
        valoresMalha = []
        for val in range(0, 9):
            if vitoria[val] != 0:
                valoresMalha.append(jogo[val])
        if 0 in valoresMalha: #condição em que não houve resultado ainda
            pass
        elif 1 in valoresMalha and 2 in valoresMalha: #condição que impede erro no programa
            pass
        elif 1 in valoresMalha: #condição em que o jogador 1 venceu
            print("jogador 1 ganhou")
            return True
        elif 2 in valoresMalha: #condição em que o jogador 2 venceu
            print("jogador 2 ganhou")
            return True

    if not 0 in jogo: #verificação se o jogo não reconheceu nenhuma vitoria e todos os espaços estão preenchidos
        print("DEU VELHA")
        return True

    return False

malha() #exibição do display para jogada

while(0 in jogo): #loop que mantém o jogo como aberto até que existam espaços vazios e nenhuma vitoria
    if jogada(1,'O') : break
    if jogada(2,'x'): break