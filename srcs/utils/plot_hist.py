import numpy as np

def plot_hist(gryf, raven, huffle, slyth, label, axs, setTitle=True):

	hg = gryf[label]
	hg = hg[~np.isnan(hg)]
	axs.hist(hg, color='red', alpha=0.4)

	hs = slyth[label]
	hs = hs[~np.isnan(hs)]
	axs.hist(hs, color='green', alpha=0.4)

	hr = raven[label]
	hr = hr[~np.isnan(hr)]
	axs.hist(hr, color='blue', alpha=0.4)

	hh = huffle[label]
	hh = hh[~np.isnan(hh)]
	axs.hist(hh, color='yellow', alpha=0.4)

	if setTitle:
		axs.set_title(label)
