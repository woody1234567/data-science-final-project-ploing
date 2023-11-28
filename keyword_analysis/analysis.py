import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

keyword = ['柯文哲', '柯市長']
# keyword = ['蔣萬安', '蔣市長']
with open('data/news_body_with_keyword_柯文哲.xlsx', 'rb') as f:
        data = pd.read_excel(f)
        data = data.fillna(-1)
        data = data.values.tolist()

data = [[d[3], d[4]] for d in data]
# print('data: ', len(data))
for i in range(len(data)):
    cnt = 0
    text = data[i][0]
    for word in keyword:
        cnt += text.count(word)
    data[i].append(cnt)
          
all_date = sorted(list(set([d[1] for d in data])))
# print('all_date: ', all_date)
cnt_dict = {d:0 for d in all_date}

for i in range(len(data)):
     cnt_dict[data[i][1]] += data[i][2]
    
# print('cnt data: ', cnt_dict)
daily_frequency = [[i, j] for i, j in zip(cnt_dict.keys(), cnt_dict.values())]
final_date = [i for i in cnt_dict.keys()]
final_freq = [i for i in cnt_dict.values()]
# print(final_date)

plt.figure(figsize=(20,15))
plt.axvline(x = final_date.index('107-11-23'), color = 'g', label = 'axvline - full height')
plt.plot(final_date, final_freq, color='blue')
plt.xticks(final_date[::50],  rotation='vertical')
plt.xlabel('date')
plt.ylabel('mentioned times')
plt.title('number of mentioning of mayor Ko in every day official news')
plt.show()
