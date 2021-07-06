# Projeto Social 
Um projeto social sem fins lucrativos, objetivo e que todos os envolvidos no projeto assimilem de forma ampla conceitos simples e complexos do desenvolvimento web com Python / Django.
Projeto para fixação do conteúdo e preparaçao para o mercado de trabalho pois usamos desenvolvimento ágil de software. 


### TODOs
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [ ] Model users
- [ ] - Cadastro usando Django-Allauth
- [ ] - Envio de e-mail para confirmação de cadastro
- [ ] - Recuperação de senha por e-mail
- [ ] Model perfil
- [ ] - Cadastro de perfil
- [ ] - Seleção do tipo de perfil
- [ ] - Seleção de interesse para algorítimo de feed
- [ ] - Alinhamento das ONG's conforme interesse
- [ ] Model feed

### Tutorial para iniciantes
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
git clone https://github.com/JonathaCnB/projeto-social.git
```

- Para **Windows**:

```
cd projeto-social
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
```

- Para **Linux**:

```
cd ecommerce
python3.9 -m venv venv
. venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
```

- Para **Mac**

```
cd ecommerce
python -m venv venv
. venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
```

Pronto!
