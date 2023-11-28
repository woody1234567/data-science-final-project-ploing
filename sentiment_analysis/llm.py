import pandas as pd
import openai
import time
import xlsxwriter
pd.options.mode.chained_assignment = None

# data[0][0] = body
# data[0][1] = date
# 103-11-29
# 107-11-24
# 111-11-26

# OpenAI key
key = "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"
# organization = "org-jp3IkVp4ofO2xxpwOCzjOBH7"
openai.api_key = key
# openai.organization = organization

with open('news_body.xlsx', 'rb') as f:
        data = pd.read_excel(f)
        data = data.values.tolist()

for i in range(len((data))):
	data[i][0] = data[i][0].replace("_x000D_", " ")
	data[i][0] = data[i][0].replace("\n", " ")
	data[i][0] = data[i][0].replace("\xa0", "").strip(' ')
	if len(data[i][0]) > 2500:
		data[i][0] = data[i][0][:2500]

for i in range(len(data)):
	flag = False
	while (flag == False):
		try:
			response = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				messages=[
						{"role": "user", "content": "請閱讀以下新聞："},
						{"role": "user", "content": data[i][0]},
						{"role": "user", "content": "請問這篇新聞是否有提到政府的政績？回答「有」或「沒有」就好"},
					],
				temperature=0.2
			)
			flag = True
			answer = response['choices'][0]['message']['content']
			if "沒有" in answer:
				data[i].append(0)
				print('no')
			else:
				data[i].append(1)
				print('yes')
		except:
			print("error. retry")
		time.sleep(3)

with xlsxwriter.Workbook('news_body_sentiment_out.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, row in enumerate(data):
        worksheet.write_row(row_num, 0, row)
