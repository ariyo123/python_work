import csv
with open('text_files/housing.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)
    textfile = open("split/011/sql.txt", "a")
    # change names in placeholder to match names in csv file.
    sql = """INSERT INTO venues(price,area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
          VALUE (%(price)s,%(area)s,%(bedrooms)s,%(bathroomes)s,%(stories)s,%(mailroad)s,%(guestroom)s,%(basement)s,%(hotwaterheating)s,%(airconditioning)s,%(parking)s,%(prefarea)s,%(furnishingstatus)s)"""
    
    for row in myCSVReader:
        # use row directly
        textfile.write(sql + "\n")