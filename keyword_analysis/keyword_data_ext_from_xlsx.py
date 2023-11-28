# This script extracts all news with certain keywords contained in the text body

from cgitb import text
from operator import neg
import pandas as pd
import xlsxwriter
pd.options.mode.chained_assignment = None


with open('TPE_news_content.xlsx', 'rb') as f:
        data = pd.read_excel(f)
        data = data.fillna(-1)
        data = data.values.tolist()          

# len(data) = 49503
# data[0][2] = title
# data[0][3] = body

keyword = ['柯文哲', '柯市長']
neg_keyword = ['參選人柯文哲']
date_span = [1031129, 1111126]

# keyword = ['蔣萬安', '蔣市長']
# neg_keyword = ['參選人蔣萬安', '蔣萬安立委', '立委蔣萬安']
# date_span = [1111126, 10**10]

content = []
count = 0
for i in range(len(data)):
	text_body = data[i][3]
	try:
		date = int(data[i][4].replace('-', ''))
	except:
		date = -1
	if date <= date_span[0] or date >= date_span[1]:
		continue

	neg_Flag = False
	for neg_key in neg_keyword:
		try:
			if neg_key in text_body:
				neg_Flag = True
				break
		except:
			pass

	for key in keyword:
		try:
			if key in text_body and not neg_Flag:
				content.append(data[i])
				break
		except:
			pass


with xlsxwriter.Workbook('news_body_with_keyword_{}.xlsx'.format(keyword[0])) as workbook:
	worksheet = workbook.add_worksheet()
	for row_num, row in enumerate(content):
		worksheet.write_row(row_num, 0, row)
