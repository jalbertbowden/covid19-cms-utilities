# -*- coding: utf-8 -*-
import csv
import re

date = '2020-11-08'
headers_facility_list = ['Facility Name', 'Facility Name Normalized', 'Date Collected', 'State', 'County', 'City', 'State Facility Type', 'CTP Facility Categorization', 'State/Fed Regulated', 'State Facility ID', 'CMS Facility ID', 'Date outbreak opened', 'Date outreak closed', 'Outbreak Status', 'Resident Census', 'Resident Positives', 'Resident Probable Positives', 'Resident Deaths', 'Resident Probable Deaths', 'Staff Positive', 'Staff Probable Positives', 'Staff Deaths', 'Staff Probable Deaths', 'Resident/Staff Positives', 'Resident/Staff Probable Positives', 'Resident/Staff Deaths', 'Resident/Staff Probable Deaths', 'Resident Positives', 'Resident Probable Positives', 'Resident Deaths', 'Resident Probable Deaths', 'Staff Positive', 'Staff Probable Positives', 'Staff Deaths', 'Staff Probable Deaths', 'Resident/Staff Positives', 'Resident/Staff Probable Positives', 'Resident/Staff Deaths', 'Resident/Staff Probable Deaths', 'Residents Tested', 'Staff Tested', 'Personal Protective Equipment']
# states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
states = ['OH']

def clean_cms_data(csv_input):
    csv_input_file = csv_input + '.csv'
    with open(csv_input_file) as fin:    
    	csvin = csv.DictReader(fin)
        headers = headers_facility_list
    	csv_headers.append(headers)

    	for row in csvin:
            providerName = row['Facility Name']
            providerNameStrip = providerName.strip()
            newName = providerNameStrip.upper()
            newName = newName.replace(' HLTH ', ' HEALTH ').replace('MANOR CARE HEALTH SERVICES', 'MANORCARE HEALTH SERVICES').replace(' & ', ' AND ').replace('CTR', 'CENTER').replace('CNTR', 'CENTER').replace('REHAB ', 'REHABILITATION ').replace(', LLC', '').replace(' LLC', '').replace('  ', ' ').replace(', INC.', '').replace(', INC', '').replace(' , INC.', '').replace('HOSP ', 'HOSPITAL ')
            newName = re.sub('REHAB$', 'REHABILITATION', newName)
            newName = re.sub(', THE$', '', newName)
            newName = re.sub(' INC$', '', newName)
            newName = re.sub(' INC.$', '', newName)
            newName = re.sub(',INC.$', '', newName)
            newName = re.sub(', LTD$', '', newName)
            newName = re.sub(' CENTE$', ' CENTER', newName)
            newNameAlt = newName.strip()
            newNameAlt = re.sub(' \(THE\)$', '', newName)
            newNameAlt = re.sub(' THE$', '', newNameAlt)
            newNameAlt = re.sub(' NRSG ', ' NURSING ', newNameAlt)
            newNameAlt = re.sub(' NSG ', ' NURSING ', newNameAlt)
            newNameAlt = re.sub(' REHAB. ', ' REHABILITATION ', newNameAlt)
            newNameAlt = re.sub(' FACI$', ' FACILITY', newNameAlt)
            newNameAlt = re.sub(',$', '', newNameAlt)

            row['Facility Name Normalized'] = newNameAlt
            newCounty = row['County'].upper()
            newCity = row['City'].upper()
            row['County'] = newCounty
            row['City'] = newCity
            csv_rows.append(row)

def output_clean_cms_data(csv_output, headers_facility_list, csv_rows):
    csv_output_file = csv_output + '.csv'
    with open(csv_output_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers_facility_list)
        writer.writeheader()
        writer.writerows(csv_rows)

for state in states:
    state_facility = date + '/states/' + state + '-' + date + '-facility-list-data'
    csv_rows = []
    csv_headers = []
    clean_cms_data(state_facility)
    csv_output = state_facility + '-normalized'
    output_clean_cms_data(csv_output, headers_facility_list, csv_rows)