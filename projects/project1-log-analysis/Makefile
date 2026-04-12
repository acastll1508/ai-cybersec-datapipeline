# Variable del interprete
PYTHON := .venv/bin/python


# Crear entorno
venv:
	python -m venv .venv


# Activar entorno 
activate:
	source .venv/bin/activate


# Instalar todo
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements/base.txt
	$(PYTHON) -m pip install -r requirements/dev.txt
	$(PYTHON) -m pip install -r requirements/viz.txt
	$(PYTHON) -m pip install -r requirements/notebook.txt


# Validar entorno completo
check:
	$(PYTHON) -m pip check
	$(PYTHON) -m pytest


# Freeze controlado
freeze: 
	$(PYTHON) -m pip freeze > requirements/lock.txt


# Ver paquetes instalados
list:
	$(PYTHON) -m pip list



# Testing
test:
	$(PYTHON) -m pytest



# Ejecutar notebook
notebook:
	$(PYTHON) -m notebook


# Registrar Kernel(ajustar nombre según proyecto en este archivo)
kernel:
	$(PYTHON) -m ipykernel install --user --name=project1-env


# Limpiar entorno
clean:
	rm -rf .venv
	

