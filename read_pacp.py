import os
from scapy.all import *
import matplotlib.pyplot as plt
import collections
import numpy as np

def get_feature_vec(filename):
	try: 
		traffic = rdpcap(filename)
		# print('read')
		data = []
		for record in traffic:
			if str(record['IP'].src)=='1.1.1.1' or str(record['IP'].dst)=='1.1.1.1' :
				if str(record['IP'].dst)=='1.1.1.1' and (len(record['TCP'].payload)>0):
					data.append(len(record['TCP'].payload))
				elif len(record['TCP'].payload)>0:
					data.append(-len(record['TCP'].payload))

		return np.array(data)

	except: 
		print(sys.exc_info()[0])
		return -1



# filename='pcaps/chrome/test_low_traf/chrome4.pcap'


############# globals
LENGTH = 202
chrome_avg_in = []
chrome_avg_out = []
firefox_avg_in = []
firefox_avg_out = []
phantomjs_avg_in = []
phantomjs_avg_out = []

chrome_avgs = []
firefox_avgs = []
phantomjs_avgs = []
#############

# chrome
for i in range(LENGTH):
	res = get_feature_vec('pcaps/chrome/test_large_scale/chrome{}.pcap'.format(i))
	chrome_avgs.append(np.average(res))


# firefox
for i in range(LENGTH):
	res = get_feature_vec('pcaps/firefox/test_large_scale/firefox{}.pcap'.format(i));
	firefox_avgs.append(np.average(res))

# phantomjs
for i in range(LENGTH):
	res = get_feature_vec('pcaps/phantomjs/test_large_scale/phantomjs{}.pcap'.format(i))
	phantomjs_avgs.append(np.average(res))


# list to array
chrome_avgs_new = np.array(chrome_avgs)
firefox_avgs_new = np.array(firefox_avgs)
phantomjs_avgs_new = np.array(phantomjs_avgs)

# remove NaN
# chrome_nan_array = np.isnan(chrome_avgs)
# chrome_not_nan_array = ~ chrome_nan_array
# chrome_avgs_new = chrome_avgs[chrome_not_nan_array]

# firefox_nan_array = np.isnan(firefox_avgs)
# firefox_not_nan_array = ~ firefox_nan_array
# firefox_avgs_new = firefox_avgs[firefox_not_nan_array]

# phantomjs_nan_array = np.isnan(phantomjs_avgs)
# phantomjs_not_nan_array = ~ phantomjs_nan_array
# phantomjs_avgs_new = phantomjs_avgs[phantomjs_not_nan_array]

print(chrome_avgs_new)
print(firefox_avgs_new)
print(phantomjs_avgs_new)

# plots
fig, axs = plt.subplots(3)
fig.suptitle('average packet lengths of chrome, firefox and phantomjs')
axs[0].set_title('chrome')
axs[0].plot(chrome_avgs_new, 'tab:orange')
axs[1].set_title('firefox')
axs[1].plot(firefox_avgs_new, 'tab:green')
axs[2].set_title('phantomjs')
axs[2].plot(phantomjs_avgs_new, 'tab:blue')
plt.show()
# res = get_feature_vec(filename)
# print(res)
# plt.plot(res)
# plt.show()





