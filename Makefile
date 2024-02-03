style:
	flake8 .

types:
	mypy sportinj

check:
    make -j3 style types
