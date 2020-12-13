# -*- coding: utf-8 -*-
import csv
import re
import facilities_states

# ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
csv_input = 'facilities/VA-2020-11-01-facility-list-data-normalized'
csv_rows = []
csv_headers = []
csv_output = csv_input + '-cleaned'

# headers_facility_list = ['Facility Name', 'Facility Name Normalized', 'Date Collected', 'State', 'County', 'City', 'State Facility Type', 'CTP Facility Categorization', 'State/Fed Regulated', 'State Facility ID', 'CMS Facility ID', 'Date outbreak opened', 'Date outreak closed', 'Outbreak Status', 'Resident Census', 'Resident Positives', 'Resident Probable Positives','Resident Deaths','','','','','','','','','','','','','','']
headers_facility_list = ['Facility Name', 'Facility Name Normalized', 'Date Collected', 'State', 'County', 'City', 'State Facility Type', 'CTP Facility Categorization', 'State/Fed Regulated', 'State Facility ID', 'CMS Facility ID', 'Date outbreak opened', 'Date outreak closed', 'Outbreak Status', 'Resident Census', 'Resident Positives', 'Resident Probable Positives', 'Resident Deaths', 'Resident Probable Deaths', 'Staff Positive', 'Staff Probable Positives', 'Staff Deaths', 'Staff Probable Deaths', 'Resident/Staff Positives', 'Resident/Staff Probable Positives', 'Resident/Staff Deaths', 'Resident/Staff Probable Deaths', 'Resident Positives', 'Resident Probable Positives', 'Resident Deaths', 'Resident Probable Deaths', 'Staff Positive', 'Staff Probable Positives', 'Staff Deaths', 'Staff Probable Deaths', 'Resident/Staff Positives', 'Resident/Staff Probable Positives', 'Resident/Staff Deaths', 'Resident/Staff Probable Deaths', 'Residents Tested', 'Staff Tested', 'Personal Protective Equipment']

state = 'VA'

def clean_cms_data(csv_input, state):
    csv_input_file = csv_input + '.csv'
    print('initial state: ', state)

    with open(csv_input_file) as fin:    
    	csvin = csv.DictReader(fin)
    	# grab headers
    	csv_headers.append(headers_facility_list)


    	for row in csvin:
            providerName = row['Facility Name Normalized']
            print(row['Facility Name Normalized'])
            providerNameStrip = providerName.strip()
            newName = providerNameStrip
            # NY -> .replace(' N Y C', 'NYC').replace('N Y S ', 'NYS ').replace('N Y ', 'NY ').replace('H C F', 'HCF').replace('H R F', 'HRF').replace('R H C F', 'RHCF')
            newName = newName.replace('\n', ' ').replace('\r', ' ').replace(' HLTH ', ' HEALTH ').replace('MANOR CARE HEALTH SERVICES', 'MANORCARE HEALTH SERVICES').replace(' & ', ' AND ').replace('CTR', 'CENTER').replace('CNTR', 'CENTER').replace('REHAB ', 'REHABILITATION ').replace(', LLC', '').replace(' LLC', '').replace('  ', ' ').replace(', INC.', '').replace(', INC', '').replace(' , INC.', '').replace('HOSP ', 'HOSPITAL ')
            print(newName)
            newName = re.sub('&', ' AND ', newName)
            newName = re.sub('REHAB$', 'REHABILITATION', newName)
            newName = re.sub(', THE$', '', newName)
            newName = re.sub(', LP$', '', newName)
            newName = re.sub(', LP.$', '', newName)
            newName = re.sub(' INC$', '', newName)
            newName = re.sub(' INC.$', '', newName)
            newName = re.sub(',INC.$', '', newName)
            newName = re.sub(', LTD$', '', newName)
            newName = re.sub(' CENTE$', ' CENTER', newName)

            newNameStrip = newName.strip()
            newNameAlt = newNameStrip.strip()
            newNameAlt = re.sub(' \(THE\)$', '', newNameAlt)
            newNameAlt = re.sub(' THE$', '', newNameAlt)
            newNameAlt = re.sub(' CONV. ', ' CONVALESCENT ', newNameAlt)
            newNameAlt = re.sub(' NRSG ', ' NURSING ', newNameAlt)
            newNameAlt = re.sub(' NSG ', ' NURSING ', newNameAlt)
            newNameAlt = re.sub(' REHAB. ', ' REHABILITATION ', newNameAlt)
            newNameAlt = re.sub(' FACI$', ' FACILITY', newNameAlt)
            newNameAlt = re.sub(',$', '', newNameAlt)
            newNameAlt = re.sub('~', '', newNameAlt)
            newNameAlt = re.sub(' §$', '', newNameAlt)

            new_facility_name = facilities_states.normalize_state(state, newNameAlt)

            # print(newNameAlt)
            print('new facility name: ', new_facility_name)
            # newNameAltStrip = newNameAlt.strip()
            # newNameAltSplit = newNameAlt.split('(')
            # row['Facility'] = newName
            # row['Provider Name'] = newName
            # row['Facility Name'] = newName
            # print(newNameAltSplit[0])
            # row['Facility Name Normalized'] = newNameAltSplit[0]
            # newNameAltStrip = newNameAlt.strip()
            row['Facility Name Normalized'] = new_facility_name
            print('what')
            csv_rows.append(row)

clean_cms_data(csv_input, state)

def output_clean_cms_data(csv_output, headers_facility_list, csv_rows):
    csv_output_file = csv_output + '.csv'
    with open(csv_output_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers_facility_list)
        writer.writeheader()
        writer.writerows(csv_rows)

# output_clean_cms_data(csv_output, headers_facility_list, csv_rows)