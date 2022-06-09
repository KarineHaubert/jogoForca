from funcoes import boasVindas, limparTela, continuar, mostraPalavra, desenhaForca, ganhou, perdeu

dicas = list
palavraChave = list
chutes = list
erros = int
acertos = int
mensagem = str
desafiante = str
competidor = str
perdedor = str
vencedor = str
enforca = int


def main():
    global desafiante, competidor, perdedor, vencedor, enforca

    def startGame():
        global dicas, palavraChave, chutes, erros, acertos, mensagem, desafiante, competidor, perdedor, vencedor, enforca

        dicas = []
        palavraChave = []
        chutes = []
        erros = 5
        acertos = 0
        mensagem = ''
        desafiante = ''
        competidor = ''
        perdedor = ''
        vencedor = ''
        enforca = 0

    def palpitar():
        global erros, acertos, mensagem, enforca
        palpite = str(input('Digite uma letra ou uma palavra:').upper())
        if len(palpite) > 1:
            if palpite == ''.join(palavraChave):
                acertos = len(palavraChave)
                return
            else:
                mensagem = '{} não é a palavra correta.'.format(palpite)
                erros -= 1
                enforca += 1
                return
        if palpite in chutes:
            mensagem = 'Você ja chutou essa letra'
            return
        else:
            chutes.append(palpite)

        if palpite in palavraChave:
            acertos += 1
            mensagem = 'A letra {} faz parte da palavra!'.format(palpite.upper())
        else:
            erros -= 1
            enforca += 1
            mensagem = 'A letra {} não faz parte da palavra!'.format(palpite.upper())
        print('\n')
            

    
    startGame();
    limparTela();
    boasVindas();

    desafiante = str(input('Digite o nome do desafiante:'));
    competidor = str(input('Digite o nome do competidor:'));

    if len(desafiante) and len(competidor) >= 3: 
        limparTela();

        palavraChave = list(str(input('Digite a palavra chave:').upper()));
        
        while len(palavraChave) < 3:
            palavraChave = list(str(input('Palavra chave deve conter no mínimo 3 caracteres:').upper()));
        
        dicas.append(str(input('Primeira dica:').upper()));
        dicas.append(str(input('Segunda dica:').upper()));
        dicas.append(str(input('Terceira dica:').upper()));

        limparTela()
        while acertos < len(palavraChave) and erros > 0:

            print('{}'.format(mensagem));
            desenhaForca(enforca);
            mostraPalavra(palavraChave, chutes);
            print('\nAcertos:{}'.format(acertos));
            print('Chances restantes:{}'.format(erros));
            print('(1) Para jogar');
            print('(2) Para receber uma dica');
            opcao = int

            try:
                opcao = int(input('Sua opção:'))
                if opcao == 1:
                    limparTela()
                    palpitar()
                elif opcao == 2:
                    if len(dicas) > 0:
                        limparTela()
                        print(dicas[0])
                        dicas.pop(0)
                    if len(dicas) > 0:
                        print('Você so tem mais {} dicas'.format(len(dicas)))
                    else:
                        print('Você não tem mais dicas!')
                    palpitar()
            except:
                limparTela()
                print('Opção invalida!')
            limparTela()

        if erros == 0:
            perdedor = 'Competidor ' + competidor.capitalize()
            vencedor = 'Desafiante ' + desafiante.capitalize()
            perdeu(palavraChave)

        elif acertos == len(palavraChave):
            perdedor = 'Desafiante ' + desafiante.capitalize()
            vencedor = 'Competidor ' + competidor.capitalize()
            ganhou()

        w = open('historico.txt', 'a')
        w.write('Palavra: {} - Vencedor: {}, Perdedor: {}\n'.format(''.join(palavraChave).capitalize(), vencedor, perdedor))
        w.close()
        r = open('historico.txt', 'r')
        print('Historico de partidas')
        print(r.read())
        continuar()
        print('Digite 1 para jogar novamente')
        print('Digite 2 para sair do jogo\n')
        quitGame = int
        while quitGame != 1 or quitGame != 2: 
            try:
                quitGame = int(input('Sua opção:'))
                if quitGame == 1:
                    main()
                elif quitGame == 2:
                    break
            except:
                limparTela()
                print('Opção invalida')
    else:
        print("Nomes inválidos!")
        continuar()
        main()



main()

