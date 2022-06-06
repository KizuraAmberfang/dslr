def plot_scatter(gryf, raven, huffle, slyth, label1, label2, axs):
	axs.scatter(gryf[label1], gryf[label2], color='red', alpha=0.4)
	axs.scatter(raven[label1], raven[label2], color='blue', alpha=0.4)
	axs.scatter(huffle[label1], huffle[label2], color='yellow', alpha=0.4)
	axs.scatter(slyth[label1], slyth[label2], color='green', alpha=0.4)
