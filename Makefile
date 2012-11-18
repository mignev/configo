help:
	@echo "   install      to install Configo"
	@echo "   uninstall    to uninstall Configo"
	@echo "   clean        to clean build files"

install:
	@echo "Installing"
	@sudo python setup.py install --record installed_files.txt

uninstall: clean
	@cat installed_files.txt | xargs sudo rm -rf
	@sudo rm installed_files.txt

clean:
	@sudo rm -rf Configo.egg*
	@sudo rm -rf dist
	@sudo rm -rf build
	@find . -name *.pyc -type f -exec rm {} \;
