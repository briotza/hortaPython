#Olá, me chamo Ciano (equipe Briotza) e seja bem vindo(a) ao meu código para o desafio do curso de férias da Facens para
#uma Horta Comunitária que desenvolvi em Python
#Meu GitHub: https://github.com/briotza
#Meu LinkedIn: https://www.linkedin.com/in/ciano-meliunas-da-silva-b013aa19b

#-------------------------------------------------------------------------------------------------------------------

#criando as listas e contadores principais
colaborador=[]
consumidor = []
resposta = 0

#contador total
QAlecrim = 0
QAlface = 0
QCebolinha = 0
QCouve = 0
QManjericao = 0
QPimenta = 0
QRucula = 0
QSalsinha = 0
QTomate = 0

#contador reservas
RAlecrim = 0
RAlface = 0
RCebolinha = 0
RCouve = 0
RManjericao = 0
RPimenta = 0
RRucula = 0
RSalsinha = 0
RTomate = 0

while resposta != 4: #menu retorna enquanto usuário não finalizar (opção 4)
    portalColaborador = False
    portalConsumidor = False

    print("Bem-vindo ao portal da Horta Comunitária") #menu principal
    print("----------------------------------------")
    print("1 - Já possuo cadastro")
    print("2 - Cadastrar-se")
    print("3 - Adm")
    print("4 - Fechar programa \n")

    resposta = int(input('Escolha uma opção: '))

    if resposta > 4: #resposta fora do menu
        print("Resposta inválida")

    if resposta == 1: #acessar perfil já cadastrado
        print("1 - Colaborador")
        print("2 - Consumidor")
        tipoCadastro = int(input('Qual portal deseja acessar? ')) #acessar perfil de colaborador ou consumidor

        if tipoCadastro == 1: #acesso colaborador
            indice = 0
            usuario = str(input("Insira seu usuário: @"))
            cont = 0
            contsenha = 0
            for i in range(len(colaborador)):  #procurar nome de usuário nos cadastros
                if usuario == colaborador[i][6]:
                    cont = 1 #encontrou
                    indice = i #marcar número do cadastro (identificador)
                    break
            if cont > 0:
                senha = str(input("Insira sua senha: "))
                if senha == colaborador[indice][7]: #se senha estiver correta
                    portalColaborador = True #iniciar login como colaborador
                else:
                    print("\nSenha Inválida\n")

            else:
                print("\nUsuário Inválido\n")

        if tipoCadastro == 2: #acesso consumidor
            indice = 0
            usuario = str(input("Insira seu usuário: @"))
            cont = 0
            contsenha = 0
            for i in range(len(consumidor)):  #procurar nome de usuário nos cadastros
                if usuario == consumidor[i][5]:
                    cont = 1 #encontrou
                    indice = i #marcar número do cadastro (identificador)
                    break
            if cont > 0:
                senha = str(input("Insira sua senha: "))
                if senha == consumidor[indice][6]: #se senha estiver correta
                    portalConsumidor = True #iniciar login como consumidor
                else:
                    print("\nSenha Inválida\n")

            else:
                print("\nUsuário Inválido\n")


    if resposta == 2: #cadastrar novo perfil
        print("1 - Colaborar")
        print("2 - Consumir")
        print("\nVocê deseja se cadastrar como colaborador ou consumidor?") #tipo de cadastro
        resposta2 = int(input("Se você já possui cadastro de colaborador e deseja consumir"
                              "\nnossos produtos, você precisa fazer os dois cadastros "))
        #pessoas que já colaboram com a horta(possuem alguma função) também podem consumir os produtos
        #se também fizerem cadastro de consumidor e marcar coleta através dele

        if resposta2 == 1: #cadastrar colaborador
            nome = str(input("Insira seu nome: "))
            cpf = input("Insira seu cpf: ")
            idade = int(input("Insira sua idade: "))
            email = str(input("Insira um e-mail para contato: "))
            bairro = str(input("Insira seu bairro: "))
            print("1 - Plantação")
            print("2 - Irrigação")
            print("3 - Colheita")
            print("4 - Distribuição")
            funcaon = int(input("Insira a função que deseja exercer: ")) #escolha da função

            if funcaon == 1: #plantação
                funcao = "plantação"
                dados = [nome, cpf, idade, email, bairro, funcao, "", ""]
                #modelo padrão de lista para plantação onde os dados podem ser modificados depois
                agosto = ["agosto 2022", 0, 0, [0],[0]]
                setembro = ["setembro 2022", 0, 0, [0],[0]]
                outubro = ["outubro 2022", 0, 0, [0],[0]]
                novembro = ["novembro 2022", 0, 0,[0],[0]]
                dezembro = ["dezembro 2022", 0, 0,[0],[0]]
                dados.insert(8, agosto)
                dados.insert(9, setembro)
                dados.insert(10, outubro)
                dados.insert(11, novembro)
                dados.insert(12, dezembro)

            if funcaon == 2: #irrigação
                contadorirri = 0
                for i in range (len(colaborador)): #conta quantas pessoas estão inscritas em irrigação
                    if colaborador[i][5] == "irrigação":
                        contadorirri = contadorirri + 1
                if contadorirri > 13: #se ultrapassar 14 cadastros em irrigação
                    print("Não há mais vagas para a função de irrigação")
                else:
                    funcao = "irrigação"
                    dados = [nome, cpf, idade, email, bairro, funcao, "", "", [""]]

                    diairrigar = ["",""]

            if funcaon == 3: #colheita
                funcao = "colheita"
                dados = [nome, cpf, idade, email, bairro, funcao, "", ""]
                # modelo padrão de lista para colheita onde os dados podem ser modificados depois
                agosto = ["agosto 2022", 0, [0]]
                setembro = ["setembro 2022", 0, [0]]
                outubro = ["outubro 2022", 0, [0]]
                novembro = ["novembro 2022", 0, [0]]
                dezembro = ["dezembro 2022", 0, [0]]
                dados.insert(8, agosto)
                dados.insert(9, setembro)
                dados.insert(10, outubro)
                dados.insert(11, novembro)
                dados.insert(12, dezembro)

            if funcaon == 4: #distribuição
                contadorirri = 0
                for i in range(len(colaborador)): #conta quantas pessoas estão inscritas em distribuição
                    if colaborador[i][5] == "distribuição":
                        contadorirri = contadorirri + 1
                if contadorirri > 13: #se ultrapassar 14 cadastros em distribuição
                    print("Não há mais vagas para a função de irrigação")
                else:
                    funcao = "distribuição"
                    # modelo padrão de lista para distribuição onde os dados podem ser modificados depois
                    dados = [nome, cpf, idade, email, bairro, funcao, "", "",[""]]

            denovo = 0
            while denovo == 0: #repete enquanto usuário digitar um user já utilizado
                user = str(input("Agora insira um nome de usuário: @"))
                contador = 0
                for i in range(len(colaborador)): #procura se já cadastraram esse user
                    if user == colaborador[i][6]: #posição 6 é, por padrão, onde o user é guardado em cadastros de colaborador
                        contador = 1 #encontrou
                        break
                if contador == 1:
                    print("\nNome de usuário já utilizado\n")
                else:
                    dados[6] = user
                    senha = str(input("Insira uma senha: ")) #cadastrar senha
                    dados[7] = senha
                    colaborador.append(dados) #perfil cadastrado
                    denovo = 1
                    print("\nUsuário cadastrado com sucesso!\n")

        if resposta2 == 2: #cadastrar consumidor
            nome = input("Insira seu nome: ")
            cpf = input("Insira seu cpf: ")
            idade = input("Insira sua idade: ")
            email = str(input("Insira um e-mail para contato: "))
            bairro = input("Insira seu bairro: ")
            dados = [nome, cpf, idade, email, bairro, "", ""] #lista padrão (consumidor) para adicionar novo usuário

            denovo = 0
            while denovo == 0: #repete enquanto usuário digitar um user já utilizado
                user = str(input("Agora insira um nome de usuário: @"))
                contador = 0
                for i in range(len(consumidor)): #procura se já cadastraram esse user
                    if user == consumidor[i][5]: #posição 5 é, por padrão, onde o user é guardado em cadastros de consumidor
                        contador = 1 #encontrou
                        break
                if contador == 1:
                    print("\nNome de usuário já utilizado\n")
                else:
                    dados[5] = user
                    senha = str(input("Insira uma senha: ")) #cadastrar senha
                    dados[6] = senha
                    consumidor.append(dados) #perfil cadastraado
                    denovo = 1
                    print("\nUsuário cadastrado com sucesso!\n")

    if resposta == 3: #modo ADM mostra todos os cadastros e número atual de produtos disponíveis e reservados
        #quais e quantos produtos cadastrados
        print(f"[Alecrim] = {QAlecrim}")
        print(f"[Alface] = {QAlface}")
        print(f"[Cebolinha] = {QCebolinha}")
        print(f"[Couve] = {QCouve}")
        print(f"[Manjericão] = {QManjericao}")
        print(f"[Pimenta] = {QPimenta}")
        print(f"[Rúcula] = {QRucula}")
        print(f"[Salsinha] = {QSalsinha}")
        print(f"[Tomate] = {QTomate}")

        #quais e quantos produtos disponíveis pra reserva
        print("reserva")
        print(f"[Alecrim] = {RAlecrim}")
        print(f"[Alface] = {RAlface}")
        print(f"[Cebolinha] = {RCebolinha}")
        print(f"[Couve] = {RCouve}")
        print(f"[Manjericão] = {RManjericao}")
        print(f"[Pimenta] = {RPimenta}")
        print(f"[Rúcula] = {RRucula}")
        print(f"[Salsinha] = {RSalsinha}")
        print(f"[Tomate] = {RTomate}")

        #todos os cadastros de moradores
        print("Cadastros")
        print(f"Colaborador: {colaborador}")
        print(f"Consumidor: {consumidor}")

    if portalColaborador == True: #portal do colaborador, caso o perfil seja de colaborador
        opc1 = 0
        while opc1 < 4:
            if colaborador[indice][5] == "plantação": #se o usuário for da plantação
                print(f"\nBem vindo, {colaborador[indice][0]}, ao seu portal da Plantação") #portal da plantação
                print("[1 - Meus dados] [2 - Meu cronograma] [3 - Meu histórico] [4 - Sair]")
                opc1 = int(input("O que deseja acessar? "))

                if opc1 == 1: #meus dados
                    print("--------Meus Dados--------")
                    print(f"Nome: {colaborador[indice][0]}")
                    print(f"Cpf: {colaborador[indice][1]}")
                    print(f"Idade: {colaborador[indice][2]}")
                    print(f"E-mail: {colaborador[indice][3]}")
                    print(f"Bairro: {colaborador[indice][4]}")
                    print(f"Usuário: @{colaborador[indice][6]}")
                    print(f"Senha: {colaborador[indice][7]}")
                    altDados = int(input("\n Deseja alterar algum dado? [1-Sim] [2-Não] "))
                    if altDados == 1: #alterar
                        print("[1 - Nome][2 - CPF][3 - Idade][4 - E-mail][5 - Bairro][6 - Usuário][7 - Senha][8 - Excluir Cadastro][9 - Cancelar]")
                        altDados2 = int(input("\n Qual dado você deseja alterar? "))
                        if altDados2 == 1: #nome
                            nome = str(input("Qual será o novo nome cadastrado? "))
                            colaborador[indice][0] = nome
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 2: #cpf
                            cpf = input("Qual será o novo cpf cadastrado? ")
                            colaborador[indice][1] = cpf
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 3: #idade
                            idade = int(input("Qual será a nova idade cadastrada? "))
                            colaborador[indice][2] = idade
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 4: #email
                            email = str(input("Qual será o novo e-mail cadastrado? "))
                            colaborador[indice][3] = email
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 5: #bairro
                            bairro = str(input("Qual será o novo bairro cadastrado? "))
                            colaborador[indice][4] = bairro
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 6: #usuario
                            user = str(input("Qual será o novo usuário cadastrado? @"))
                            cont = 0
                            for i in range(len(colaborador)): # procurar nome de usuário nos cadastros
                                if user == colaborador[i][6]:
                                    cont = 1  # encontrou
                                    break
                            if cont > 0:
                                print("Nome de usuário já utilizado")
                            else:
                                colaborador[indice][6] = user
                                print("Alteração efetuada com sucesso!")
                        if altDados2 == 7: #senha
                            senha = str(input("Qual será a nova senha cadastrada? "))
                            colaborador[indice][7] = senha
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 8: #excluir perfil
                            certeza = int(input("Tem certeza? [1 - Sim][2 - Não]")) #confirmação
                            if certeza == 1:
                                del(colaborador[indice])
                                print("Perfil excluído com sucesso!")
                                break
                            if certeza == 2:
                                print("Operação cancelada")
                    if altDados == 2: #não quer alterar dados
                        print("")

                if opc1 == 2: #meu cronograma
                    print("--------Meu Cronograma--------")
                    print("\nO que é Cronograma?") #descrição
                    print("Ao se inscrever na função de Plantação você deve definir seu cronograma, onde você escolhe 2 dias por mês "
                          "\npara se comprometer a plantar novos produtos em nossa horta. Você pode sempre alterar as datas aqui no "
                          "\nportal, porém pedimos que faça com antecedência para que possamos ter ciência dos dias que você virá. "
                          "\nAssim que você comparecer nas datas marcadas e realizar o plantio você deve acessar o portal novamente "
                          "\ne registrar o que foi plantado selecionando a opção de Histórico no menu do portal.")
                    print("OBS: Os dias não são fixos, portando você pode definir dias diferentes para cada mês, se não puder "
                          "\ncomparecer, deixar a data 0")
                    print("\n[1 - 2022]") #ano 2022
                    ano = int(input("Selecione o ano que deseja acessar: "))
                    if ano == 1:
                        print("[1 - Agosto]")
                        print("[2 - Setembro]")
                        print("[3 - Outubro]")
                        print("[4 - Novembro]")
                        print("[5 - Dezembro]")
                        print("[6 - Cancelar]")
                        mes = int(input("Selecione o mês que deseja acessar: ")) #escolha do mes
                        if mes == 1:
                            NumMes = 8
                            NomMes = "agosto"
                            DiasMes = 31
                        if mes == 2:
                            NumMes = 9
                            NomMes = "setembro"
                            DiasMes = 30
                        if mes == 3:
                            NumMes = 10
                            NomMes = "outubro"
                            DiasMes = 31
                        if mes == 4:
                            NumMes = 11
                            NomMes = "novembro"
                            DiasMes = 30
                        if mes == 5:
                            NumMes = 12
                            NomMes = "dezembro"
                            DiasMes = 31
                        if mes < 6:
                            print(f"Atualmente, as duas datas agendadas são: {colaborador[indice][NumMes][1]} "
                                  f"de {NomMes} e {colaborador[indice][NumMes][2]} de {NomMes}") #mostrar datas definidas anteriormente
                            altdatas = int(input("Deseja alterar? [1 - Sim] [2 - Não] "))
                            if altdatas == 1: #alterar
                                print(f"Selecione 2 dias de {NomMes} para agendar (1 - {DiasMes})")
                                dia1 = int(input("1º dia: ")) #primeiro dia
                                if dia1 > DiasMes: #se o dia ultrapassar o número de dias de determinado mês
                                    print("Dia inválido")
                                else:
                                    dia2 = int(input("2º dia: ")) #segundo dia
                                    if dia2 > DiasMes: #se o dia ultrapassar o número de dias de determinado mês
                                        print("Dia inválido")
                                    else:
                                        #registra
                                        colaborador[indice][NumMes][1] = dia1
                                        colaborador[indice][NumMes][3][0] = dia1
                                        colaborador[indice][NumMes][2] = dia2
                                        colaborador[indice][NumMes][4][0] = dia2

                if opc1 == 3: #meu histórico
                    print("--------Meu Histórico--------")
                    print("\nNo histórico você deve registrar as suas plantações efetuadas nas datas"
                          "\nque foram agendadas na aba Meu Cronograma. Informando o vegetal plantado,"
                          "\nquantidade e o horário aproximado.")
                    print("\n[1 - 2022]") #2022
                    ano = int(input("Selecione o ano que deseja acessar: "))
                    if ano == 1:
                        print("[1 - Agosto]")
                        print("[2 - Setembro]")
                        print("[3 - Outubro]")
                        print("[4 - Novembro]")
                        print("[5 - Dezembro]")
                        print("[6 - Cancelar]")
                        mes = int(input("Selecione o mês que deseja acessar: ")) #escolher mês
                        if mes == 1:
                            NumMes = 8
                            NomMes = "agosto"
                        if mes == 2:
                            NumMes = 9
                            NomMes = "setembro"
                        if mes == 3:
                            NumMes = 10
                            NomMes = "outubro"
                        if mes == 4:
                            NumMes = 11
                            NomMes = "novembro"
                        if mes == 5:
                            NumMes = 12
                            NomMes = "dezembro"
                        if mes < 6:
                            print(f"1 - [{colaborador[indice][NumMes][1]} de {NomMes}] ")
                            print(f"\n2 - [{colaborador[indice][NumMes][2]} de {NomMes}]") #datas que registrou no cronograma
                            registro = int(input("Em qual data gostaria de registrar: "))

                            if registro == 1:
                                tamanho = len(colaborador[indice][NumMes][3]) #indentifica tamanho do registro na data escolhida
                                data = 3
                            if registro == 2:
                                tamanho = len(colaborador[indice][NumMes][4]) #indentifica tamanho do registro na data escolhida
                                data = 4

                            if tamanho < 2: #se lista possuir menos que 2 itens, quer dizer que ainda não foi feito o registro da data
                                QProduto = int(input("Quantos TIPOS (ex: alface, tomate...) de produtos foram plantados nessa data? "))
                                for i in range (QProduto): #laço de repetição na quantidade de tipos de produtos
                                    print("[1 - Alecrim]")
                                    print("[2 - Alface]")
                                    print("[3 - Cebolinha]")
                                    print("[4 - Couve]")
                                    print("[5 - Manjericão]")
                                    print("[6 - Pimenta]")
                                    print("[7 - Rúcula]")
                                    print("[8 - Salsinha]")
                                    print("[9 - Tomate]")
                                    print("[10 - Cancelar]")
                                    produto = int(input(f"Qual o {i + 1}º produto plantado: ")) #qual produto
                                    quantidade = int(input("Quantos(exemplo: 3): ")) #quantos produtos
                                    if produto == 1:
                                        vegetal = "alecrim"
                                    if produto == 2:
                                        vegetal = "alface"
                                    if produto == 3:
                                        vegetal = "cebolinha"
                                    if produto == 4:
                                        vegetal = "couve"
                                    if produto == 5:
                                        vegetal = "manjericão"
                                    if produto == 6:
                                        vegetal = "pimenta"
                                    if produto == 7:
                                        vegetal = "rúcula"
                                    if produto == 8:
                                        vegetal = "salsinha"
                                    if produto == 9:
                                        vegetal = "tomate"
                                    if produto < 10: #se não cancelar
                                        detalhes = [vegetal, quantidade]
                                        colaborador[indice][NumMes][data].append(detalhes) #registra o que foi plantado na data escolhida
                            else:
                                print("Registro já realizado!") #registro trancado (já realizou anteriormente)
                else:
                    print("")

            if colaborador[indice][5] == "irrigação": #se colaborador for da irrigação
                print(f"\nBem vindo, {colaborador[indice][0]}, ao seu portal da Irrigação") #portal da irrigação
                print("[1 - Meus dados] [2 - Meu cronograma] [4 - Sair]")
                opc1 = int(input("O que deseja acessar? "))

                if opc1 == 1: #meus dados
                    print("--------Meus Dados--------")
                    print(f"Nome: {colaborador[indice][0]}")
                    print(f"Cpf: {colaborador[indice][1]}")
                    print(f"Idade: {colaborador[indice][2]}")
                    print(f"E-mail: {colaborador[indice][3]}")
                    print(f"Bairro: {colaborador[indice][4]}")
                    print(f"Usuário: @{colaborador[indice][6]}")
                    print(f"Senha: {colaborador[indice][7]}")
                    altDados = int(input("\n Deseja alterar algum dado? [1-Sim] [2-Não] "))
                    if altDados == 1: #alterar
                        print("[1 - Nome][2 - CPF][3 - Idade][4 - E-mail][5 - Bairro][6 - Usuário][7 - Senha][8 - Excluir Cadastro][9 - Cancelar]")
                        altDados2 = int(input("\n Qual dado você deseja alterar? "))
                        if altDados2 == 1: #nome
                            nome = str(input("Qual será o novo nome cadastrado? "))
                            colaborador[indice][0] = nome
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 2: #cpf
                            cpf = input("Qual será o novo cpf cadastrado? ")
                            colaborador[indice][1] = cpf
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 3: #idade
                            idade = int(input("Qual será a nova idade cadastrada? "))
                            colaborador[indice][2] = idade
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 4: #email
                            email = str(input("Qual será o novo e-mail cadastrado? "))
                            colaborador[indice][3] = email
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 5: #bairro
                            bairro = str(input("Qual será o novo bairro cadastrado? "))
                            colaborador[indice][4] = bairro
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 6: #usuário
                            user = str(input("Qual será o novo usuário cadastrado? @"))
                            cont = 0
                            for i in range(len(colaborador)):  # procurar nome de usuário nos cadastros
                                if user == colaborador[i][6]:
                                    cont = 1  # encontrou
                                    break
                            if cont > 0:
                                print("Nome de usuário já utilizado")
                            else:
                                colaborador[indice][6] = user
                                print("Alteração efetuada com sucesso!")
                        if altDados2 == 7: #senha
                            senha = str(input("Qual será a nova senha cadastrada? "))
                            colaborador[indice][7] = senha
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 8: #excluir perfil
                            certeza = int(input("Tem certeza? [1 - Sim][2 - Não]")) #confirmação
                            if certeza == 1:
                                del(colaborador[indice])
                                print("Perfil excluído com sucesso!")
                                break
                            if certeza == 2:
                                print("Operação cancelada")

                if opc1 == 2: #meu cronograma
                    print("--------Meu Cronograma--------")
                    print("Ao se inscrever na função de Irrigação você deve definir seu cronograma, onde você escolhe 1 dia da semana "
                          "\ne um período para se comprometer a irrigar nossa horta toda semana. Você pode sempre alterar o dia e/ou "
                            "\nperíodo aqui no portal, desde que esteja disponível. Caso não consiga comparecer, nos informe antecipadamente"                            "\n através da aba de Avisos.")

                    print("\nAtualmente seu cronograma é:")
                    print(colaborador[indice][8][0]) #cronograma atual

                    altIrri = int(input('Deseja alterar? [1 - Sim] [2 - Não] '))
                    if altIrri == 1:
                        #dias e períodos disponíveis
                        print("[1 - Domingo - Manhã(07h - 11h)] [2 - Domingo - Tarde(14h - 17h)]")
                        print("[3 - Segunda - Manhã(07h - 11h)] [4 - Segunda - Tarde(14h - 17h)]")
                        print("[5 - Terça - Manhã(07h - 11h)] [6 - Terça - Tarde(14h - 17h)]")
                        print("[7 - Quarta - Manhã(07h - 11h)] [8 - Quarta - Tarde(14h - 17h)]")
                        print("[9 - Quinta - Manhã(07h - 11h)] [10 - Quinta - Tarde(14h - 17h)]")
                        print("[11 - Sexta - Manhã(07h - 11h)] [12 - Sexta - Tarde(14h - 17h)]")
                        print("[13 - Sábado - Manhã(07h - 11h)] [14 - Sábado - Tarde(14h - 17h)]")
                        print("[15 - Cancelar]")

                        semana = int(input("Escolha um novo cronograma: "))
                        if semana == 1:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["domingo manhã"] == colaborador[i][8]:
                                  cont = 1
                                  break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["domingo manhã"]
                                print("Alteração efetuada!")
                        if semana == 2:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["domingo tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["domingo tarde"]
                                print("Alteração efetuada!")
                        if semana == 3:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["segunda manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["segunda manhã"]
                                print("Alteração efetuada!")
                        if semana == 4:
                                cont = 0
                                for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                    if ["segunda tarde"] == colaborador[i][8]:
                                        cont = 1
                                        break
                                if cont > 0:
                                    print("Dia e período já ocupado")
                                else:
                                    colaborador[indice][8] = ["segunda tarde"]
                                    print("Alteração efetuada!")
                        if semana == 5:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["terça manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["terça manhã"]
                                print("Alteração efetuada!")
                        if semana == 6:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["terça tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["terça tarde"]
                                print("Alteração efetuada!")
                        if semana == 7:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["quarta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quarta manhã"]
                                print("Alteração efetuada!")
                        if semana == 8:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["quarta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quarta tarde"]
                                print("Alteração efetuada!")
                        if semana == 9:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["quinta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quinta manhã"]
                                print("Alteração efetuada!")
                        if semana == 10:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["quinta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quinta tarde"]
                                print("Alteração efetuada!")
                        if semana == 11:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["sexta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sexta manhã"]
                                print("Alteração efetuada!")
                        if semana == 12:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["sexta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sexta tarde"]
                                print("Alteração efetuada!")
                        if semana == 13:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["sábado manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sábado manhã"]
                                print("Alteração efetuada!")
                        if semana == 14:
                            cont = 0
                            for i in range(len(colaborador)): #verifica se algum usuário já está cadastrado nesse cronograma
                                if ["sábado tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sábado tarde"]
                                print("Alteração efetuada!")
                        if semana == 15:
                            print("")

                if opc1 == 4: #finaliza
                    print("")

            if colaborador[indice][5] == "colheita": #se usuário for da colheita
                print(f"\nBem vindo, {colaborador[indice][0]}, ao seu portal da Colheita") #portal da colheita
                print("[1 - Meus dados] [2 - Meu cronograma] [3 - Meu histórico] [4 - Sair]")
                opc1 = int(input("O que deseja acessar? "))

                if opc1 == 1: #meus dados
                    print("--------Meus Dados--------")
                    print(f"Nome: {colaborador[indice][0]}")
                    print(f"Cpf: {colaborador[indice][1]}")
                    print(f"Idade: {colaborador[indice][2]}")
                    print(f"E-mail: {colaborador[indice][3]}")
                    print(f"Bairro: {colaborador[indice][4]}")
                    print(f"Usuário: @{colaborador[indice][6]}")
                    print(f"Senha: {colaborador[indice][7]}")
                    altDados = int(input("\n Deseja alterar algum dado? [1-Sim] [2-Não] "))
                    if altDados == 1:
                        print(
                            "[1 - Nome][2 - CPF][3 - Idade][4 - E-mail][5 - Bairro][6 - Usuário][7 - Senha][8 - Excluir Cadastro][9 - Cancelar]")
                        altDados2 = int(input("\n Qual dado você deseja alterar? "))
                        if altDados2 == 1: #nome
                            nome = str(input("Qual será o novo nome cadastrado? "))
                            colaborador[indice][0] = nome
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 2: #cpf
                            cpf = input("Qual será o novo cpf cadastrado? ")
                            colaborador[indice][1] = cpf
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 3: #idade
                            idade = int(input("Qual será a nova idade cadastrada? "))
                            colaborador[indice][2] = idade
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 4: #email
                            email = str(input("Qual será o novo e-mail cadastrado? "))
                            colaborador[indice][3] = email
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 5: #bairro
                            bairro = str(input("Qual será o novo bairro cadastrado? "))
                            colaborador[indice][4] = bairro
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 6: #usuário
                            user = str(input("Qual será o novo usuário cadastrado? @"))
                            cont = 0
                            for i in range(len(colaborador)):  # procurar nome de usuário nos cadastros
                                if user == colaborador[i][6]:
                                    cont = 1  # encontrou
                                    break
                            if cont > 0:
                                print("Nome de usuário já utilizado")
                            else:
                                colaborador[indice][6] = user
                                print("Alteração efetuada com sucesso!")
                        if altDados2 == 7: #senha
                            senha = str(input("Qual será a nova senha cadastrada? "))
                            colaborador[indice][7] = senha
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 8: #excluir perfil
                            certeza = int(input("Tem certeza? [1 - Sim][2 - Não]")) #certeza
                            if certeza == 1:
                                del (colaborador[indice])
                                print("Perfil excluído com sucesso!")
                                break
                            if certeza == 2:
                                print("Operação cancelada")
                    if altDados == 2:
                        print("")

                if opc1 == 2:
                    print("--------Meu Cronograma--------") #meu cronograma
                    print("\nO que é Cronograma?")
                    print(
                        "Ao se inscrever na função de Colheita você deve definir seu cronograma, onde você escolhe 1 dia por mês "
                        "\npara se comprometer a colher novos produtos em nossa horta. Você pode sempre alterar a data aqui no "
                        "\nportal, porém pedimos que faça com antecedência para que possamos ter ciência do dia que você virá. "
                        "\nAssim que você comparecer nas datas marcadas e realizar a colheita você deve acessar o portal novamente "
                        "\ne registrar o que você colheu selecionando a opção de Histórico no menu do portal.")
                    print("Os dias não são fixos, portando você pode definir dias diferentes para cada mês, se não puder "
                        "\ncomparecer, deixar a data 0")
                    print("Horários também não são fixos mas você deve comparecer entre o período de 07h a 17h")
                    print("\n[1 - 2022]") #2022
                    ano = int(input("Selecione o ano que deseja acessar: "))
                    if ano == 1:
                        print("[1 - Agosto]")
                        print("[2 - Setembro]")
                        print("[3 - Outubro]")
                        print("[4 - Novembro]")
                        print("[5 - Dezembro]")
                        print("[6 - Cancelar]")
                        mes = int(input("Selecione o mês que deseja acessar: ")) #escolher mês
                        if mes == 1:
                            NumMes = 8
                            NomMes = "agosto"
                            DiasMes = 31
                        if mes == 2:
                            NumMes = 9
                            NomMes = "setembro"
                            DiasMes = 30
                        if mes == 3:
                            NumMes = 10
                            NomMes = "outubro"
                            DiasMes = 31
                        if mes == 4:
                            NumMes = 11
                            NomMes = "novembro"
                            DiasMes = 30
                        if mes == 5:
                            NumMes = 12
                            NomMes = "dezembro"
                            DiasMes = 31
                        if mes < 6:
                            print(f"Atualmente, a data agendada é: {colaborador[indice][NumMes][1]} "
                                  f"de {NomMes}") #mostrar
                            altdatas = int(input("Deseja alterar? [1 - Sim] [2 - Não] "))
                            if altdatas == 1:
                                finalizar = 0 #repete
                                while finalizar == 0: #repete se usuário não concordar com dia
                                    print(f"Selecione 1 dia de {NomMes} para agendar (1 - {DiasMes})")
                                    dia1 = int(input("Dia: "))
                                    if dia1 > DiasMes: #se ultrapassar quantidade de dias do mês
                                        print("Dia inválido")
                                    else:
                                        contdia = 0
                                        for i in range (len(colaborador)): #verifica se a data está sendo ocupada por outro usuário
                                            if colaborador[i][5] == "colheita":
                                                if colaborador[i][NumMes][1] == dia1:
                                                    contdia = contdia + 1
                                        if contdia > 0:
                                            print(f"Outros {contdia} usuários marcaram colheita nessa data, deseja manter?")
                                            escolha = int(input("[1 - Sim] [2 - Não]"))
                                            if escolha == 1:
                                                colaborador[indice][NumMes][1] = dia1
                                                colaborador[indice][NumMes][2][0] = dia1 #registrado
                                                print(f"\nData registrada como {dia1} de {NomMes} com sucesso!")
                                                print("\nNão esqueça de comparecer no período de 07h a 17h\n")
                                                finalizar = 1 #concorda
                                        else:
                                            colaborador[indice][NumMes][1] = dia1
                                            colaborador[indice][NumMes][2][0] = dia1 #registrado
                                            print(f"\nData registrada como {dia1} de {NomMes} com sucesso!")
                                            print("\nNão esqueça de comparecer no período de 07h a 17h\n")
                                            finalizar = 1 #concorda

                if opc1 == 3:
                    print("--------Meu Histórico--------") #meu histórico
                    print("\nNo histórico você deve registrar as suas colheitas efetuadas nas datas"
                          "\nque foram agendadas na aba Meu Cronograma. Informando o vegetal colhido e "
                          "\nquantidade.")
                    print("\n[1 - 2022]") #2022
                    ano = int(input("Selecione o ano que deseja acessar: "))
                    if ano == 1:
                        print("[1 - Agosto]")
                        print("[2 - Setembro]")
                        print("[3 - Outubro]")
                        print("[4 - Novembro]")
                        print("[5 - Dezembro]")
                        print("[6 - Cancelar]")
                        mes = int(input("Selecione o mês que deseja acessar: ")) #selecione o mês
                        if mes == 1:
                            NumMes = 8
                            NomMes = "agosto"
                            DiasMes = 31
                        if mes == 2:
                            NumMes = 9
                            NomMes = "setembro"
                            DiasMes = 30
                        if mes == 3:
                            NumMes = 10
                            NomMes = "outubro"
                            DiasMes = 31
                        if mes == 4:
                            NumMes = 11
                            NomMes = "novembro"
                            DiasMes = 30
                        if mes == 5:
                            NumMes = 12
                            NomMes = "dezembro"
                            DiasMes = 31
                        if mes < 6:
                            print(f"[{colaborador[indice][NumMes][1]} de {NomMes}] ") #data definida no cronograma
                            registro = int(input("Essa é a data que gostaria de registrar? [1 - Sim] [2 - Não]: "))

                            if registro == 1: #registrar
                                tamanho = len(colaborador[indice][NumMes][2]) #conta tamanho da lista
                                if tamanho < 2: #se a lista possuir menos de 2 itens
                                    QProduto = int(input("Quantos TIPOS de produtos foram colhidos nessa data? "))
                                    for i in range(QProduto): #laço pela quantidade de tipos de produtos
                                        print("[1 - Alecrim]")
                                        print("[2 - Alface]")
                                        print("[3 - Cebolinha]")
                                        print("[4 - Couve]")
                                        print("[5 - Manjericão]")
                                        print("[6 - Pimenta]")
                                        print("[7 - Rúcula]")
                                        print("[8 - Salsinha]")
                                        print("[9 - Tomate]")
                                        print("[10 - Cancelar]")
                                        produto = int(input(f"Qual o {i + 1}º produto colhido: ")) #produto
                                        quantidade = int(input("Quantos(exemplo: 3): ")) #quantidade do produto
                                        if produto == 1:
                                            vegetal = "alecrim"
                                            QAlecrim = QAlecrim + quantidade #adiciona a quantidade do produto no contador total
                                            RAlecrim = RAlecrim + quantidade #adiciona a quantidade do produto no contador de reserva
                                        if produto == 2:
                                            vegetal = "alface"
                                            QAlface = QAlface + quantidade
                                            RAlface = RAlface + quantidade
                                        if produto == 3:
                                            vegetal = "cebolinha"
                                            QCebolinha = QCebolinha + quantidade
                                            RCebolinha = RCebolinha + quantidade
                                        if produto == 4:
                                            vegetal = "couve"
                                            QCouve = QCouve + quantidade
                                            RCouve = RCouve + quantidade
                                        if produto == 5:
                                            vegetal = "manjericão"
                                            QManjericao = QManjericao + quantidade
                                            RManjericao = RManjericao + quantidade
                                        if produto == 6:
                                            vegetal = "pimenta"
                                            QPimenta = QPimenta + quantidade
                                            RPimenta = RPimenta + quantidade
                                        if produto == 7:
                                            vegetal = "rúcula"
                                            QRucula = QRucula + quantidade
                                            RRucula = RRucula + quantidade
                                        if produto == 8:
                                            vegetal = "salsinha"
                                            QSalsinha = QSalsinha + quantidade
                                            RSalsinha = RSalsinha + quantidade
                                        if produto == 9:
                                            vegetal = "tomate"
                                            QTomate = QTomate + quantidade
                                            RTomate = RTomate + quantidade
                                        if produto < 10:
                                            detalhes = [vegetal, quantidade]
                                            colaborador[indice][NumMes][2].append(detalhes)
                                else:
                                    print("Registro já realizado!") #ja realizou registro anteriormente
                else:
                    print("")

            if colaborador[indice][5] == "distribuição": #se usuário for da distribuição
                print(f"\nBem vindo, {colaborador[indice][0]}, ao seu portal da Distribuição") #portal da distribuição
                print("[1 - Meus dados] [2 - Meu cronograma] [3 - Retirada] [4 - Sair]")
                opc1 = int(input("O que deseja acessar? "))

                if opc1 == 1: #meus dados
                    print("--------Meus Dados--------")
                    print(f"Nome: {colaborador[indice][0]}")
                    print(f"Cpf: {colaborador[indice][1]}")
                    print(f"Idade: {colaborador[indice][2]}")
                    print(f"E-mail: {colaborador[indice][3]}")
                    print(f"Bairro: {colaborador[indice][4]}")
                    print(f"Usuário: @{colaborador[indice][6]}")
                    print(f"Senha: {colaborador[indice][7]}")
                    altDados = int(input("\n Deseja alterar algum dado? [1-Sim] [2-Não] "))
                    if altDados == 1: #alterar
                        print(
                            "[1 - Nome][2 - CPF][3 - Idade][4 - E-mail][5 - Bairro][6 - Usuário][7 - Senha][8 - Excluir Cadastro][9 - Cancelar]")
                        altDados2 = int(input("\n Qual dado você deseja alterar? "))
                        if altDados2 == 1: #nome
                            nome = str(input("Qual será o novo nome cadastrado? "))
                            colaborador[indice][0] = nome
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 2: #cpf
                            cpf = input("Qual será o novo cpf cadastrado? ")
                            colaborador[indice][1] = cpf
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 3: #idade
                            idade = int(input("Qual será a nova idade cadastrada? "))
                            colaborador[indice][2] = idade
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 4: #email
                            email = str(input("Qual será o novo e-mail cadastrado? "))
                            colaborador[indice][3] = email
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 5: #bairro
                            bairro = str(input("Qual será o novo bairro cadastrado? "))
                            colaborador[indice][4] = bairro
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 6: #usuário
                            user = str(input("Qual será o novo usuário cadastrado? @"))
                            cont = 0
                            for i in range(len(colaborador)):  # procurar nome de usuário nos cadastros
                                if user == colaborador[i][6]:
                                    cont = 1  # encontrou
                                    break
                            if cont > 0:
                                print("Nome de usuário já utilizado")
                            else:
                                colaborador[indice][6] = user
                                print("Alteração efetuada com sucesso!")
                        if altDados2 == 7: #senha
                            senha = str(input("Qual será a nova senha cadastrada? "))
                            colaborador[indice][7] = senha
                            print("Alteração efetuada com sucesso!")
                        if altDados2 == 8: #excluir perfil
                            certeza = int(input("Tem certeza? [1 - Sim][2 - Não]")) #confirmação
                            if certeza == 1:
                                del (colaborador[indice])
                                print("Perfil excluído com sucesso!")
                                break
                            if certeza == 2:
                                print("Operação cancelada")
                    if altDados == 2:
                        print("")

                if opc1 == 2:
                    print("--------Meu Cronograma--------") #meu cronograma
                    print(
                        "Ao se inscrever na função de Distribuição você deve definir seu cronograma, onde você escolhe 1 dia da semana "
                        "\ne um horário para se comprometer a distribuir nossos produtos a população. Você pode sempre alterar o dia e/ou "
                        "\nperíodo aqui no portal, desde que esteja disponível.")
                    print("Você só precisa comparecer quando um consumidor marcar coleta na sua data e horário de distribuição")
                    print("\nAtualmente seu cronograma é:") #mostra o cronograma atual
                    if ["domingo manhã"] == colaborador[indice][8]:
                        print("Domingo - 08h")
                    if ["domingo tarde"] == colaborador[indice][8]:
                        print("Domingo - 17h")
                    if ["segunda manhã"] == colaborador[indice][8]:
                        print("Segunda - 08h")
                    if ["segunda tarde"] == colaborador[indice][8]:
                        print("Segunda - 17h")
                    if ["terça manhã"] == colaborador[indice][8]:
                        print("Terça - 08h")
                    if ["terça tarde"] == colaborador[indice][8]:
                        print("Terça - 17h")
                    if ["quarta manhã"] == colaborador[indice][8]:
                        print("Quarta - 08h")
                    if ["quarta tarde"] == colaborador[indice][8]:
                        print("Quarta - 17h")
                    if ["quinta manhã"] == colaborador[indice][8]:
                        print("Quinta - 08h")
                    if ["quinta tarde"] == colaborador[indice][8]:
                        print("Quinta - 17h")
                    if ["sexta manhã"] == colaborador[indice][8]:
                        print("Sexta - 08h")
                    if ["sexta tarde"] == colaborador[indice][8]:
                        print("Sexta - 17h")
                    if ["sábado manhã"] == colaborador[indice][8]:
                        print("Sábado - 08h")
                    if ["sábado tarde"] == colaborador[indice][8]:
                        print("Sábado - 17h")
                    if [""] == colaborador[indice][8]: #se ainda não definiu
                        print("Você ainda não possui cronograma definido")

                    altIrri = int(input('Deseja alterar? [1 - Sim] [2 - Não] '))
                    if altIrri == 1: #alterar
                        #opções de dias e horários
                        print("[1 - Domingo - 08h] [2 - Domingo - 17h]")
                        print("[3 - Segunda - 08h] [4 - Segunda - 17h]")
                        print("[5 - Terça - 08h] [6 - Terça - 17h]")
                        print("[7 - Quarta - 08h] [8 - Quarta - 17h]")
                        print("[9 - Quinta - 08h] [10 - Quinta - 17h]")
                        print("[11 - Sexta - 08h] [12 - Sexta - 17h]")
                        print("[13 - Sábado - 08h] [14 - Sábado - 17h]")
                        print("[15 - Cancelar]")

                        semana = int(input("Escolha um novo cronograma: "))
                        if semana == 1:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["domingo manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["domingo manhã"]
                                print("Alteração efetuada!")
                        if semana == 2:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["domingo tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["domingo tarde"]
                                print("Alteração efetuada!")
                        if semana == 3:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["segunda manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["segunda manhã"]
                                print("Alteração efetuada!")
                        if semana == 4:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["segunda tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["segunda tarde"]
                                print("Alteração efetuada!")
                        if semana == 5:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["terça manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["terça manhã"]
                                print("Alteração efetuada!")
                        if semana == 6:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["terça tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["terça tarde"]
                                print("Alteração efetuada!")
                        if semana == 7:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["quarta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quarta manhã"]
                                print("Alteração efetuada!")
                        if semana == 8:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["quarta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quarta tarde"]
                                print("Alteração efetuada!")
                        if semana == 9:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["quinta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quinta manhã"]
                                print("Alteração efetuada!")
                        if semana == 10:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["quinta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["quinta tarde"]
                                print("Alteração efetuada!")
                        if semana == 11:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["sexta manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sexta manhã"]
                                print("Alteração efetuada!")
                        if semana == 12:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["sexta tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sexta tarde"]
                                print("Alteração efetuada!")
                        if semana == 13:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["sábado manhã"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sábado manhã"]
                                print("Alteração efetuada!")
                        if semana == 14:
                            cont = 0
                            for i in range(len(colaborador)): #verificar se algum usuário já escolheu esse cronograma
                                if ["sábado tarde"] == colaborador[i][8]:
                                    cont = 1
                                    break
                            if cont > 0:
                                print("Dia e período já ocupado")
                            else:
                                colaborador[indice][8] = ["sábado tarde"]
                                print("Alteração efetuada!")
                        if semana == 15: #cancelar
                            print("")
                if opc1 == 3: #retirada
                    print("--------Retirada--------")
                    print("Nesta aba você será notificado se deverá comparecer na sua próxima data "
                          "\ncombinada, além disso, após comparecimento você deverá voltar nessa aba"
                          "\npara nos informar quantos produtos foram retirados ou descartados\n")
                    reservas = len(colaborador[indice]) - 9 #verificar quantas reservas foram feitas na sua data
                    print(f"Reservas na sua próxima data: {reservas}")
                    while reservas > 0: #laço para apresentar reservas
                        VerReservas = 8 + reservas #indice para posições da lista de reservas
                        print(f"CPF: {colaborador[indice][VerReservas][0]}")
                        print(f"Produto: {colaborador[indice][VerReservas][1]}")
                        reservas = reservas - 1

                    print("\nCaso essa data já tenha passado, nos informe quais e quantos produtos foram retirados")
                    print("Inclua também os produtos que estragaram e foram descartados")
                    informar = int(input("[1 - Sim] [2 - Não]"))
                    if informar == 1: #data ja passou
                        QProduto = int(input("Quantos TIPOS (ex: alface, tomate...)de produtos foram retirados/descartados nessa sua última data? "))
                        for i in range(QProduto): #laço a partir do número de tipos de produto
                            print("[1 - Alecrim]")
                            print("[2 - Alface]")
                            print("[3 - Cebolinha]")
                            print("[4 - Couve]")
                            print("[5 - Manjericão]")
                            print("[6 - Pimenta]")
                            print("[7 - Rúcula]")
                            print("[8 - Salsinha]")
                            print("[9 - Tomate]")
                            print("[10 - Cancelar]")
                            produto = int(input(f"Qual o {i + 1}º produto: ")) #produto
                            quantidade = int(input("Quantos(exemplo: 3): ")) #quantidade
                            if produto == 1:
                                vegetal = "alecrim"
                                QAlecrim = QAlecrim - quantidade #subtrai a quantidade de produtos retirados/descartados na data da contagem total
                            if produto == 2:
                                vegetal = "alface"
                                QAlface = QAlface - quantidade
                            if produto == 3:
                                vegetal = "cebolinha"
                                QCebolinha = QCebolinha - quantidade
                            if produto == 4:
                                vegetal = "couve"
                                QCouve = QCouve - quantidade
                            if produto == 5:
                                vegetal = "manjericão"
                                QManjericao = QManjericao - quantidade
                            if produto == 6:
                                vegetal = "pimenta"
                                QPimenta = QPimenta - quantidade
                            if produto == 7:
                                vegetal = "rúcula"
                                QRucula = QRucula - quantidade
                            if produto == 8:
                                vegetal = "salsinha"
                                QSalsinha = QSalsinha - quantidade
                            if produto == 9:
                                vegetal = "tomate"
                                QTomate = QTomate - quantidade
                        excluir = len(colaborador[indice]) - 9
                        while excluir > 0: #enquanto ainda possuir reservas na sua data
                            ExcluirReservas = 8 + excluir
                            del(colaborador[indice][ExcluirReservas]) #deleta as reservas dessa última data
                            excluir = excluir - 1

    if portalConsumidor == True: #se o usuário for consumidor
        opc1 = 0
        while opc1 < 3: #enquanto usuário não quiser sair do portal
            print(f"\nBem vindo, {consumidor[indice][0]}, ao seu portal do Consumidor") #portal do consumidor
            print("[1 - Meus dados] [2 - Marcar Coleta] [3 - Sair]")
            opc1 = int(input("O que deseja acessar? "))
            if opc1 == 1: #meus dados
                print("--------Meus Dados--------")
                print(f"Nome: {consumidor[indice][0]}")
                print(f"Cpf: {consumidor[indice][1]}")
                print(f"Idade: {consumidor[indice][2]}")
                print(f"E-mail: {consumidor[indice][3]}")
                print(f"Bairro: {consumidor[indice][4]}")
                print(f"Usuário: @{consumidor[indice][5]}")
                print(f"Senha: {consumidor[indice][6]}")
                altDados = int(input("\n Deseja alterar algum dado? [1-Sim] [2-Não] "))
                if altDados == 1:
                    print(
                        "[1 - Nome][2 - CPF][3 - Idade][4 - E-mail][5 - Bairro][6 - Usuário][7 - Senha][8 - Excluir Cadastro][9 - Cancelar]")
                    altDados2 = int(input("\n Qual dado você deseja alterar? "))
                    if altDados2 == 1: #nome
                        nome = str(input("Qual será o novo nome cadastrado? "))
                        consumidor[indice][0] = nome
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 2: #cpf
                        cpf = input("Qual será o novo cpf cadastrado? ")
                        consumidor[indice][1] = cpf
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 3: #idade
                        idade = int(input("Qual será a nova idade cadastrada? "))
                        consumidor[indice][2] = idade
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 4: #email
                        email = str(input("Qual será o novo e-mail cadastrado? "))
                        consumidor[indice][3] = email
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 5: #bairro
                        bairro = str(input("Qual será o novo bairro cadastrado? "))
                        consumidor[indice][4] = bairro
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 6: #usuário
                        user = str(input("Qual será o novo usuário cadastrado? @"))
                        cont = 0
                        for i in range(len(colaborador)):  # procurar nome de usuário nos cadastros
                            if user == colaborador[i][6]:
                                cont = 1  # encontrou
                                break
                        if cont > 0:
                            print("Nome de usuário já utilizado")
                        else:
                            colaborador[indice][6] = user
                            print("Alteração efetuada com sucesso!")
                    if altDados2 == 7: #senha
                        senha = str(input("Qual será a nova senha cadastrada? "))
                        consumidor[indice][6] = senha
                        print("Alteração efetuada com sucesso!")
                    if altDados2 == 8: #excluir perfil
                        certeza = int(input("Tem certeza? [1 - Sim][2 - Não]")) #confirmação
                        if certeza == 1:
                            del (consumidor[indice])
                            print("Perfil excluído com sucesso!")
                            break
                        if certeza == 2:
                            print("Operação cancelada")
                if altDados == 2:
                    print("")

            if opc1 == 2: #marcar coleta
                print("--------Marcar Coleta--------")
                print("\nPor meio dessa aba você consegue reservar nossos produtos que você pretende "
                      "\nadquirir de acordo com a disponibilidade de cada um. Além disso consegue marcar "
                      "\ndata e horário que irá buscar, de acordo com a disponibilidade de nossos distribuidores."
                      "\nA disponibilidade dos produtos é atualizada a cada colheita e cada reserva.")
                reserva = int(input("\nDeseja marcar uma nova reserva? [1 - Sim] [2 - Não]"))
                if reserva == 1: #nova reserva
                    agendar = 0
                    #mostra quantos produtos ainda não foram reservados
                    print(f"[1 - Alecrim ({RAlecrim} disponíveis)]")
                    print(f"[2 - Alface ({RAlface} disponíveis)]")
                    print(f"[3 - Cebolinha ({RCebolinha} disponíveis)]")
                    print(f"[4 - Couve ({RCouve} disponíveis)]")
                    print(f"[5 - Manjericão ({RManjericao} disponíveis)]")
                    print(f"[6 - Pimenta ({RPimenta} disponíveis)]")
                    print(f"[7 - Rúcula ({RRucula} disponíveis)]")
                    print(f"[8 - Salsinha ({RSalsinha} disponíveis)]")
                    print(f"[9 - Tomate ({RTomate} disponíveis)]")
                    print(f"[10 - Cancelar]")
                    print("Lembrando que o número disponível pode não ser verídico")
                    #foi criado um contador apenas para reservas pois pode ser que o número de produtos reservados
                    #não seja o mesmo que o consumidor retirou e o contador total é mais oficial
                    NRProduto = int(input("Qual produto gostaria de reservar? ")) #produto
                    if NRProduto < 10: #se não cancelar
                        QRProduto = int(input("Quantos? ")) #quantidade
                        pronto = 1
                        if NRProduto == 1:
                            if QRProduto > RAlecrim: #se a quantidade for maior que a disponível
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "alecrim" #nome produto
                                agendar = 1 #quantidade aceita
                                pronto = 0 #ativa o laço que define o agendamento
                                RAlecrim = RAlecrim - QRProduto #subtrai a quantidade dos disponiveis
                        if NRProduto == 2:
                            if QRProduto > RAlface:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "alface"
                                agendar = 1
                                pronto = 0
                                RAlface = RAlface - QRProduto
                        if NRProduto == 3:
                            if QRProduto > RCebolinha:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "cebolinha"
                                agendar = 1
                                pronto = 0
                                RCebolinha = RCebolinha - QRProduto
                        if NRProduto == 4:
                            if QRProduto > RCouve:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "couve"
                                agendar = 1
                                pronto = 0
                                RCouve = RCouve - QRProduto
                        if NRProduto == 5:
                            if QRProduto > RManjericao:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "manjericão"
                                agendar = 1
                                pronto = 0
                                RManjericao = RManjericao - QRProduto
                        if NRProduto == 6:
                            if QRProduto > RPimenta:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "pimenta"
                                agendar = 1
                                pronto = 0
                                RPimenta = RPimenta - QRProduto
                        if NRProduto == 7:
                            if QRProduto > RRucula:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "Rúcula"
                                agendar = 1
                                pronto = 0
                                RRucula = RRucula - QRProduto
                        if NRProduto == 8:
                            if QRProduto > RSalsinha:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "salsinha"
                                agendar = 1
                                pronto = 0
                                RSalsinha = RSalsinha - QRProduto
                        if NRProduto == 9:
                            if QRProduto > RTomate:
                                print("Você ultrapassou a quantidade disponível")
                            else:
                                RProduto = "tomate"
                                agendar = 1
                                pronto = 0
                                RTomate = RTomate - QRProduto
                        if pronto == 0:
                            while pronto == 0: #enquanto a coleta não for agendada
                                if agendar == 1: #quantidade aceita
                                    print("[1 - Domingo - 08h] [2 - Domingo - 17h]")
                                    print("[3 - Segunda - 08h] [4 - Segunda - 17h]")
                                    print("[5 - Terça - 08h] [6 - Terça - 17h]")
                                    print("[7 - Quarta - 08h] [8 - Quarta - 17h]")
                                    print("[9 - Quinta - 08h] [10 - Quinta - 17h]")
                                    print("[11 - Sexta - 08h] [12 - Sexta - 17h]")
                                    print("[13 - Sábado - 08h] [14 - Sábado - 17h]")
                                    print("[15 - Cancelar]")
                                    semana = int(input("Agora escolha uma data e horário para a coleta: ")) #agendar horario e data com disponibilizador
                                    if semana == 1:
                                        cont = 0
                                        for i in range(len(colaborador)): #verifica se há disponibilizador nessa data e horário
                                            if ["domingo manhã"] == colaborador[i][8]:
                                                cont = 1 #encontrou
                                                distri = i #guarda o disponibilizador
                                                break
                                        if cont < 1: #se não encontrou
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else: #se encontrou
                                            print("Coleta agendada! Compareça na horta no próximo Domingo (08h)")
                                            pronto = 1 #coleta agendada
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta) #registrar na lista do disponibilizador a reserva
                                    if semana == 2:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["domingo tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Domingo (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 3:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["segunda manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Segunda (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 4:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["segunda tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Segunda (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 5:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["terça manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Terça (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 6:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["terça tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Terça (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 7:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["quarta manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Quarta (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 8:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["quarta tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Quarta (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 9:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["quinta manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Quinta (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 10:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["quinta tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Quinta (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 11:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["sexta manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Sexta (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 12:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["sexta tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Sexta (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 13:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["sábado manhã"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Sábado (08h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 14:
                                        cont = 0
                                        for i in range(len(colaborador)):
                                            if ["sábado tarde"] == colaborador[i][8]:
                                                cont = 1
                                                distri = i
                                                break
                                        if cont < 1:
                                            print("\nNão há nenhum disponibilizador nessa data e horário\n")
                                        else:
                                            print("Coleta agendada! Compareça na horta em Sábado (17h)")
                                            pronto = 1
                                            NColeta = [consumidor[indice][1], RProduto]
                                            colaborador[distri].append(NColeta)
                                    if semana == 15: #cancelar
                                        print("")



