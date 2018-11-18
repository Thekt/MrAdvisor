import csv

def calendar_writer(file_name: str, final_calendar: list)->None:
    """writes the final calendar (list of dicts) to a csv table named file_name which will be located in the folder containing the code"""
    file = open(file_name,'w',encoding="utf-8")#here we force the encoding to be utf-8 to avoid display bugs
    writer = csv.DictWriter(file, fieldnames = list(final_calendar[0].keys()))
    writer.writeheader()
    writer.writerows(final_calendar)
    file.close()

def csv_reader(file_path: str)->list:
    """reads the csv table named file_name and converts it to a list of dicts"""
    file = open(file_path,'r')
    output_list = [{k: v for k, v in row.items()} for row in csv.DictReader(file)]
    return output_list
    #example of use: csv_reader('C:/Users/Thomas/Jupyter Files/CSV-JSON-XML-CocaCola.csv')
    
