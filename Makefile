build:
	@python3 setup.py bdist_wheel

clean:
	@rm -rf build/ dist/ pilkommedia.egg-info/ .eggs/

upload:
	@python3 -m twine upload dist/*
