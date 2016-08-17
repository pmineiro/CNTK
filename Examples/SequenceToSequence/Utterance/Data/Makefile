
ntk:=80
maxsid:=10000000
tcut:=19

all: utt.train utt.test utt.valid

uttvocab: uttpair2train uttpairs.train.tsv.gz
	zcat $(word 2,$^) | perl ./$(word 1,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) > /dev/null

utt.%: uttpair2train uttpairs.%.tsv.gz uttvocab
	zcat $(word 2,$^) | perl ./$(word 1,$^) $* uttvocab $(maxsid) 2 $(ntk) $(tcut) > /data/utterance/$@
	ln -sf /data/utterance/$@ .

uttpairs.%.tsv.gz: makeutterancedata.py UtteranceLabels.tsv
	iconv -f utf-16 -t utf-8 $(word 2,$^) | python ./$(word 1,$^) $* | gzip > /data/utterance/$@
	ln -sf /data/utterance/$@ .
