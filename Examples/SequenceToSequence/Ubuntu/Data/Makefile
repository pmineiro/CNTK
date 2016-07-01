.SECONDARY:

all: ubuntu.train ubuntu.valid ubuntu.test

shortubuntu.train: train.csv ubuntu2trainv1short
	perl ./$(word 2,$^) train $< > $@

shortubuntu.%: %.csv ubuntu2trainv1short
	perl ./$(word 2,$^) $* $< > $@

ubuntu.train: train.csv ubuntu2trainv1
	perl ./$(word 2,$^) train $< > $@

ubuntu.%: %.csv ubuntu2trainv1
	perl ./$(word 2,$^) $* $< > $@
