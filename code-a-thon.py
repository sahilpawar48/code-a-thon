  
import csv  
    
# field names  
fields = ['empName', 'empNO', 'street', 'city', 'code']  
    
# data rows of csv file  
rows = [ ['Nikhil', '101', 'Rm road', 'thane','400605'],  
         ['Sanchit','102', 'hg road', 'thane','400605'],  
         ['Aditya', '103', 'sg road', 'thane','400605'],  
         ['Sagar', '104', 'ysd road', 'thane','400605'],  
         ['Prateek', '105', 'Rjo road', 'thane','400605'],  
         ['Sahil', '106', 'Rh road', 'thane','400605']]  
    
# name of csv file  
filename = "employee.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows)


