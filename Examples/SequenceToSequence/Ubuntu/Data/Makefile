.SECONDARY:

ubuntu.train: train.csv ubuntu2trainv1
	perl ./ubuntu2trainv1 train $< > $@

ubuntu.%: %.csv ubuntu2trainv1
	perl ./ubuntu2trainv1 $* $< > $@
