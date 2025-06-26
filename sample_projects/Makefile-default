SAMPLE_PROJECTS := $(shell ls -F sample_projects/ | grep -E "/" | sed -e s/\\///)
# sample projects 	
list-projects:
	@echo $(SAMPLE_PROJECTS)
	
%:
	cp ./sample_projects/$*/custom_modules/* ./custom_modules/
	rm -fr main.cpp README.md model.yml Makefile
	cp ./sample_projects/$*/main.cpp ./main.cpp
	cp ./sample_projects/$*/README.md ./README.md
	cp ./sample_projects/$*/model.yml ./model.yml
	cp ./sample_projects/$*/Makefile .
	rm -fr config/*
	cp -r ./sample_projects/$*/config/* ./config/
	rm -fr scripts/*
	cp ./sample_projects/$*/scripts/* ./scripts/
