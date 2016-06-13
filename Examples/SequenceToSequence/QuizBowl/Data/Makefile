quizbowl.train: question_data/questions.csv csv2cntk
	perl ./csv2cntk train $< > $@

quizbowl.%: question_data/questions.csv csv2cntk quizbowl.train
	perl ./csv2cntk $* $< > $@

question_data/questions.csv: question_data.tar.gz
	tar -zxf question_data.tar.gz question_data/questions.csv
	touch $@

question_data.tar.gz:
	wget https://cs.umd.edu/~miyyer/data/question_data.tar.gz
