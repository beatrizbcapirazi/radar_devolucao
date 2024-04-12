import telebot
from telebot import types
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

# Configurando Telegram
chave_api = os.environ.get('CHAVE_API')
bot = telebot.TeleBot(chave_api)

# Acesso ao Sheets
credenciais_acesso = os.environ.get('GOOGLE')
conta = ServiceAccountCredentials.from_json_keyfile_name(credenciais_acesso)
api = gspread.authorize(conta)
planilha = api.open_by_key('1oX79tHXEPgW-9ZNVXRN4HtGKj5IWQI5d2diTX5LdUsY')
sheet = planilha.worksheet("Robo")

# Lista de todos os estados
estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
           "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
           "RS", "RO", "RR", "SC", "SP", "SE", "TO", "BR"]

# Obter todos os dados da planilha como uma lista de listas
dados_planilha = sheet.get_all_values()

# Dicionário para mapear códigos de estado para mensagens correspondentes
mensagens_por_estado = {}

# Iterando sobre cada estado na lista de estados
for estado in estados:
    # Encontrando o índice da linha correspondente ao estado na planilha
    # Obtendo a linha correspondente aos dados do estado
    index = estados.index(estado) + 1
    linha = dados_planilha[index]

    # Extraindo os dados da linha
    casos_devolucao = linha[1]

    # Mensagem para cada estado
    mensagem_ac = f"O Acre registrou {dados_planilha[1][2]} casos de devolução de 2020 a 2024, de acordo com os dados divulgados pelo Tribunal de Justiça do Estado do Acre via Lei de Acesso à Informação (LAI)."
    mensagem_al = f"{dados_planilha[2][2]} sobre os casos casos de devolução de Alagoas. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://e-sic.al.gov.br/"
    mensagem_ap = f"{dados_planilha[3][2]} sobre os casos casos de devolução do Amapá. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: http://esic.ap.gov.br/"
    mensagem_am = f"O Amazonas registrou {dados_planilha[4][2]} casos de devolução, segundo dados divulgados pelo Tribunal de Justiça do Estado do Amazonas via pedido de Lei de Acesso à Informação (LAI)."
    mensagem_ba = f"{dados_planilha[5][2]} sobre os casos de devolução da Bahia. Em resposta a o pedidode LAI, a Ouvidoria pediu que eu entrasse em contato com a Comissão Estadual Judiciária de Adoção Internacional (CEJAI-BA) no dia 04 de março. No dia 07, a instituição respondeu que o assunto não era de sua competência, fornecendo o contato de e-mail da Coordenadoria da Infância e Juventude (CIJ). O-mail fornecido não respondeu a demanda. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://ouvidoria.tjba.jus.br/#/ouvidoria/manifestacao/3"
    mensagem_ce = f"O Ceará registrou {dados_planilha[6][2]} casos de devolução, segundo dados divulgados pelo Tribunal de Justiça do Ceará via pedido de Lei de Acesso à Informação (LAI)."
    mensagem_df = f"O Distrito Federal registrou {dados_planilha[7][2]} casos de devolução de 2015 a 2018, de acordo com dados divulgados pelo Tribunal de Justiça do Distrito Federal e dos Territórios via pedido de Lei de Acesso à Informação (LAI)."
    mensagem_es = f"{dados_planilha[8][2]} sobre os casos de devolução no Espírito Santo. No dia 20 de março, a instituição informou que não existe atualmente no SNA ferramenta disponível, para os usuários, que permita extrair dados referentes à devoluções em processo de adoção, orientando a entrar em contato com o Conselho Nacional de Justiça (CNJ). Após esclarecer que o CNJ também havia sido contatado e a ideia era entender o cenário também de cada estado, não houve mais resposta. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse:https://www.tjes.jus.br/portal-transparencia/ouvidoria/sic/"
    mensagem_go = f"{dados_planilha[9][2]} sobre os casos de devolução em Goiás. Em 4 de março, a 1ª Escrivania Juizado da Infância e Juventude afirmou são raríssimos casos de devolução de crianças/adolescentes após adoção em Goiânia  e há muitos anos eles não tenho conhecimento de devoluções. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://goias.gov.br/controladoria/acesso-a-informacao/"
    mensagem_ma = f"{dados_planilha[10][2]} sobre os casos de devolução no Maranhão.Em 8 de abril, o Tribunal de Justiça do Maranhão enviou o relatório de inspeção no Sistema Nacional de Adoção e Acolhimento (SNA), de 2022, afirmando que não houve nenhum registro de devolução no estado durante o estágio de convivência. Segundo a entidade, este é o dado mais atual que a entidade possuo."
    mensagem_mt = f"{dados_planilha[11][2]} sobre os casos de devolução no Mato Grosso. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://clickjudapp.tjmt.jus.br/ouvidoria"
    mensagem_ms = f"{dados_planilha[12][2]} sobre os casos de devolução no Mato Grosso do Sul. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://sti.tjms.jus.br/confluence/pages/viewpage.action?pageId=181606643"
    mensagem_mg = f"Minas Gerais registrou {dados_planilha[13][2]} casos de devolução, segundo dados divulgados pela Justiça de 1º grau do Poder Judiciário de Minas Gerais via pedido de Lei de Acesso à Informação (LAI)."
    mensagem_pa = f"{dados_planilha[14][2]} sobre os casos de devolução no Pará. Em 20 de março, o Tribunal de Justiça do Pará afirmou que não foram encontrados códigos específicos (classes, assuntos e movimentos) nas Tabelas Processuais Unificadas do Conselho Nacional de Justiça sobre a demanda formulada. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://apps.tjpa.jus.br/ouvidoria/"
    mensagem_pb = f"{dados_planilha[15][2]} sobre os casos de devolução na Paraíba. Segundo o Tribunal de Justiça da Paraíba, a instituição não possui condições de prestar as informações requeridas, uma vez que no sistema que temos acesso ao Sistema Nacional de Adoção e Acolhimento (SNA), não há emissão de relatórios sobre casos de devoluções. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://www.tjpb.jus.br/transparencia/acesso-a-informacao/lei-de-acesso-a-informacao"
    mensagem_pr = f"{dados_planilha[16][2]} sobre os casos de devolução no Paraná. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://www.tjpr.jus.br/acesso-a-informacao"
    mensagem_pe = f"{dados_planilha[17][2]} sobre os casos de devolução em Pernambuco. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://portal.tjpe.jus.br/web/transparencia/pedidos-de-informacao"
    mensagem_pi = f"O Piauí registrou {dados_planilha[18][2]} casos de devolução, segundo dados divulgados pelo Tribunal de Justiça do Piauí via pedido de Lei de Acesso à Informação (LAI)."
    mensagem_rj = f"O Rio de Janeiro registrou {dados_planilha[19][2]} casos de devolução, segundo dados divulgados pelo Tribunal de Justiça do Estado do Rio de Janeiro via pedido de Lei de Acesso à Informação (LAI). Vale apontar que o TJ do estado afirmou que o quantitativo de 550 crianças/adolesscentes foram levantados desde a criação do Sistema Nacional de Adoção e Acolhimento (SNA), em 2019. Segundo eles, o sistema só disponibiliza a opção CANCELADA, que abrange também outros critérios como: desistência, falecimento, maioridade e inativação. "
    mensagem_rn = f"O Rio Grande do Norte registrou {dados_planilha[20][2]} casos de devolução entre 2018 e 2023, segundo dados divulgados pela Coordenadoria Estadual da Infância e da Juventude do Estado do Rio Grande do Norte via Lei de Acesso à Informação (LAI)."
    mensagem_rs = f"{dados_planilha[21][2]} sobre os casos de devolução no Rio Grande do Sul. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://www.tjrs.jus.br/novo/institucional/transparencia/ouvidoria/"
    mensagem_ro = f"{dados_planilha[22][2]} sobre os casos de devolução em Rondônia. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://www.tjro.jus.br/mn-sist-ouvidoria"
    mensagem_rr = f"{dados_planilha[23][2]} sobre os casos de devolução em Roraima. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse:https://www.tjrr.jus.br/index.php/servico-de-informacoes-ao-cidadao"
    mensagem_sc = f"Santa Catarina registrou {dados_planilha[24][2]} casos de devolução de 2016 a 2017, segundo dados divulgados pelo Tribunal de Justiça de Santa Catarina via Lei de Acesso à Informação (LAI)."
    mensagem_sp = f"{dados_planilha[25][2]} sobre os casos de devolução em São Paulo informou não ter estes dados no momento, mas adiantou que está em curso no TJSP uma pesquisa sobre esse tema. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acesse: https://www.tjsp.jus.br/CanaisAtendimentoRelacionamento/SIC"
    mensagem_se = f"{dados_planilha[26][2]} sobre os casos de devolução em Sergipe. Em 12 de abril, a instituição afirmou ter solicitado os dados para o SNA, mas não possuem acesso. Segundo eles, a instituição solicitou, via e-mail, a inclusão desse parâmetro de pesquisa e fornecimento de dados via SNA"
    mensagem_to = f"{dados_planilha[27][2]} sobre os casos de devolução no Tocantins. Para fazer um pedido de Lei de Acesso à Informação (LAI) sobre o assunto ao estado acess :https://sei.tjto.jus.br/sei/modulos/tjto/ouvidoria/"
    mensagem_br = f"O Brasil registrou {dados_planilha[28][2]} casos de devolução após o trânsito em julgado, ou seja, quando o processo de adoção já foi concluído e a guarda definitiva do menor foi concedida.Segundo a lei, a adoção é irrevogável e, portanto, devolver a criança adotiva é considerado abandoná-la, da mesma forma como ocorre com um filho biológico. O retorno da criança é previsto na lei apenas no estágio de convivência, durante o qual os pretendentes à adoção têm a guarda provisória da criança."
    
    # Adicionando as mensagens ao dicionário mensagens_por_estado
    mensagens_por_estado["AC"] = mensagem_ac
    mensagens_por_estado["AL"] = mensagem_al
    mensagens_por_estado["AP"] = mensagem_ap
    mensagens_por_estado['AM'] = mensagem_am
    mensagens_por_estado['BA'] = mensagem_ba
    mensagens_por_estado['CE'] = mensagem_ce
    mensagens_por_estado['DF'] = mensagem_df
    mensagens_por_estado['ES'] = mensagem_es
    mensagens_por_estado['GO'] = mensagem_go
    mensagens_por_estado['MA'] = mensagem_ma
    mensagens_por_estado['MT'] = mensagem_mt
    mensagens_por_estado['MS'] = mensagem_ms
    mensagens_por_estado['MG'] = mensagem_mg
    mensagens_por_estado['PA'] = mensagem_pa
    mensagens_por_estado['PB'] = mensagem_pb
    mensagens_por_estado['PR'] = mensagem_pr
    mensagens_por_estado['PE'] = mensagem_pe
    mensagens_por_estado['PI'] = mensagem_pi
    mensagens_por_estado['RJ'] = mensagem_rj
    mensagens_por_estado['RN'] = mensagem_rn
    mensagens_por_estado['RS'] = mensagem_rs
    mensagens_por_estado['RO'] = mensagem_ro
    mensagens_por_estado['RR'] = mensagem_rr
    mensagens_por_estado['SC'] = mensagem_sc
    mensagens_por_estado['SP'] = mensagem_sp
    mensagens_por_estado['SE'] = mensagem_se
    mensagens_por_estado['TO'] = mensagem_to
    mensagens_por_estado["BR"] = mensagem_br

# Função para enviar o teclado inline
def enviar_inline_keyboard(chat_id, texto_opcao, opcoes):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for option in opcoes:
        markup.add(*[types.InlineKeyboardButton(text=opt["text"],
                   callback_data=opt["callback_data"]) for opt in option])
    bot.send_message(chat_id, texto_opcao, reply_markup=markup)

# Responder o callback
@bot.callback_query_handler(func=lambda call: call.data in mensagens_por_estado)
def callback_query(call):
    estado = call.data
    mensagem = mensagens_por_estado.get(estado)
    bot.send_message(call.message.chat.id, mensagem)

# Responder ao comando
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    user = mensagem.from_user
    if user.last_name:
        nome_completo = f"{user.first_name} {user.last_name}"
    else:
        nome_completo = user.first_name
    bot.send_message(mensagem.chat.id,
                     f'''
Olá, {nome_completo}. Convencionou-se chamar de "devolução de crianças e jovens adotados" o processo de retorno do menor aos abrigos após a conclusão do processo legal de adoção e a concessão da guarda definitiva aos pais. É sabido que o termo "devolver" é comumente aplicado a objetos, documentos e trocas monetárias, não a pessoas. No entanto, infelizmente, ocorrem devoluções de crianças adotadas mesmo após a finalização do processo de adoção e a concessão da guarda definitiva, o que contraria o artigo 39 do Estatuto da Criança e do Adolescente (ECA).

De acordo com a lei, a adoção é um ato irrevogável e, portanto, devolver uma criança adotada é considerado abandono, equiparado ao abandono de um filho biológico. Portanto, trata-se de um ato ilegal.

O objetivo do Radar da Devolução é coletar dados tanto sobre as devoluções que ocorrem após o término do processo legal, quanto aquelas que acontecem durante o período de convivência. Durante o estágio de convivência, os pretendentes à adoção têm a guarda provisória da criança, e a lei prevê o retorno da criança ao abrigo em determinadas circunstâncias.

É importante ressaltar que os dados sobre este assunto são de difícil acesso, especialmente porque há pouco tempo que começaram a ser coletados pelas Varas da Infância, Tribunais de Justiça e pelo Conselho Nacional de Justiça (CNJ). Devido a essa dificuldade de acesso e à falta de padronização na coleta de dados, pode haver distorções nos números e estes podem não refletir totalmente a realidade das devoluções no país.''')


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    user = mensagem.from_user
    if user.last_name:
        nome_completo = f"{user.first_name} {user.last_name}"
    else:
        nome_completo = user.first_name
    bot.send_message(mensagem.chat.id,
                     f"Olá, {nome_completo}. Não. Segundo a lei, a adoção é irrevogável e, portanto, devolver a criança adotiva é considerado abandoná-la, da mesma forma como ocorre com um filho biológico. O retorno da criança é previsto na lei apenas no estágio de convivência, durante o qual os pretendentes à adoção têm a guarda provisória da criança.")


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    user = mensagem.from_user
    if user.last_name:
        nome_completo = f"{user.first_name} {user.last_name}"
    else:
        nome_completo = user.first_name

    texto_opcao = f"{nome_completo}, escolha o estado para verificar as devoluções:"

    # Iterar sobre cada estado na lista de estados
    opcoes = []
    for estado in estados:
        # Encontrar o índice da linha correspondente ao estado na planilha
        # Adicionando 1 porque o cabeçalho está na primeira linha
        index = estados.index(estado) + 1
        # Obtendo a linha correspondente aos dados do estado
        linha = dados_planilha[index]

        # Extraindo os dados da linha
        # Supondo que o número de casos de devolução está na segunda coluna
        casos_devolucao = linha[1]

        # Mensagem para cada estado
        mensagem_estado = f"{estado} tem {casos_devolucao} casos de devolução."

        # Adicionando a opção ao teclado inline
        opcao = {"text": estado, "callback_data": estado}
        opcoes.append([opcao])

        # Adicionando a mensagem ao dicionário mensagens_por_estado
        mensagens_por_estado[estado] = mensagem_estado

    enviar_inline_keyboard(mensagem.chat.id, texto_opcao, opcoes)


@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    user = mensagem.from_user
    if user.last_name:
        nome_completo = f"{user.first_name} {user.last_name}"
    else:
        nome_completo = user.first_name
    bot.send_message(mensagem.chat.id,
                     f'''{nome_completo}, em comparação com as 4.677 adoções bem-sucedidas em 2023, o número de crianças devolvidas pode parecer irrelevante, quase insignificante, não é mesmo? Entretanto, as devoluções demonstram que há um problema. 
                     
                     Embora as devoluções sejam ilegais, a situação é ignorada pela mídia e não é abordada por uma parcela considerável do poder público. 
                     
                     Em um levantamento de estudos referentes à devolução de crianças (Devolução de crianças adotadas: uma revisão integrativa da literatura, 2017), avalia-se que não há muito material publicado sobre o assunto; no total, foram encontrados 18 artigos publicados – seguindo os critérios dos pesquisadores – entre 1988 e 2016. O ano com o maior número de publicações foi 2010, quando o ECA completou 20 anos e começou-se a discutir sua efetividade e o impacto que as medidas haviam tido na vida dos jovens. De acordo com os autores, não existem dados específicos devido à ilegalidade do ato. Há uma tentativa de abafar casos de devolução, como se eles fossem difamar a imagem construída da adoção, segundo diversos autores que tratam da temática. Tanto que alguns profissionais evitam discutir esse tema com medo de que os estigmas acerca da adoção se perpetuem. Não falar sobre o assunto evita que novos casos apareçam? A conversa, até onde se sabe, pode ser o fio condutor de mudanças.''')

# Responder para qualquer mensagem de texto enviada para robô
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    texto = """
    Olá, eu sou o Radar da Devolução. Muito prazer! Para descobrir mais sobre o cenário da devolução no Brasil, clique em um item:
    /opcao1 - Quero entender o que são as devoluções na área da adoção
    /opcao2 - As devoluções são legais?
    /opcao3 - Veja dados sobre devolução em cada estado do Brasil
    /opcao4 - Por que falar sobre a devolução?
    Responder qualquer outra coisa não vai funcionar. Por favor, escolha uma das opções listadas"""
    bot.reply_to(message, texto)


# Iniciar o bot e manter ele ativo enquanto o Collab estiver rodando
bot.polling()
