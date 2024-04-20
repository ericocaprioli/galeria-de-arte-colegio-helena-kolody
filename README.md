# Galeria de Arte Colégio Helena Kolody
A Galeria do Colégio Helena Kolody promove apreciação cultural, fortalece habilidades sociais e estimula o pensamento crítico. É um centro de colaboração que celebra a diversidade e talento dos alunos, transcendendo disciplinas acadêmicas para estimular crescimento pessoal e coletivo.

## Instalar Dependências
Para instalar as dependências do projeto, é necessário utilizar o virtual-environment (ambiente virtual) do python. Para isso utilize o seguinte código:
```
python -m venv .venv
```
Sendo `.venv` o nome do arquivo do ambiente virtual que será criado.

É necessário ativar o ambiente virtual, para use o seguinte código:
Windows:
```
\.venv\Scripts\Activate
```
Terminal Linux no Windows:
```
source \.venv\Scripts\Activate
```
Terminal Linux:
```
source \.venv\bin\Activate
```

Com ambiente virtual criado e ativo, utilizamos o seguinte código e não comprometemos o projeto com arquivos externos.
```
pip install django pillow
```

## Resolvendo o problema com o PowerShell
No PowerShell pode ocorrer um erro ao ativar o ambiente virtual. Vamos resolver o problema com o powershell. Primeiramente iremos visualizar qual a política de execução do seu powershell, use o comando:
```
Get-ExecutionPolicy
```
Caso o terminal informe como `Restricted`, altere para `Bypass` com o seguinte comando e tente repetir o processo da página 3:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Iniciando o servidor do Django
O Django já entrega um servidor de testes, no qual não pode ser utilizado na produção. Para iniciar utilizamos o seguinte comando:
```
python manage.py runserver
```
