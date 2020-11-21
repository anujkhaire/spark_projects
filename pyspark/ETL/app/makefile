build:
	rm -rf ./dist && mkdir ./dist
	cp ./main.py ./dist
	cp ./conf.json ./dist
	zip -r dist/jobs.zip jobs
	#zip -r dist/shared.zip shared
	#sudo docker run --rm -v $(PWD):/foo -w /foo lambci/lambda:build-python3.6 
	pip3 install -r $(PWD)/requirement.txt -t ./dist/libs
	cd ./dist/libs && zip -r -D ../libs.zip .