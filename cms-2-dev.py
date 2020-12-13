# -*- coding: utf-8 -*-
import csv
import re
import cms_states

csv_input_a = 'states/covid-19-nursing-home-dataset-week-ending-2020-11-01-'
csv_input_b = '-2020-11-01-min'
# cms_states = ['AR', 'CA', 'CO', 'CT', 'FL', 'GA', 'IA', 'ID', 'IL', 'KY', 'LA', 'ME', 'MI', 'NC', 'ND', 'NJ', 'NM', 'NY', 'OH', 'OR', 'PA', 'VA', 'WV', 'WY']
# 'NM', 'NY', 'OH', 'OR', 'PA', 'VA', 'WV', 'WY
# 'SD', 'UT', 'VT', 'WA', 'WI']
var_cms_states = ['VA']

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

# clean_cms_data(csv_input)

def output_clean_cms_data(csv_output, csv_headers, csv_rows):
	csv_output_file = csv_output + '.csv'
	with open(csv_output_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = csv_headers[0])
		writer.writeheader()
		writer.writerows(csv_rows)

# output_clean_cms_data(csv_output, csv_headers, csv_rows)

for state in var_cms_states:
	print(state)
	state_input = csv_input_a + state + csv_input_b
	print(state_input)
	clean_cms_data(state_input, state)
	csv_output = state_input + '-normalized'
	# output_clean_cms_data(csv_output, csv_headers, csv_rows)
	print(state)