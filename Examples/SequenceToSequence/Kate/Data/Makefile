.SECONDARY:

ntk:=80
maxsid:=100000000
tcut:=4

all: shortkate3tri.train shortkate3tri.valid shortkate3tri.test 

shortvocab3tri: source.txt kate2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortkate3tri.%: source.txt kate2trainv3trishort shortvocab3tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > /data/kate/$@
	ln -sf /data/kate/$@ .
