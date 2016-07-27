.SECONDARY:

ntk:=80
maxsid:=10000000
tcut:=2

all: shortubuntu3tri.megatrain shortubuntu3tri.valid shortubuntu3tri.test

shortvocab3tri: megatrain.csv ubuntu2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > $@

shortubuntu3tri.%: %.csv ubuntu2trainv3trishort shortvocab3tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > $@
