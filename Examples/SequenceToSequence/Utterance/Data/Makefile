
ntk:=80
maxsid:=1000000
tcut:=6

all: $(foreach split,train test valid,shortutt6tri.$(split))

shortvocab6tri: UtteranceLabels.tsv utterance2trainv6trishort
	iconv -f utf-16 -t utf-8 $< | perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) > /dev/null

shortutt6tri.%: UtteranceLabels.tsv utterance2trainv6trishort shortvocab6tri
	iconv -f utf-16 -t utf-8 $< | perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) > /data/utterance/$@
	ln -sf /data/utterance/$@ .

