# ElectionsProject

add your api keys to the twitter_credentials.py file and you are good to go
This repository contains the script for data extraction and a trial cleaning .ipynb files that are working successfully 
in cleaning the text of the data


The data cleaning scripts are under review and testing and will be available very soon. however the trial jupyter notebook
files has been successful in cleaning the data at least up to a point that polarity and subjectivity can be generated 
without any stress of going through the cleaning process again

NOTE:
To make use of this repo and its content 

1. first you must create an app on twitter developer page

2. retrieve your twitter credentials and insert them in the twitter_credentials.py 
(DataExtraction\Scripts\twitter_credentials.py) file. Note that without this this programs and scripts may not function 
as it's intended to

3. Open any of the files from the two folders for the two major political parties and run any of the script files to 
start the extraction process


4.After the extraction process for both parties have been successfully completed, copy all **.csv** files from 
**DataExtraction\CollectedData** to **CleanedData\NPP\Data\tweets** for each of the political parties respectively.
5. Run the **combineCSV.ipynb** (CleanedData\NPP\Data\tweets\combineCsv.ipynb) file and execute all cells.
this process combines all the individual csv files with the data from different individuals of the same party into one
csv file.

5. Naivigate to **CleanedData\NDC\Files\sentiment.ipynb** and execute all cells in the notebook file to process the 
collated data from both parties

NB: a combination of both sentiment process has been placed outside in the main folder 
**CleanedData\CombinedAnalysis.ipynb**, this holds the analysis of both parties side by side to make comparison and 
evaluation of the data easier


