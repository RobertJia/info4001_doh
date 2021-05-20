import os
from scapy.all import *
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

filename=''

print(get_feature_vec(filename))





