import json
import pandas as pd
import re

# num_there takes in a string
def num_there(s):
    return any(i.isdigit() for i in s) # return true if it contains a digit else return false

# data_format takes in our txt file and will format it to our needs
def data_format(file):
    result = [] # Used to store our records
    # Columns from the data table. Feel free to make any renaming changes to the column headers here
    newcolumns = ["LULC", "HRU", "GIS", "SUB", "MGT", "MON", "AREAkm2", "PRECIPmm", "SNOFALLmm", "SNOMELTmm", "IRRmm", "PETmm", "ETmm", "SW_INITmm", "SW_ENDmm", "PERCmm", "GW_RCHGmm", "DA_RCHGmm", 
            "REVAPmm", "SA_IRRmm", "DA_IRRmm", "SA_STmm", "DA_STmm", "SURQ_GENmm", "SURQ_CNTmm", "TLOSSmm", "LATQGENmm", "GW_Qmm", "WYLDmm", "DAILYCN", "TMP_AVdgC", "TMP_MXdgC", "TMP_MNdg", 
            "CSOL_TMPdg", "CSOLARMJ/m2", "SYLDt/ha", "USLEt/ha", "N_APPkg/ha", "P_APPkg/ha", "NAUTOkg/ha", "PAUTOkg/ha", "NGRZkg/ha", "PGRZkg/ha", "NCFRTkg/ha", "PCFRTkg/ha", "NRAINkg/ha", 
            "NFIXkg/ha", "F-MNkg/ha", "A-MNkg/ha", "A-SNkg/ha", "F-MPkg/ha", "AO-LPkg/ha", "L-APkg/ha", "A-SPkg/ha", "DNITkg/ha", "NUPkg/ha", "PUPkg/ha", "ORGNkg/ha", "ORGPkg/ha", "SEDPkg/ha",
            "NSURQkg/ha", "NLATQkg/ha", "NO3Lkg/ha", "NO3GWkg/ha", "SOLPkg/ha", "P_GWkg/ha", "W_STRS", "TMP_STRS", "N_STRS", "P_STRS", "BIOMt/ha", "LAI", "YLDt/ha", "BACTPct", "BACTLPct", "WTAB",
            "CLIm", "WTAB", "SOLm", "SNOmm", "CMUPkg/ha", "CMTOTkg/ha", "QTILEmm", "TNO3kg/ha", "LNO3kg/ha", "GW_Q_Dmm", "LATQCNTmm", "TVAPkg/ha"]
    
    with open(file) as f:
        lines = f.readlines() # List containing lines of file
        i = 1
        for line in lines:
            line = line.strip() # Remove leading/trailing white spaces
            if line: 
                if i == 1: # Makes sure that we aren't using the header line 
                    i = i + 1
                else:
                    d = {} # Dictionary to store file data (each line)
                    data = [item.strip() for item in line.split()] # Split line items and store in a list
                    for index, elem in enumerate(data): # Loops though each item in data list
                        if index == 0 and num_there(elem) == True: # Checks first element to make sure that it's only the crop name
                            data[0:1] = re.findall(r'(\w+?)(\d+)', elem)[0]  # If element contains a number split string into two items and set new values to our list
                        elif index == 5:
                            data[5:6] =   elem.split(".") # If element contains a "." split string into two items and set new values to our list
                        d[newcolumns[index]] = data[index] # Set our coulmn name as the key and data as the value
                    result.append(d) # Append dictionary to list
    return result

# convert_csv takes in our txt file
def convert_csv(file):
    data_parsed = data_format(file) # The parased/formatted data
    df = pd.DataFrame(data_parsed) # Creates a DataFrame of the formatted data
    df.to_csv (r'C:\Users\Vnguyen\Downloads\test.csv', index=None) # Converts the DataFrame to a CSV file. File path to where you'd like to save the csv file and what you'd like to name it.
    return print("CSV Conversion Completed") # Returns a message to the command line so the user knows when the task is finsihed.

# This is where the csv converter function is being called.
convert_csv(r'C:\Users\Vnguyen\Downloads\testoutput.txt') # File path to your output.txt file goes here
