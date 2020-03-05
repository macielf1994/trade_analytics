<h3>Introdução:</h3>

Primeiro projeto pessoal em <b>analise dados</b> onde ele tem como objetivo o controle financeiro e estatístico da atividade de <b>day trader</b> que já vinha estudando a alguns anos.

Os valores no exemplo abaixo são referentes a negociação do menor lote de contratos de WINFUT, nunca sofrendo alteração.

<img src=https://i.imgur.com/4XZDCs5.png width=950 height=410>

Foi necessário um pouco de programação em <b>Python</b> utilizando framework <b>Django</b>.

<b>PostgreSQL</b> para armazenamento dos dados e o <b>Power BI</b> para tratamento e visualização dos dados em dashboard.

Em busca de aprender mais sobre o framework e tentando sofisticar mais a aplicação, irei adicionar mais informações que podem ser úteis sobre trading, melhorar o visual dos painéis no Power BI, desenvolver um front-end pra aplicação e adicionar novos painéis por exemplo de desempenho no mercado de derivativos (opções).

<h3>Sobre a ideia do projeto:</h3>
  
  Um dos primeiros passos que as pessoas que iniciam no mercado financeiro tomam para operar <b>day trade</b> é aprender sobre padrões, padrões de preços, padrões de comportamento, entre outras coisas. Faz sentido, em um ambiente tão aleatório e cheio de ruídos apesar de toda a aleatoriedade há os momentos em que os mercados evoluem de alguma maneira não aleatória, e torna possível acompanhar alguns padrões que podem ser sinais significativos de compra ou venda em algum momento oportuno.
  
  Mas por trás desses padrões existem cenários de volatilidade e contexto de preço que não podem ser desconsiderados pra que esses padrões sejam realmente sinais com alguma significancia, ao invés de apenas ruído.
  
  Só que há um porém, se pegarmos livros, artigos e conteúdos da internet, encontraremos centenas desses padrões que podem ser aplicados das mais variadas maneiras, e que não se encontra com facilidade em que tipo de contexto analítico esses padrões costumam funcionar mínimamente bem.
  
  Então com tantos padrões e tantas maneiras de serem aplicados, a tentativa de estruturar uma <b>metodologia de trading</b> a fim de explorar alguma gama de vantagem é muito difícil se o processo é feito apenas por observação e intuição, sem que haja uma maneira de guardar, tratar e analisar os dados que ao longo de uma grande amostragem esses padrões costumam trazer.
  
  Foi ai que tive a ideia de buscar sofisticar minhas analises no <b>Excel</b>, tentando desenvolver dashboards pra estruturar uma <b>metodologia de trading</b> explorando o máximo possível os dados e tentando encontrar uma vantagem, acabei conhecendo as areas de <b>Business Intelligence</b> e <b>data analytics</b>.
  
  Essa ideia de montar um projeto de <b>BI</b> foi me levando a outras necessidades e curiosidades como aprender sobre <b>bancos de dados</b>, <b>frameworks</b>, <b>linguagem python</b> entre outros tecnologias que com o tempo venho buscando aprender.
  
  E a título de curiosidade, no meio desse processo acabei descobrindo algumas informações relevantes em relação ao meu desempenho no trading, que talvez não sei se conseguiria apenas por feeling. O fato de que dedicando as operações de day trade apenas as duas horas mais volateis do dia, que são a abertura do mercado a vista e do mercado americano (das 10:00 as 12:00), conseguiria otimizar o tempo gasto e os custos alcançando resultados melhores como mostra a curva de capital abaixo:
  
  <img src=https://i.imgur.com/HzNlCnx.png width=950 height=410>

<h3><b>Instalação/Configuração</b></h3>

<b>Instale o virtualenv</b>

Execute no terminal ```pip install virtualenv```

<b>Crie um ambiente virtual</b>

Execute no terminal ```virtualenv nome_do_ambiente_virtual```

<b>Inicie o ambiente virtual</b>

Execute no terminal ```./nome_do_ambiente_virtual/Scripts/activate```

<b>Abra a pasta do ambiente virtual</b>

Execute no terminal ```cd nome_do_ambiente_virtual```

<b>Faça a instalação do Django</b>

Execute no terminal ```pip install django```

<b>Baixe o repositório</b>

Execute no terminal ```git clone https://github.com/mfidelis1994/trade_analytics.git```

<b>Abra a pasta do respositório</b>

Execute no terminal ```cd trader_analytics```

<h3>Conectando o Django ao banco de dados</h3>

Você precisa ter instalado o adaptador PSYCOPG para conectar o Django ao banco de dados PostgreSQL.

Execute no terminal ```pip install psycopg2```

Na pasta 'trade_analytics' encontre o arquivo settings.py e no escopo de DATABASES, em DB_NAME altere o nome do banco de dados; em DB_USER altere o de usuario, por padrão pode deixar como postgres; em DB_PASS altere a senha.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME','trading_project'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'PORT': '5432',
        'HOST': 'localhost'
    }
}
```

Você pode baixar a última versão do gerenciador de banco de dados PostgreSQL nesse link:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Após a instalação do gerenciador de de banco de dados, abra o <b>pgAdmin 4</b>.

Irá pedir que seja cadastrado uma senha master de Admin, coloque a senha como configurado no escopo DATABASES do settings.py.
![imagem1](https://user-images.githubusercontent.com/46089953/75961675-2f07b000-5ea1-11ea-9a5e-f3baacb28852.png)

Em seguida clique em 'Servers' e digite a senha de Admin cadastrada.

![imagem2](https://user-images.githubusercontent.com/46089953/75961707-4050bc80-5ea1-11ea-956d-b5c897a5539d.png)

Crie um novo banco de dados com o mesmo nome configurado no escopo DATABASES do settings.py.

![imagem3](https://user-images.githubusercontent.com/46089953/75961735-4e064200-5ea1-11ea-9980-0794914f95ad.png)

![imagem4](https://user-images.githubusercontent.com/46089953/75961752-56f71380-5ea1-11ea-91c6-0a7c0ffd6911.png)

<h3><b>Criando as tabelas no banco de dados</b></h3>

Importando os modelos de dados pro banco de dados.

Execute no terminal ```python manage.py migrate```

![imagem5](https://user-images.githubusercontent.com/46089953/75961753-578faa00-5ea1-11ea-8868-1daf6ea0a0b3.png)

Verá que as tabelas no banco de dados foram criadas de acordo como foi programado no arquivo models.py de cada app.

![imagem6](https://user-images.githubusercontent.com/46089953/75961754-578faa00-5ea1-11ea-9e67-9e3e257a8c85.png)

Feito isso crie um super usuário.

Execute o comando ```python manage.py createsuperuser```

Digite o nome, em seguida email, senha e confirmação da senha.

Execute no terminal ```python manage.py runserver```

Abra o browser e digite o endereço local: ```127.0.0.1:8000/admin```

Digite o usuario e senha cadastrado no Django.

![imagem7](https://user-images.githubusercontent.com/46089953/75961755-58284080-5ea1-11ea-8657-02bde7a6476f.png)

Abrirá a pagina de administração do site onde pode ser cadastrados os dados das operações feitas.

![imagem8](https://user-images.githubusercontent.com/46089953/75961757-58c0d700-5ea1-11ea-8bc7-f24024f96eb2.png)

Por exemplo na seção de day trade:

![imagem9](https://user-images.githubusercontent.com/46089953/75961758-59596d80-5ea1-11ea-8757-00f02afae8af.png)

Agora pra conectar o Dashboard Trading ao banco de dados, você precisará do <b>Power BI</b> que pode ser baixado na <b>Microsoft Store</b>.

Instalado o Power BI clique em obter dados:

![imagem10](https://user-images.githubusercontent.com/46089953/75961759-59596d80-5ea1-11ea-8d70-4cfec9b600ec.png)

Na pesquisa digite postgres e em seguida clique em Banco de Dados PostgreSQL

![imagem11](https://user-images.githubusercontent.com/46089953/75961760-59596d80-5ea1-11ea-8850-014e0f767c02.png)

Servidor: 127.0.0.1
Banco de Dados: o nome dado ao banco de dados.
![imagem12](https://user-images.githubusercontent.com/46089953/75961762-59f20400-5ea1-11ea-890f-aabaf6af1fda.png)

Usuário: postgres
Senha: senha cadastrada no servidor do banco de dados.
![imagem13](https://user-images.githubusercontent.com/46089953/75961763-59f20400-5ea1-11ea-802f-b9aaef60b75a.png)

Provavelmente aparecerá uma mensagem de "Suporte a Criptografia" Clique em OK.

![imagem14](https://user-images.githubusercontent.com/46089953/75961768-5a8a9a80-5ea1-11ea-9b4a-78e34f05e3a2.png)

Importe as tabelas desejadas e o ambiente para estudos de dados em trading está configurado:

![imagem15](https://user-images.githubusercontent.com/46089953/75961750-565e7d00-5ea1-11ea-9110-06dc58083c7e.png)
