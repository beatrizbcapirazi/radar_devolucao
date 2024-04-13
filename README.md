Projeto final do 3º trimestre do Master em Jornalismo de Dados do Insper:

*Radar da devolução*

Por meio da API do Telegram, construí um robô que pudesse fornecer informações sobre a devolução de crianças adotadas no Telegram, além de conceder informações sobre o cenário da devolução em todos os estados do Brasil a partir da criação de uma base de dados própria. O objetivo do Radar da Devolução é coletar dados tanto sobre as devoluções que ocorrem após o término do processo legal quanto aquelas que acontecem durante o período de convivência. Durante o estágio de convivência, os pretendentes à adoção têm a guarda provisória da criança, e a lei prevê o retorno da criança ao abrigo em determinadas circunstâncias.

*Instalações:*

Para começar, é preciso instalar as seguintes bibliotecas de dados:

-pyTelegramBotAPI (telebot)
- gspread
- oauth2client.service_account
- oauth2client.service_account
- dotenv 
- os

Para fazer rodar, você precisará criar acesso a API do Google Sheets (o que é possível através desse link: https://developers.google.com/sheets/api/guides/concepts?hl=pt-br) para obter as suas credenciais, criar uma planilha no Google Sheets ou Excel e acessar o 'BotFather' para criar um bot do telegram (a documentação pode ser verificada neste link: https://core.telegram.org/bots/api). 

*Processo de captação de dados:*

Para começar, vasculhei todas as bases de dados públicas disponíveis para verificar se havia informações sobre a temática. Não havia, e por isso decidi construir uma base de dados própria. Parti então para os pedidos de Lei de Acesso à Informação (LAI) no Conselho Nacional de Justiça (CNJ) e nos Tribunais de Justiça de todos os 26 estados brasileiros, além do Distrito Federal.

Esse processo todo levou dois meses, sendo conduzido de fevereiro a abril — data da entrega do trabalho. A ideia é ampliar essa base de dados com o passar do tempo, tanto para aumentar o escopo de cobertura e possibilitar análises mais precisas, mas também para melhorar o desenvolvimento do Radar da Devolução com o passar do tempo e tornar estes dados acessíveis e replicáveis em outros projetos de dados. 

 Posteriormente, realizei a limpeza desses dados, e iniciei o desenvolvimento do robô no Google Colab para realizar testes e implementar a lógica do robô de forma eficaz. Com o progresso do projeto, decidi migrar todo o código para o ambiente de desenvolvimento do Visual Studio Code (VSCode) para garantir uma execução mais estável e eficiente do robô.

O ambiente do VSCode foi relevante para conseguir criar testes maiores sobre a funcionalidade do robô e verificar se o código como um todo estava funcionndo, para levar o código para o Render e outras plataformas que facilitassem o seu funcionamento sem a interferência humana. 

*Como usar?*

Para utilizar o projeto, basta acessar o @radardevolucao_bot e seguir as instruções das opções oferecidas para entender o que é a devolução e um mapeamento das informações por cada estado do Brasil. Vale destacar que este projeto é replicável, com o dicionário de estados podendo ser subtítuido por regiões municipais e as funções podendo ser ampliadas para outros usos de dados públicos.

Exemplo de uso:

![image](https://github.com/beatrizbcapirazi/radar_devolucao/assets/163068430/d45e9f91-aa03-47c3-8ce4-cc6c4da2ff2f)

Status do Projeto: O projeto ainda está em desenvolvimento e deve ser finalizado, com os dados coletados sendo abertos ainda em 2024.

Contato: Caso tenha dúvidas, sugestões ou queira contribuir com o projeto e ampliar os dados sobre essa temática no Brasil entre em contato pelo e-mail: beatriz.bcapirazi@gmail.com ou pelo Linkedin: https://www.linkedin.com/in/beatriz-capirazi/
