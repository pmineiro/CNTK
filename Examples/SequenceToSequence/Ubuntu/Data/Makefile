.SECONDARY:

ntk:=100
maxsid:=10000000
tcut:=2

all: shortubuntu3tri.megatrain shortubuntu3tri.valid shortubuntu3tri.test

shortvocab3tri: megatrain.csv ubuntu2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortubuntu3tri.%: %.csv ubuntu2trainv3trishort shortvocab3tri
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > /data/ubuntu-cntk-data/$@
	ln -s /data/ubuntu-cntk-data/$@ .

shortvocab3trimega: megatrain.csv ubuntu2trainv3trishort
	perl ./$(word 2,$^) preprocess $@ $(maxsid) 2 $(ntk) $(tcut) $< > /dev/null

shortubuntu3trimega.%: %.csv ubuntu2trainv3trishort shortvocab3trimega
	perl ./$(word 2,$^) $* $(word 3,$^) $(maxsid) 2 $(ntk) $(tcut) $< > /data/ubuntu-cntk-data/$@
	ln -s /data/ubuntu-cntk-data/$@ .

# dragoonz

shortvocab4: megatrain.csv ubuntu2trainv4short
	perl ./$(word 2,$^) preprocess $< > /dev/null

shortubuntu4.%: %.csv ubuntu2trainv4short shortvocab4
	perl ./$(word 2,$^) $* $< > $@

shortvocab3: megatrain.csv ubuntu2trainv3short
	perl ./$(word 2,$^) preprocess $< > /dev/null

shortubuntu3.%: %.csv ubuntu2trainv3short shortvocab3
	perl ./$(word 2,$^) $* $< > $@

vocab3: megatrain.csv ubuntu2trainv3
	perl ./$(word 2,$^) preprocess $< > /dev/null

ubuntu3.%: %.csv ubuntu2trainv3 vocab3
	perl ./$(word 2,$^) $* $< > $@

dubshortubuntu.train: train.csv ubuntu2trainv2short
	perl ./$(word 2,$^) train $< > $@

dubshortubuntu.%: %.csv ubuntu2trainv2short dubshortubuntu.train
	perl ./$(word 2,$^) $* $< > $@

shortubuntu.train: train.csv ubuntu2trainv1short
	perl ./$(word 2,$^) train $< > $@

shortubuntu.%: %.csv ubuntu2trainv1short shortubuntu.train
	perl ./$(word 2,$^) $* $< > $@

ubuntu.train: train.csv ubuntu2trainv1
	perl ./$(word 2,$^) train $< > $@

ubuntu.%: %.csv ubuntu2trainv1 ubuntu.train
	perl ./$(word 2,$^) $* $< > $@
