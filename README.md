# covid19-cms-utilities  

Collection of Python scripts for wrangling with [cms.gov's Nursing Home Dataset](https://data.cms.gov/stories/s/bkwz-xpvg), and normalizing the reported facility names.  

NOTE: This initally included processes for normalizing the facility names that states report. Functionality for that is still baked in, but is not in use.  

## Starting Off  
Check [COVID-19 Nursing Home Data landing page](https://data.cms.gov/stories/s/bkwz-xpvg) for the latest dataset date release.  
That value, in international format (YYYY-MM-DD) needs to be added to `get-cms-nursing.py` as the value for `file_date`.  
Open up `cms-1.py` and `cms-2.py` and update the `cms_date` with the value, as well as append the value to the `cms_reporting_dates` list. 

Once these have been updated, run `get-cms-nursing-py` to download the latest CMS dataset, dividing it into separate files by state, and then dividing those files by date.
Then run `cms-1.py` and `cms-2.py`, both of which normalize the facility names and output minimized, normalized data files.
Output from `cms-1.py` has `-min` appended to the file name, output from `cms-2.py` has `-normalized` appended after the `-min` in the file name.  

From start to finish, this process takes some time to run, clocked in @ almost an hour in its last run.  

The initial CMS dataset files are too big for GitHub's default, so be sure to compress them and delete the original file before committing any work.
