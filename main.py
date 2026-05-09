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


#--------------------------------------------------------------------------
rows = []

with open("students.csv", "r") as file:
    '''
        Reads file and adds a value to MEMORY (rows[]) if condition is true
    '''
    reader = csv.DictReader(file)
    for row in reader:
        if row['Name'] == 'Ana':
            row['Course'] = 'BSDS'
        rows.append(row)

with open("students.csv", "w", newline="") as file:
    '''
        Writes the values in MEMORY into the CSV file
    '''
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
#-----------------------------------------------------------------


filtered_rows = []

with open("students.csv", "r") as file:
    '''
        Reads the csv and stores the records that meet the condition in memory.
    '''
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['Score']) >= 80:
            filtered_rows.append(row)

with open("students.csv", "w", newline="") as file:
    '''
        overwrites the csv file with the values stored in memory. 
    '''
    writer = csv.DictWriter(file, fieldnames=filtered_rows[0].keys())
    writer.writeheader()
    writer.writerows(filtered_rows)


