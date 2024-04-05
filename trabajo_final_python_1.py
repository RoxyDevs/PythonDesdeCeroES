### We use the "csv" standard library for spreadsheet handling
import csv

# DECLARATIVE SECTION
### All the constants are here
### By using this, we avoid the usage of "magic strings" througout the code
### the source and the new file will be in the same folder (./) as the python file 
original_file ='./recursosPython.csv'
file_character_encoding = 'utf-8-sig'

file_by_state ='./recursosPythonFiltradoPorProvincia.csv'
file_setup_for_write_mode ='w'
file_setup_for_new_line =''

column_id = 'DNI'
column_name = 'Nombre'
column_surname = 'Apellido'
column_email = 'Email'
column_bith_date = 'Fecha de nacimiento'
column_location ='Lugar de residencia'

id = 'id'
name='name'
surname='surname'
email='email'
birth_date='birth_date'
location='location'

given_surname_to_filter =['Gomez']
given_location_to_filter =['Santa Fe','Cordoba']

### Here are all the data structures used in the program
converted_file_information = []
information_filtered_by_name = []
information_filtered_by_state = []
information_filtered_for_export_file = []

### this class is used for the columns of the Excel file. The properties from a to f are relatives to the columns A .. F in the excel spreadsheet

class CategorizedData:
    def __init__(self, a, b, c, d, e, f ):
        self.column_list =[a,b,c,d,e,f]

### These are the instances of the clases that we'll use. One for the columns in the original file, and another for the keys in the converted dictionary

excel_columns = CategorizedData(
    column_id,
    column_name,
    column_surname,
    column_email,
    column_bith_date,
    column_location
    )

dictionary_keys = CategorizedData(
    id,
    name,
    surname,
    email,
    birth_date,
    location
)


### By using this function we'll load data during file import/export

def load_dictionary(
    source,destination,
    source_cols,destination_cols
    ):

    number_of_columns_from_source_file = len(source_cols.column_list)
    
    def get_the_dictionary_key(destination_cols,column):
        return destination_cols.column_list[column]

    def get_the_cell_value(source,source_cols,column):
        return source[source_cols.column_list[column]]
        
    row = {
        get_the_dictionary_key(destination_cols,column): get_the_cell_value(source,source_cols,column) 
        for column in range(number_of_columns_from_source_file)
        }
    
    destination.append(row)

### this function loads a dictionary with the key names whoose will be used in te output file

def load_dictionary_formated_for_output_from_source_dictionary(
    source_dictionary,destination_dictionary,
    source_cols,dest_cols
    ):
    destination_dictionary.clear()
    for source_register in source_dictionary:
        load_dictionary(
            source_register,destination_dictionary,
            source_cols,dest_cols
            )

### This function is used to import a file from the spreadsheet into a dictionary list


def import_csv_file(file_path,file_character_encoding):
    converted_file_information.clear()
    with open(file_path,encoding=file_character_encoding) as original_csv_file:
        reader = csv.DictReader(original_csv_file)    
        for ordered_dict in reader:
            load_dictionary(
                ordered_dict,
                converted_file_information,
                excel_columns,
                dictionary_keys
                )

### This function filters the dictionary according to the the search criteria
def filter_by_multiple_search_criteria(
    search_key,
    search_values, 
    source_dictionary, 
    destination_dictionary,
    source_dictionary_columns,
    destination_dictionary_columns
    ):
    destination_dictionary.clear()
    for dictionary in source_dictionary:
        search_criteria = dictionary[search_key].lower()
        for index in range(len(search_values)):
            if search_criteria == search_values[index].lower():
                load_dictionary(
                    dictionary,
                    destination_dictionary,
                    source_dictionary_columns,
                    destination_dictionary_columns
                    )
                
### This function prints de data for the filtered people
def print_filtered_information():
    print('Estas son los datos de las personas cuyo apellido es','Gomez')
    total = len(information_filtered_by_name)
    count =1
    for person_filtered_data in information_filtered_by_name:
        print()
        print(
        count,'de',total,':',
        person_filtered_data[name].upper(), person_filtered_data[surname].upper()
        )
        print('DNI:',person_filtered_data[id])
        print('Email:',person_filtered_data[email])
        print('Fecha de nacimiento:',person_filtered_data[birth_date])
        print('Lugar de residencia:',person_filtered_data[location])
        print('-------------------------------------------------------------')
        count = count + 1
        
### This function prints the new file with the filtered data
def write_new_file_csv():
    with open(
    file_by_state,file_setup_for_write_mode,newline=file_setup_for_new_line
    )as destination_csv_file:
        fieldnames=excel_columns.column_list
    
        csv_dictionary_writer = csv.DictWriter(destination_csv_file,fieldnames=fieldnames)
        csv_dictionary_writer.writeheader()
    
        for dictionary in information_filtered_for_export_file:
            csv_dictionary_writer.writerow(dictionary)
# EXECUTIVE SECTION 

### In this section we call all the functions  previusly declared

import_csv_file(original_file,file_character_encoding)

filter_by_multiple_search_criteria(
    surname,
    given_surname_to_filter,
    converted_file_information, 
    information_filtered_by_name,
    dictionary_keys,
    dictionary_keys
    )

filter_by_multiple_search_criteria(
    location,
    given_location_to_filter,
    converted_file_information, 
    information_filtered_by_state,
    dictionary_keys,
    dictionary_keys
    )

load_dictionary_formated_for_output_from_source_dictionary(
    information_filtered_by_state,
    information_filtered_for_export_file,
    dictionary_keys,
    excel_columns
    )

# OUTPUT SECTION 

print_filtered_information()

write_new_file_csv()