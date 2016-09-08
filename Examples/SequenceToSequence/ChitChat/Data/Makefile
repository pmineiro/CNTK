.SECONDARY:

ntk:=80
maxsid:=10000000
tcut:=6

datafile:=4-turn.fortraining.filtered.2015-01-01...2015-06-30.convos.txt

all: shortchitchat3tri.train shortchitchat3tri.valid shortchitchat3tri.test 

shortvocab3tri: $(datafile) chitchat2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortchitchat3tri.%: $(datafile) chitchat2trainv3trishort shortvocab3tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > /data/chitchat/$@
	ln -sf /data/chitchat/$@ .
