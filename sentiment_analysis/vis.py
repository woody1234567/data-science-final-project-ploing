import matplotlib.pyplot as plt
import pandas as pd



with open('news_body_sentiment_out.xlsx', 'rb') as f:
        data = pd.read_excel(f)
        data = data.values.tolist()

all_days = []
for d in data:
    all_days.append(d[1])
all_days = set(all_days)

cnt = {i:0 for i in all_days}
all = {i:0 for i in all_days}
por = {i:0 for i in all_days}

for d in data:
    all[d[1]] += 1
    cnt[d[1]] += d[-1]

for i in all_days:
     por[i] = cnt[i] / all[i]
     
print('all: ', all)
print('cnt: ', cnt)
print('por: ', por)

plt.bar(por.keys(), por.values())
plt.show()