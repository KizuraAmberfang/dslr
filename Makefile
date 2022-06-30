all:	train calc

calc:
		python3 srcs/logreg_predict.py data/dataset_test.csv data/weight.csv

train:
		python3 srcs/logreg_train.py data/dataset_train.csv

desc:
		python3 srcs/describe.py data/dataset_train.csv

hist:
		python3 srcs/histogram.py data/dataset_train.csv

scatter:
		python3 srcs/scatter_plot.py data/dataset_train.csv

pair:
		python3 srcs/pair_plot.py data/dataset_train.csv

test:
		python3 srcs/test.py data/dataset_train.csv

bonus1:
		python3 srcs/histogram_bonus.py data/dataset_train.csv

bonus2:
		python3 srcs/logreg_train.py data/dataset_train.csv -v	