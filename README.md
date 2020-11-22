# covid19-cms-utilities  

Collection of Python scripts for wrangling with cms.gov's Nursing Home Dataset.  

NOTE: While in the process of detailing this, I became aware that LTC team's focus may shift...so this is not complete.  
Most people interested wanted to look @/help with the name normalization process.  
If you are normalizing Facility List data, you want to use `facilities-1.py` and `facilities-2.py`.  
If you are normalizing CMS data, you want to use `cms-data-min.py`, `cms-1.py`, and `cms-2.py`.  

1.
Run 'get-cms-nursing.py'
this will:
	download cms.gov Nursing Home dataset to 'cms' directory
	make a copy of the original dataset
	use the copy to chop the dataset into individual state CSVs
	chop each state CSV by date
	it produces 1300+ CSVs
	we only want 50+
	plan on cleaning this up programmatically, but have not even looked into, let alone started on fixing this.
	I have been manually selecting all of the unwanted CSVs and deleting them.


2.
Collect Facility List data
	cms.gov's dataset has a backdated timestamp; today is 2020-11-20 and the most current cms.gov dataset (released yesterday, 2020-11-19) is dated 2020-11-08.  
	[cms.gov's timestamp]

	In the date directory, make a new directory called 'states', and place the collected Facility Lists into this directory. 'states' directory is a sibling to the 'cms' directory.


3.
Minimize CMS data
	cms.gov dataset has over 50 columns and we only need a number of them to perform the `VLOOKUP`.
	open up `cms-data-min.py` and edit the value for the `date` variable to the current date timestamp for the cms.gov data.
	run `cms-data-min.py` and it will loop through each cms.gov state CSV and output a new CSV with only the columns/fields we need.  
	which reminds me, i'm willing to bet that most people analyzing this data aren't aware that the overwhelming majority of the data is cut off...we should fix that.

4. Minimize CMS data 2
	open up `cms-1.py` and edit the date value.
	if you are running it for all states, comment out the second `cms_states` array and run the script.
	if you are running it for one state, edit the second `cms_states` array with the desired state's acryonym, and run the script.

5. Minimize CMS data 3
	open up `cms-2.py` and edit `date` value.
	note the value in the `cms_states` array before editing with desired state's acronym.
	the majority of this script is always commented out...recalling the original value in the `cms_states` array,
	locate that states' normalizations by searching for `# XX`, where `XX` is the state's acronym.
	you can also simply scroll through to the state.
	comment out this state's normalization paremeters using Python's block comments `"""`.  
	Now find the state you are normalizing's parameters using the same approach(es).  
	Uncomment out this state's paremeters by deleting the Python block comments preceding and postceding the parameter code.
	Now run `cms-2.py`.
	Note: this is where the regex lives that does the normalizations. if you are adding/editing normalizations, this is where you'll be adding/editing values.

6. Minizing Facility Lists
	process for this is very similar to CMS and I'll double back here to flesh this out.



