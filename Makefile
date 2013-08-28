all: bootstrap buildout setup_project

bootstrap:
	python bootstrap.py -v 2.1.1

buildout:
	./bin/buildout

setup_project:
	./setup_project.sh

distclean: clean

clean:
	rm -rf .installed.cfg bin develop-eggs eggs parts
	find . -name '*.pyc' | xargs rm
	
