# Análises automatizadas de Vulnerabilidade para Sites

O site foi criado utilizando a linguagem de programação Python e o framework Flask, que é um micro-framework para criação de aplicativos web. O site é baseado em um modelo de formulário que permite que o usuário insira dados referentes à vulnerabilidade de um determinado website. Esses dados são salvos em um banco de dados SQLite para que possam ser posteriormente acessados e exibidos na página.


Os benefícios desse tipo de site incluem a possibilidade de realizar Análises de vulnerabilidade de sites de forma mais rápida e automatizada, com uma interface de usuário amigável e fácil de usar. Além disso, a capacidade de armazenar dados em um banco de dados permite que os dados sejam facilmente acessados e analisados em momentos futuros, o que é especialmente útil para análises de segurança a longo prazo .



# Tipos de Análise de Site?

1 - (Capacidade de armazenar dados em um banco de dados)

2 - (Incluem a possibilidade de realizar Análises de vulnerabilidade)

3 - (Permite que o usuário insira dados referentes à vulnerabilidade de um determinado website)



## Sobre avaliação de vunerabilidade?

O site em questão é um aplicativo web que permite aos usuários avaliar a qualidade de um determinado site, levando em consideração aspectos como SEO, vulnerabilidades, armazenamento, spam e tráfego.


Para usar o site, os usuários devem primeiro criar uma conta de usuário, que será protegida por autenticação. Uma vez autenticados, os usuários podem inserir a URL de um site que desejam avaliar, juntamente com as pontuações correspondentes para cada um dos aspectos mencionados acima. O site armazenará esses dados em um banco de dados e exibirá os resultados para o usuário.


Os usuários também podem visualizar os resultados para todos os sites avaliados, bem como os resultados individuais para um site específico, com base em seu ID exclusivo.


Além disso, a aplicação também possui recursos de segurança, como autenticação com senha e um token de autenticação OTP, para garantir que somente usuários autorizados tenham acesso aos recursos do aplicativo.


# Como usar:

Para usar o site, você precisa seguir os seguintes passos:


1) Certifique-se de ter instalado o Python em sua máquina. Você pode baixá-lo no site oficial do Python (https://www.python.org/downloads/).

  2) Instale as bibliotecas Flask, flask_otp e Werkzeug. Você pode fazer isso usando o pip (gerenciador de pacotes do Python). No terminal ou prompt de comando, execute os seguintes comandos:
  
` pip install Flask `

`  pip install flask_otp `

` pip install Werkzeug `


3)  Baixe os arquivos do projeto e coloque-os em uma pasta.

 4)   Abra o terminal ou prompt de comando e navegue até a pasta do projeto.

  5)  Digite o comando python app.py e pressione Enter.

6)   Abra o navegador e acesse o endereço http://localhost:5000/. A página de login será exibida.

 7)  Peça a senha ADM por E-mail por segurança: melkycontato50@gmail.com
 
 8)  Insira o token de autenticação OTP. Para gerar o token, você pode usar um aplicativo de autenticação OTP, como o Google Authenticator ou o Authy.

 9)   Após fazer login, você poderá ver a página principal do site.

 10)  Na página principal, você pode inserir os resultados dos testes de segurança para um determinado URL. Preencha os campos na parte inferior da página e clique em "Adicionar".

  11)  Para ver todos os resultados dos testes de segurança, clique no link "Resultados" no menu superior.

  12)  Para ver um resultado específico, clique em seu ID na lista de resultados.



Para testar o site, você pode tentar inserir resultados de teste usando URLs reais ou falsas e verificar se os resultados são exibidos corretamente na lista de resultados. Você também pode tentar fazer login com um nome de usuário ou senha incorretos e verificar se o site exibe uma mensagem de erro.






# Autor:

# Melky Correia
