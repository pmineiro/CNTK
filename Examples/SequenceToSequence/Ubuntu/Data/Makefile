.SECONDARY:

ntk:=80
maxsid:=10000000
tcut:=6

all: shortubuntu3tri.megatrain shortubuntu3tri.valid shortubuntu3tri.test shortubuntu6tri.megatrain shortubuntu6tri.valid shortubuntu6tri.test

shortvocab7tri: megatrain.csv ubuntu2trainv7trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortubuntu7tri.%: %.csv ubuntu2trainv7trishort shortvocab7tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > $@

shortvocab6tri: megatrain.csv ubuntu2trainv6trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortubuntu6tri.%: %.csv ubuntu2trainv6trishort shortvocab6tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > $@

shortvocab3tri: megatrain.csv ubuntu2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortubuntu3tri.%: %.csv ubuntu2trainv3trishort shortvocab3tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > $@
