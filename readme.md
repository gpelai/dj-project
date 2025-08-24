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
## Curriculo

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