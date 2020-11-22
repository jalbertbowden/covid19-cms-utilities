import csv
import re

date = '2020-11-08'
headers_min = ['Provider Name', 'Federal Provider Number', 'Provider Address','Provider City','County','Residents Total Confirmed COVID-19','Residents Total Suspected COVID-19','Residents Total All Deaths','Residents Total COVID-19 Deaths','Total Number of Occupied Beds','Staff Total Confirmed COVID-19','Staff Total Suspected COVID-19','Staff Total COVID-19 Deaths', 'Latitude', 'Longitude']
cms_dir = 'cms/'
cms_states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
csv_input_a = date + '/' + cms_dir + 'covid-19-nursing-home-dataset-week-ending-' + date + '-'
csv_input_b = '-' + date
csv_rows = []

def clean_cms_data(csv_input):
    csv_input_file = csv_input + '.csv'
    with open(csv_input_file) as fin:    
    	csvin = csv.DictReader(fin)
        for row in csvin:
            provider_name = row['Provider Name']
            provider_fed_id = row['Federal Provider Number']
            provider_address  = row['Provider Address']
            provider_city  = row['Provider City']
            provider_county  = row['County']
            provider_covid_residents_confirmed  = row['Residents Total Confirmed COVID-19']
            provider_covid_residents_suspected  = row['Residents Total Suspected COVID-19']
            provider_covid_residents_deaths_total  = row['Residents Total All Deaths']
            provider_covid_residents_deaths_covid  = row['Residents Total COVID-19 Deaths']
            provider_covid_occupied_beds  = row['Total Number of Occupied Beds']
            provider_covid_staff_confirmed_total  = row['Staff Total Confirmed COVID-19']
            provider_covid_staff_suspected_total  = row['Staff Total Suspected COVID-19']
            providerCOVIDStaffDeathsTotal  = row['Staff Total COVID-19 Deaths']
            provider_geo_coordinates = row['Geolocation']
            provider_geo = provider_geo_coordinates.replace('POINT (', '').replace(')', '')
            if provider_geo_coordinates == '':
                provider_coordinates = [0, 0]
            else:
                provider_coordinates = provider_geo.split(' ')

            provider_lon = provider_coordinates[0]
            provider_lat = provider_coordinates[1]
            rowRow = [provider_name, provider_fed_id, provider_address, provider_city, provider_county, provider_covid_residents_confirmed, provider_covid_residents_suspected, provider_covid_residents_deaths_total, provider_covid_residents_deaths_covid, provider_covid_occupied_beds, provider_covid_staff_confirmed_total, provider_covid_staff_suspected_total, providerCOVIDStaffDeathsTotal, provider_lat, provider_lon]
            csv_rows.append(rowRow)


def output_clean_cms_data(csv_output, headers_min, csv_rows):
    csv_output_file = csv_output + '.csv'
    with open(csv_output_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers_min)
        csvwriter.writerows(csv_rows)

for state in cms_states:
    state_cms = csv_input_a + state + csv_input_b
    csv_output = state_cms + '-min'
    clean_cms_data(state_cms)
    output_clean_cms_data(csv_output, headers_min, csv_rows)
print('cms state csv min complete!')