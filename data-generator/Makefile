# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 data/GenerateData.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	rm -rf *.csv

.PHONY: all venv run cleanmak