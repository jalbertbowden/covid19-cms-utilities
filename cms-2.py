# -*- coding: utf-8 -*-
import csv
import re
import cms_states

cms_reporting_states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
cms_reporting_dates = ['2020-05-24', '2020-05-31', '2020-06-07', '2020-06-14', '2020-06-21', '2020-06-28', '2020-07-05', '2020-07-12', '2020-07-19', '2020-07-26', '2020-08-02', '2020-08-09', '2020-08-16', '2020-08-23', '2020-08-30', '2020-09-06', '2020-09-13', '2020-09-20', '2020-09-27', '2020-10-04', '2020-10-11', '2020-10-18', '2020-10-25', '2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13']
cms_date = '2020-12-13'
csv_input_a = cms_date + '/cms/covid-19-nursing-home-dataset-week-ending-' + cms_date + '-'

csv_rows = []
csv_headers = []

def clean_cms_data(csv_input, state):
	csv_input_file = csv_input + '.csv'
	with open(csv_input_file) as fin:    
		csvin = csv.DictReader(fin)

		headers = csvin.fieldnames
		csv_headers.append(headers)

		for row in csvin:
			providerName = row['Provider Name']
			print(row['Provider Name'])
			providerCounty = row['County']
			newCounty = providerCounty.upper()
			
			if state == 'NY':
				newName = providerName.replace('\n', '').replace('\r', '').replace('  ', ' ').replace(' -- ', ' - ').replace(' N Y C', 'NYC').replace('N Y S ', 'NYS ').replace('N Y ', 'NY ').replace('H C F', 'HCF').replace('H R F', 'HRF').replace('R H C F', 'RHCF').replace(' & ', ' AND ').replace('&', ' AND ').replace('A S N F', 'ASNF').replace('CTR', 'CENTER').replace('CNTR', 'CENTER').replace(' CONV ', ' CONVALESCENT ').replace(' CONV. ', ' CONVALESCENT ').replace(' HLTH ', ' HEALTH ').replace('HOSP ', 'HOSPITAL ').replace(', INC.', '').replace(', INC', '').replace(' , INC.', '').replace(', LLC', '').replace(' LLC', '').replace(', L L C', '').replace('L L C', '').replace(' LLC', '').replace(' L T C', ' LTC').replace(' NSG ', ' NURSING ').replace('NRSG', 'NURSING').replace(' NRSING', 'NURSING').replace(' NRS ', ' NURSING ').replace(' PHY ', ' PHYSICAL ').replace('REHAB ', 'REHABILITATION ').replace('S N F', 'SNF').replace(' T C U', ' TCU').replace('WAR MEM ', 'WAR MEMORIAL ')
			else:
				newName = providerName.replace('\n', '').replace('\r', '').replace('  ', ' ').replace(' -- ', ' - ').replace(' & ', ' AND ').replace('&', ' AND ').replace('A S N F', 'ASNF').replace('CTR', 'CENTER').replace('CNTR', 'CENTER').replace(' CONV ', ' CONVALESCENT ').replace(' CONV. ', ' CONVALESCENT ').replace(' HLTH ', ' HEALTH ').replace('HOSP ', 'HOSPITAL ').replace(', INC.', '').replace(', INC', '').replace(' , INC.', '').replace(', LLC', '').replace(' LLC', '').replace(', L L C', '').replace('L L C', '').replace(' LLC', '').replace(' L T C', ' LTC').replace(' NSG ', ' NURSING ').replace('NRSG', 'NURSING').replace(' NRSING', 'NURSING').replace(' NRS ', ' NURSING ').replace(' PHY ', ' PHYSICAL ').replace('REHAB ', 'REHABILITATION ').replace('S N F', 'SNF').replace(' T C U', ' TCU').replace('WAR MEM ', 'WAR MEMORIAL ')			
			print(newName)
			newName = re.sub('REHAB$', 'REHABILITATION', newName)
			newName = re.sub(' REHABILI$', ' REHABILITATION', newName)
			newName = re.sub(' CEN$', ' CENTER', newName)
			newName = re.sub(' CENTE$', ' CENTER', newName)
			newName = re.sub(' HOSP$', ' HOSPITAL', newName)
			newName = re.sub(' HOSP$', ' HOSPITAL', newName)
			newName = re.sub(' HOSPITA$', ' HOSPITAL', newName)
			newName = re.sub(', INC$', '', newName)
			newName = re.sub(' INC$', '', newName)
			newName = re.sub(' INC.$', '', newName)
			newName = re.sub(',INC$', '', newName)
			newName = re.sub(', LP$', '', newName)
			newName = re.sub(', LTD$', '', newName)
			newName = re.sub(', THE$', '', newName)
			newName = re.sub(' THE$', '', newName)
			newName = re.sub(',THE$', '', newName)
			newName = re.sub(' \(THE\)$', '', newName)
			newName = re.sub(' \( THE \)$', '', newName)
			newName = re.sub(' COMMUNIT$', ' COMMUNITY', newName)
			newName = re.sub(',$', '', newName)

			newName = cms_states.normalize_cms_state(state, newName)

			print(newName)
			newNameStrip = newName.strip()
			row['Provider Name'] = newNameStrip
			row['County'] = newCounty
			csv_rows.append(row)

def output_clean_cms_data(csv_output, csv_headers, csv_rows):
	csv_output_file = csv_output + '.csv'
	with open(csv_output_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = csv_headers[0])
		writer.writeheader()
		writer.writerows(csv_rows)


for state in cms_reporting_states:
	for reporting_date in cms_reporting_dates:
		print('reporting date: ', reporting_date)
		csv_input_b = '-' + reporting_date + '-min'
		print(csv_input_b)
		state_input = csv_input_a + state + csv_input_b
		print('state input: ', state_input)
		clean_cms_data(state_input, state)
		csv_output = state_input + '-normalized'
		output_clean_cms_data(csv_output, csv_headers, csv_rows)
	print(state + ' is done!')