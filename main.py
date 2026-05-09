import csv

#-------------------------------------------------
with open("output.csv", "w", newline="") as file:
    '''
        Write csv file using csv.writer
    '''
    writer = csv.writer(file)
    writer.writerow(["id", "product", "price"])
    writer.writerow([1, "Laptop", 45000])
#--------------------------------------------------



#-------------------------------------------------------------------------
with open("users.csv", "w", newline="") as file:
    '''
        Write csv file using dictionaries
    '''

    fieldnames = ['id', 'name', 'email']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id': 1, 'name': 'Anna', 'email': 'anna@gmail.com'})
#--------------------------------------------------------------------------
