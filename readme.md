# BASIC DJANGO STEPS
- cria um diretório
- cria venv
	- inicia venv
	- instala django
- cria projeto django-admin startproject
	- passa usar python manage.py em vez de django-admin
- cria um root/templates/base.html para servir de base para os outros html
	- configura o templates no settings do projeto main para ser o base_dir
		- intalled_apps
		- templates/dirs/base_dir
- cria um app com python manage
	- configura urls.py do projeto main para enxergar as urls do novo app
	- cria view no app
		def > return render()
	- cria urls.py do app
		import path e views
		urlpatterns path
	- cria {nome do app}/templates/{nome do app}
		- cria index.html do web


# Models
- certificados
1. instituicao
2. titulo
3. descricao
4. data_inicio
5. data_final
6. categoria

- experiencias
1. instituicao
2. cargo
3. descricao
4. data_inicio
5. data_final
6. categoria

- skills
1. titulo
2. categoria

# Exemplos
```
primeiro_certificado = Certificados(
    instituicao = "EF",
    titulo = "EFSET Quick English Check",
    descricao= "Score: Advanced / Proficient (CEFR C1/C2)",
    data_inicio= "2024-01-01",
    data_final= "2024-01-01",
    categoria= "Idiomas"
)
```
```
primeiro_experienciaProfissional = Experiencias(
    instituicao = "Yduqs",
    cargo = "Suporte TI",
    descricao= "Suporte N1 e N2; RPA Python; Desenvolvedor SBM; Gestão e analise sobre grandes massas de tickets;",
    data_inicio= "2019-10-01",
    data_final= "2023-09-30",
    categoria= "profissional"
)
```
```
primeiro_experienciaProjeto = Experiencias(
    instituicao = "gpelai",
    cargo = "Desenvolvedor",
    descricao= "Projeto web em Django para criar e exibir currículo online, utilizando Python, HTML, CSS, Bootstrap e SQLite.",
    data_inicio= "2025-08-01",
    data_final= "2023-08-31",
    categoria= "projeto"
)
```

