Internal Reporting Tool
=======================

## Project Description:
This tool was created to display the top 3 articles, author rankings, and dates with more that 1% request errors by querying the newsdata SQL database. The output that the tool displays has been put into the project-output.rtf file included.

## Dependencies:
* [Python](https://www.python.org/downloads/) 3.6 or higher installed.
* [PostgreSQL](https://www.postgresql.org/download/) 9.5.12 or higher installed.

## Running the project:
* Prepare the database:
 1. Unzip the newsdata.sql to a folder.
 2. Open a terminal or Git bash window and change directories to the folder containing the newsdata.sql file.
 3. Enter `psql -d news -f newsdata.sql` to load the data into PostgreSQL.
 4. Once the data is loaded, connect to the database by entering `psql -d news`.
 5. Check the newsdata tables are there with the command `\dt`.
 6. Now you will need to create the author_slug view by entering the command: `create view author_slug as select slug, name from articles, authors where articles.author = authors.id;`.
 7. Check the view by entering the command: `select * from author_slug`.
 8. Now create the error_dates view by entering the command: `create view error_dates as select count(status) as errors, time::date as date from log where status =  '404 NOT FOUND' group by time::date order by time::date;`.
 9. Check the view by entering the command: `select * from error_dates`.

* Executing the data reporting tool:
 1. Copy the datareporting.py file into the same directory as the newsdata.sql file.
 2. Open a terminal and change directories to where the datareporting.py file is.
 3. Run the file by entering the command: `python datareporting.py`.

## File Manifest
* datareporting.py
* project_output.rtf
* README.md