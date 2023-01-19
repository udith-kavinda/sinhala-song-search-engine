# IR_Project-Song_Search_Engine
Sinhala Song Search Engine using ElasticSearch and Python for IR Project(CS4642)

## Getting Start
### Setting up the Environment
* Download and Install the _ElasticSearch_
* Install the _ICU_Tokenizer_ plugin on the ElasticSearch
* Install the _python3_ with _pip3_
* Install the python packages in the _requirements.txt_
   ```
   pip install -r /path/to/requirements.txt
   ```

### Running the Project
1. First start the ElasticSearch locally on port 9200.
2. Then run **_index_creation.py_** file to create the index and insert data.
3. Next run the **_main.py_** to start the search engine
4. Then visit http://localhost:5000/ for see the user interface.
5. Finally add your search query in the search box for searching.

## File Structure
* data - Folder contains jason file and csv file of corpus of sinhala songs
* templates - Folder contains Html user interface of the search engine
* images - Folder contains diagrams used in README.md
* index_creation.py - Python code for index creating and data inserting
* search_function.py - Python code use for process search query
* search_queries.py - Elastic Search queries
* requirements.txt - python requirements 

## Details of Song Data
sinhala_songs.json file contains 100 Sinhala Songs with the following data.
1. title
2. artist
3. lyricist
4. album
5. year
6. lyric 
7. metaphors

## Basic Functionalities
* It supports searching by the title, artist
name, writer name, album name, year or using the part of the lyrics.(Faceted Query)
> eg : කඳුල ඉතින් සමා වෙයන්, පාරමිතා නොපුරමු අප දෙදෙනා,  නිසංසල සඳක්, ශෂිකා නිසංසලා
* Can search songs using year which they released and by giving two years seperated by space (ex- 2000 2020), we can get all the songs between those two years.
> eg : 2000 2017, 2017
* Search Engine can identify synonyms related to specific fields like ගයපු(artist), ලියපු(lyricist), සංගීත(music) and search
based on the identified fields
> eg : ගුණදාස කපුගේ ගයපු සින්දු, කරුණාරත්න රචකයා
* Search Engine supports only Sinhala Language queries
> eg : ගුණදාස කපුගේ ගයපු සින්දු

Following images shows the example search result of the UI.

![Search Example of UI](./images/search_results1.PNG)

![Search Example of UI](./images/search_results2.PNG)


