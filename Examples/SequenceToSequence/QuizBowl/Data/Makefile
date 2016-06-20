.SECONDARY:

SCRIPTDIR:=$(HOME)/src/msr_intern2016/scripts/
MYDIR=$(shell pwd)

all: quizbowl.train quizbowl.test quizbowl.dev

quizbowl.sent: question_data/questions.csv csv2sent
	perl ./csv2sent $< > $@

quizbowl.coarse.%: quizbowl.sent
	(cd $(SCRIPTDIR); python ./get_coarse_words.py $(MYDIR)/$< $(MYDIR)/$@ $*)

quizbowl.multi.train: question_data/questions.csv quizbowl.coarse.0 quizbowl.coarse.1 coarse2cntk
	perl ./coarse2cntk train $< > $@

quizbowl.multi.%: question_data/questions.csv quizbowl.coarse.0 quizbowl.coarse.1 coarse2cntk quizbowl.multi.train
	perl ./coarse2cntk $* $< > $@

quizbowl.train: question_data/questions.csv csv2cntk
	perl ./csv2cntk train $< > $@

quizbowl.%: question_data/questions.csv csv2cntk quizbowl.train
	perl ./csv2cntk $* $< > $@

question_data/questions.csv: question_data.tar.gz
	tar -zxf question_data.tar.gz question_data/questions.csv
	touch $@

question_data.tar.gz:
	wget https://cs.umd.edu/~miyyer/data/question_data.tar.gz
