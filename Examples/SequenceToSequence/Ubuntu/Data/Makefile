.SECONDARY:

all: ubuntu3.megatrain ubuntu3.valid ubuntu3.test

ubuntu3.megatrain: megatrain.csv ubuntu2trainv3
	perl ./$(word 2,$^) megatrain $< > $@

ubuntu3.%: %.csv ubuntu2trainv3 ubuntu3.megatrain
	perl ./$(word 2,$^) $* $< > $@

shortubuntu3.megatrain: megatrain.csv ubuntu2trainv3short
	perl ./$(word 2,$^) megatrain $< > $@

shortubuntu3.%: %.csv ubuntu2trainv3short shortubuntu3.megatrain
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
