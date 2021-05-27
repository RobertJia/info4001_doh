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
			    elif (len(record['TCP'].payload)>0):
			        data.append(-len(record['TCP'].payload))

		return np.array(data)

	except: 
		print(sys.exc_info()[0])
		return -1



# filename='pcaps/chrome/test_low_traf/chrome4.pcap'


############# globals
LENGTH = 202
chrome_avgs = []
firefox_avgs = []
phantomjs_avgs = []
#############

# chrome
for i in range(LENGTH){
	res = get_feature_vec('pcaps/chrome/test_large_scale/pcaps/chrome{}.pcap'.format(i));
	chrome_avgs.append(np.average(res))
}

# firefox
for i in range(LENGTH){
	res = get_feature_vec('pcaps/firefox/test_large_scale/pcaps/firefox{}.pcap'.format(i));
	firefox_avgs.append(np.average(res))
}

# phantomjs
for i in range(LENGTH){
	res = get_feature_vec('pcaps/phantomjs/test_large_scale/pcaps/phantomjs{}.pcap'.format(i));
	phantomjs_avgs.append(np.average(res))
}

# list to array
chrome_avgs = np.array(chrome_avgs)
firefox_avgs = np.array(firefox_avgs)
phantomjs_avgs = np.array(phantomjs_avgs)

# plots
plt.boxplot(chrome_avgs)

# res = get_feature_vec(filename)
# print(res)
# plt.plot(res)
# plt.show()





