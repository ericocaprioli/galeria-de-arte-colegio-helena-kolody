# Galeria de Arte Colégio Helena Kolody
A Galeria do Colégio Helena Kolody promove apreciação cultural, fortalece habilidades sociais e estimula o pensamento crítico. É um centro de colaboração que celebra a diversidade e talento dos alunos, transcendendo disciplinas acadêmicas para estimular crescimento pessoal e coletivo.

## Instalar Dependências
Para instalar as dependências do projeto, é necessário utilizar o virtual-environment (ambiente virtual) do python. Para isso utilize o seguinte código:
```
python -m venv .venv
```
Sendo `.venv` o nome do arquivo do ambiente virtual que será criado.

É necessário ativar o ambiente virtual, para use o seguinte código:

Terminal Linux no Windows:
```
source \.venv\Scripts\Activate
```

Com ambiente virtual criado e ativo, utilizamos o seguinte código e não comprometemos o projeto com arquivos externos.
```
pip install django pillow
```

## Iniciando o servidor do Django
O Django já entrega um servidor de testes, no qual não pode ser utilizado na produção. Para iniciar utilizamos o seguinte comando:
```
python manage.py runserver
```

## Realizando as migrações
O Django possui uma técnologia que é muito comum em outras linguagens de programação, porém extremamente útil. Essa técnologia se chama ORM (Object-Relational-Manager), um banco de dados é criado apartir das models do projeto. O termo migração será muito comum nesse momento, o termo é a ação de tornar as classes models, tabelas no banco de dados. Como as migrações já foram criadas com `makemigrations` iremos apenas realiza-lás:
```
python manage.py migrate
```
Com isso não iremos mais ver aquela mensagem vermelha sobre as `unapplied migrations`.

## Adcionando um Superusuário 
Para criar usuários administradores, é necessário utilizar o seguinte comando: 
```
python manage.py createsuperuser
```
Após isso será necesspario informar uma série de informações, pressionando `enter` entre elas.
``` 
Username: admin 
```
```
 Email address: admin@example.com 
```
```
Password: **********
Password (again): *********
Superuser created successfully.
```
Concluíndo a criação do superusuário, será possível fazer login no endereço localhost:8000/admin. Assim visualizando todas as tabelas, classes models e objetos criados.
