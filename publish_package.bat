@echo off
pipenv run python setup.py sdist
pipenv run twine upload .\dist\*
del .\dist\* /f /q