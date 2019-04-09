# yeast_dictionary

##### SGD data accessed Apr 12, 2018


### Instructions:   
1. Download the [yeast_dictionary repository](https://github.com/j-berg/yeast_dictionary/archive/master.zip) to your Desktop
2. Unzip the downloaded repository file
3. Copy your matrix of interest into the yeast dictionary folder/directory
  - Must be a .csv file (can resave the file in this format using Excel) 
  - Make sure the column with the gene systematic names (i.e. YGL080W) is labeled `ORF name`. This is case-sensitive and must include the space
4. Open Terminal or other command-line interface (you can type this in Spotlight Search on a Mac to find it easily)
5. Navigate to directory where the yeast_dictionary files are by typing the following and pressing enter after each line:
```
cd ~/Desktop
cd yeast_dictionary-master
```
6. Execute the script on your dataframe by the following command:
```
python yeast_dict.py input_table_name.csv output_table_file.csv
```
7. Your new table should be output in the `yeast_dictionary-master` directory in the same format as you entered it, but with the common names and descriptions appended at the end of each row
