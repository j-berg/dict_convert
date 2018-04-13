import csv, collections
from collections import defaultdict
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Make sure the column you want it to grab the sys.name from is labeled 'ORF name'\nmake sure yeast_orf_dict file is in the same path as where you are working from\n")
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()

#populate dictionaries
common_dict = defaultdict(lambda: defaultdict(list))
process_dict = defaultdict(lambda: defaultdict(list))
descript_dict = defaultdict(lambda: defaultdict(list))

with open ("./yeast_orf_dict.csv", mode='r') as infile:
    dict_raw = csv.reader(infile)

    for col in dict_raw:
        common_dict[col[0]] = col[1]
        process_dict[col[0]] = col[2]
        descript_dict[col[0]] = col[3]

#process file of interest
with open (args.input_file, mode='r') as infile:
    df = pd.read_csv(infile)
df["Common_Name"] = ""
df["Process"] = ""
df["Description"] = ""

df['Common_Name'] = df['ORF name'].map(common_dict)
df['Process'] = df['ORF name'].map(process_dict)
df['Description'] = df['ORF name'].map(descript_dict)

df.to_csv(args.output_file,sep=",")
