import requests
import os
import csv




nursing_home_dataset_csv_url = 'https://data.cms.gov/api/views/s2uc-8wxp/rows.csv?accessType=DOWNLOAD'
nursing_home_dataset_csv_file = 'COVID-19_Nursing_Home_Dataset.csv'

file_base = 'covid-19-nursing-home-dataset-week-ending-'
file_date = '2020-11-29'
file_format = '.csv'
file_name = file_date + '/' + file_base + file_date + file_format

directory_current = os.getcwd()

def get_cms_file_name(file_date, nursing_home_dataset_csv_file):
	current_nursing_home_dataset_csv_file = nursing_home_dataset_csv_file.split('.')
	print(current_nursing_home_dataset_csv_file[0])

get_cms_file_name(file_date, nursing_home_dataset_csv_file)

def make_date_directory(directory_current, file_date):
	mode = 0755
	path = os.path.join(directory_current, file_date)
	try:
		os.mkdir(path, mode)
	except OSError as error:
		print("Directory '% s' already exists!" % file_date)
		print(error)
	else:
		print("Directory '% s' created" % file_date)


def get_latest_cms_data(nursing_home_dataset_csv_url, nursing_home_dataset_csv_file, nursing_home_dataset_csv_file_local):
	print "Downloading file:%s" % nursing_home_dataset_csv_file
	r = requests.get(nursing_home_dataset_csv_url)

	with open(nursing_home_dataset_csv_file_local, 'wb') as code:
		code.write(r.content)
	print "File:%s" % nursing_home_dataset_csv_file_local + " download complete!"



def get_local_file_name(file_date, nursing_home_dataset_csv_file):
	local_nursing_home_dataset_csv_file = file_date + '/' + nursing_home_dataset_csv_file
	return local_nursing_home_dataset_csv_file

def make_cms_data_clone(file_date, nursing_home_dataset_csv_file, file_name):
	print('cloning cms dataset!')
	csv_rows = []
	csv_headers = []

	with open(nursing_home_dataset_csv_file_local) as fin:
		csvin = csv.DictReader(fin)
		for header in csvin.fieldnames:
			csv_headers.append(header)
		for row in csvin:
			csv_rows.append(row)

	with open(file_name, 'w') as fout:
		dw = csv.DictWriter(fout, fieldnames=csv_headers)
		dw.writeheader()
		for csv_row in csv_rows:
			dw.writerow(csv_row)

	print('cms data clone successful. new file: ' + file_name)

states_array = []

def make_cms_state_csvs(file_name):
	file_name_states = file_name.split('.')
	file_name_states_path = file_name_states[0] + '-'

	with open(file_name) as fin:
		csvin = csv.DictReader(fin)
		outputs = {}
		for row in csvin:
			cat = row['Provider State']
			# print(cat)
			if cat not in outputs:
				print('new state: ', cat)
				states_array.append(cat)
				state_file_name = file_name_states_path + cat
				print(state_file_name)
				fout = open(file_name_states_path + '{}.csv'.format(cat), 'w')
				dw = csv.DictWriter(fout, fieldnames=csvin.fieldnames)
				dw.writeheader()
				outputs[cat] = fout, dw
			outputs[cat][1].writerow(row)
		for fout, _ in outputs.values():
			fout.close()
	print('cms data split by state complete!')


def make_cms_state_date_csvs(file_name, states_array):
	print('make cms state date csvs: ', file_name)
	state_file_name = file_name.split('.')
	state_file_name_path = state_file_name[0] + '-'
	print('state file name path: ', state_file_name_path)

	counter = 0
	for state in states_array:
		print('counter: ', counter)
		print('state: ', state)
		print(state_file_name_path)
		print(state_file_name_path + state)
		counter = counter + 1
		state_file_path = state_file_name_path + state + '.csv'
		print('state file name: ', state_file_path)

		with open(state_file_path) as fin:
			csvin = csv.DictReader(fin)
			outputs = {}
			for row in csvin:
				cat = row['Week Ending']
				cat = cat.replace('/', '-')
				date_arr = cat.split('-')
				file_text_date = date_arr[2] + '-' + date_arr[0] + '-' + date_arr[1]
				print('corrected date: ', file_text_date)
				if cat not in outputs:

					state_file_name_out = state_file_name_path + state + '-' + cat
					print(state_file_name_out)
					fout = open(state_file_name_path + state + '-{}.csv'.format(file_text_date), 'w')
					dw = csv.DictWriter(fout, fieldnames=csvin.fieldnames)
					dw.writeheader()
					outputs[cat] = fout, dw
				outputs[cat][1].writerow(row)
			for fout, _ in outputs.values():
				fout.close()
		print('cms state data split by date complete!')

# make directory for latest dataset's date
make_date_directory(directory_current, file_date)
# get local cms data file name/path
nursing_home_dataset_csv_file_local = get_local_file_name(file_date, nursing_home_dataset_csv_file)
# download latest cms.gov dataset csv
get_latest_cms_data(nursing_home_dataset_csv_url, nursing_home_dataset_csv_file, nursing_home_dataset_csv_file_local)
# make clone of cms data
make_cms_data_clone(file_date, nursing_home_dataset_csv_file, file_name)
# chop cms csv into individual state csvs
make_cms_state_csvs(file_name)
# chop cms state csvs into individual state by date csvs
make_cms_state_date_csvs(file_name, states_array)