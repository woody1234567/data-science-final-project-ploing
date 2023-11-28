import numpy as np
import pandas as pd
import time
import xlsxwriter
pd.options.mode.chained_assignment = None


data = np.load('TPE_contents.npy', allow_pickle=True)
# len(data) = 49503
# data[0][1] = title
# data[0][2] = body
# data[0][3] = date
# 103-11-29
# 107-11-24
# 111-11-26

for i in range(len(data)):
    try:
        data[i][3] = int(data[i][3].replace('-', ''))
    except:
        data[i][3] = -1

def get_news_content(data, day):
    content = []
    for i in range(len(data)):
        if data[i][3] == day:
            content.append([data[i][2], data[i][3]])
    return content

# save partial data for web openai
def get_news_content_by_span(start_day, end_day):
    content = []
    for i in range(len(data)):
        if data[i][3] >= start_day and data[i][3] <= end_day:
            content.append([data[i][2], data[i][3]])
    return content

partial_data = get_news_content_by_span(1071120, 1071130)
with xlsxwriter.Workbook('10days_news_body.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, row in enumerate(partial_data):
        worksheet.write_row(row_num, 0, row)

'''
# OpenAI key
key = "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"
# organization = "org-jp3IkVp4ofO2xxpwOCzjOBH7"
openai.api_key = key
# openai.organization = organization

# with open("prompts_target_and_summarization.txt", "r") as f: 
# 	prompts = f.read()

# in_data = pd.read_csv(in_csv)

for i in range(len(in_data)):
	flag = False
	# sample = in_data.iloc[i, :]
	while (flag == False):
		try:
			response = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				messages=[
						{"role": "user", "content": prompts},
						{"role": "user", "content": 'Now for the sentence: ' + sample['utterance']},
						{"role": "user", "content": 'Give me the summarized sentence and the target object. Your answer must be in the form "summarized sentence: \n target object: "'},
					],
				temperature=0.2
			)
			flag = True
			answer = response['choices'][0]['message']['content'].split('\n')
			summarized_sentence = sample['utterance']
			target_object = sample['instance_type']

			# sample = sample.to_frame().T
			# sample.to_csv(out_csv, index=False, header=i==0, mode='a')
		except:
			print("error. retry")
		time.sleep(3)
'''