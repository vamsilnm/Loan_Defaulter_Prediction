import csv
import re
file_open = open('/home/vamsi/Documents/loan_defaulter_challenge/train_indessa.csv')
file_read = csv.reader(file_open)
# file_output = open('non_defaulter_transactions.csv','w')
# output_writer = csv.writer(file_output)
record_count = 0
pt_plan = {}
defaulter = 0
non_defaulter = 0
discrepency_defaulter = 0
discrepency_non_defaulter = 0
inconsistency = []
for each_row in file_read:
	if pt_plan.get(each_row[13]):
		pt_plan[each_row[13]] += 1
	else:
		pt_plan[each_row[13]] = 1
print pt_plan.keys()
print pt_plan

	

	
		
		
# print 'd_defualter',discrepency_defaulter
# print 'd_non_defualter',discrepency_non_defaulter		
# print 'defaulter',defaulter
# print 'non_defaulter',non_defaulter
# print record_count
# print 532429 - record_count
# print inconsistency
	
# if each_row[2] != each_row[3]:
# 		record_count += 1
# 		if each_row[44] == '1':
# 			discrepency_defaulter += 1
# 		else:
# 			discrepency_non_defaulter += 1
# 	else:
# 		if each_row[44] == '1':
# 			defaulter += 1
# 		else:
# 			non_defaulter += 1
	
# print pt_plan
	
# if pt_plan.get(each_row[16]):
# 		pt_plan[each_row[16]] += 1
# 	else:
# 		pt_plan[each_row[16]] = 1