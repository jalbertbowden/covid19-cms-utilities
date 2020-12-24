import csv
import re

headers_min = ['Provider Name', 'Federal Provider Number', 'Provider Address','Provider City','County','Residents Total Confirmed COVID-19','Residents Total Suspected COVID-19','Residents Total All Deaths','Residents Total COVID-19 Deaths','Total Number of Occupied Beds','Staff Total Confirmed COVID-19','Staff Total Suspected COVID-19','Staff Total COVID-19 Deaths']

cms_states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
cms_reporting_dates = ['2020-05-24', '2020-05-31', '2020-06-07', '2020-06-14', '2020-06-21', '2020-06-28', '2020-07-05', '2020-07-12', '2020-07-19', '2020-07-26', '2020-08-02', '2020-08-09', '2020-08-16', '2020-08-23', '2020-08-30', '2020-09-06', '2020-09-13', '2020-09-20', '2020-09-27', '2020-10-04', '2020-10-11', '2020-10-18', '2020-10-25', '2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13']
cms_date = '2020-12-13'

csv_input_a = cms_date + '/cms/covid-19-nursing-home-dataset-week-ending-' + cms_date + '-'
csv_input_b = '-' + cms_date

def clean_cms_data(csv_input, csv_output, headers_min):
    csv_rows = []


    csv_input_file = csv_input + '.csv'
    with open(csv_input_file) as fin:    
    	csvin = csv.DictReader(fin)
        for row in csvin:
            providerName = row['Provider Name']
            providerFedID = row['Federal Provider Number']
            providerAddress  = row['Provider Address']
            providerCity  = row['Provider City']
            providerCounty  = row['County']
            providerCOVIDResidentsConfirmed  = row['Residents Total Confirmed COVID-19']
            providerCOVIDResidentsSuspected  = row['Residents Total Suspected COVID-19']
            providerCOVIDResidentsDeathsTotal  = row['Residents Total All Deaths']
            providerCOVIDResidentsDeathsCOVID  = row['Residents Total COVID-19 Deaths']
            providerCOVIDOccuppiedBeds  = row['Total Number of Occupied Beds']
            providerCOVIDStaffConfirmedTotal  = row['Staff Total Confirmed COVID-19']
            providerCOVIDStaffSuspectedTotal  = row['Staff Total Suspected COVID-19']
            providerCOVIDStaffDeathsTotal  = row['Staff Total COVID-19 Deaths']
            rowRow = [providerName, providerFedID, providerAddress, providerCity, providerCounty, providerCOVIDResidentsConfirmed, providerCOVIDResidentsSuspected, providerCOVIDResidentsDeathsTotal, providerCOVIDResidentsDeathsCOVID, providerCOVIDOccuppiedBeds, providerCOVIDStaffConfirmedTotal, providerCOVIDStaffSuspectedTotal, providerCOVIDStaffDeathsTotal]
            csv_rows.append(rowRow)

    output_clean_cms_data(csv_output, headers_min, csv_rows)


def output_clean_cms_data(csv_output, headers_min, csv_rows):
    csv_output_file = csv_output + '.csv'
    with open(csv_output_file, 'w') as csvfile:

        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers_min)
        csvwriter.writerows(csv_rows)

for state in cms_states:
    for reporting_date in cms_reporting_dates:
        state_cms = csv_input_a + state + '-' + reporting_date
        print(state_cms)
        csv_output = state_cms + '-min'
        clean_cms_data(state_cms, csv_output, headers_min)