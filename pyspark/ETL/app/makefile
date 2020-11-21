build:
	rm -rf ./deploy && mkdir ./deploy
	cp ./main.py ./deploy
	cp ./conf.json ./deploy
	zip -r deploy/jobs.zip jobs
	pip3 install -r $(PWD)/requirement.txt -t ./deploy/libs
	cd ./deploy/libs && zip -r -D ../libs.zip .
