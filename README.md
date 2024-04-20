# Galeria de Arte Colégio Helena Kolody
A Galeria do Colégio Helena Kolody promove apreciação cultural, fortalece habilidades sociais e estimula o pensamento crítico. É um centro de colaboração que celebra a diversidade e talento dos alunos, transcendendo disciplinas acadêmicas para estimular crescimento pessoal e coletivo.

## Instalar Dependências
Para instalar as dependências do projeto, é necessário utilizar o virtual-environment (ambiente virtual) do python. Para isso utilize o seguinte código:
```
python -m venv .venv
```
Sendo `.venv` o nome do arquivo do ambiente virtual que será criado.

Com ambiente virtual criado, utilizamos o seguinte código e não comprometemos o projeto com arquivos externos.
```
pip install django pillow
```

## Iniciando o servidor do Django
O Django já entrega um servidor de testes, no qual não pode ser utilizado na produção. Para iniciar utilizamos o seguinte comando:
```
python manage.py runserver
```
