import pandas as pd
channel=pd.read_csv('ychannels.csv') 

channel_id = dict()

name = list()
cid = list()

for chid in channel['id']:
    cid.append(chid)

for val in channel['name']:
    name.append(val)

k = 0
while k<len(cid):
    channel_id[cid[k]] = name[k].strip()
    k = k + 1

print(channel_id)