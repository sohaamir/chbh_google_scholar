import csv

# # List of names to be written into the CSV file
# names = [
#     "Alan Wing",
#     "Andrea Krott",
#     "Kim Shapiro",
#     "Craig McAllister",
#     "Clare Anderson",
#     "Rachel Upthegrove",
#     "Dietmar Heinke",
#     "Lei Zhang",
#     "Magda Chechlacz",
#     "Joseph Galea",
#     "Massimiliano (Max) Di Luca",
#     "Jennifer Cook",
#     "Matthew Apps",
#     "KyungMin An",
#     "Katja Kornysheva",
#     "Andrew J. Bremner",
#     "Ali Mazaheri",
#     "Hamid Dehghani",
#     "Damian Cruse",
#     "Patricia Lockwood",
#     "Ned Jenkinson",
#     "Tom Rhys Marshall",
#     "Chris Miall",
#     "Stephane De Brito",
#     "Romy Froemer",
#     "Anna Kowalczyk",
#     "Suzanne Higgs",
#     "Sarah Aldred",
#     "Andrew Bagshaw",
#     "Rickson C. Mesquita",
#     "Martin Wilson",
#     "Davinia Fernández-Espejo",
#     "Andrew Quinn",
#     "Hyojin Park",
#     "Karen Mullinger",
#     "Arkady Konovalov",
#     "Felipe Orihuela-Espina",
#     "Carmel Mevorach",
#     "Paul Muhle-Karbe",
#     "Clayton Hickey",
#     "Katrien Segaert",
#     "Nick Holmes",
#     "Sam Lucas",
#     "Ole Jensen",
#     "Barbara Pomiechowska",
#     "Jian Liu",
#     "Steven Frisson",
# ]

# # Specify the path for the CSV file to be saved
# csv_file_path = "names_and_citation_ids.csv"

# # Writing names to a CSV file
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "citation_id"])  # Writing the header
    
#     # Writing each name with a placeholder for citation_id
#     for name in names:
#         writer.writerow([name, ""])

# print(f"CSV file has been created at {csv_file_path}.")

# Specify the path of the original CSV file
original_csv_path = "names_and_citation_ids.csv"

# Specify the path for the new CSV file to be created
filtered_csv_path = "filtered_names_and_citation_ids.csv"

# Open the original CSV file for reading
with open(original_csv_path, mode='r', newline='', encoding='utf-8') as infile:
    # Open the new CSV file for writing
    with open(filtered_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        # Create a CSV DictReader to read the original file
        reader = csv.DictReader(infile)
        # Create a CSV DictWriter to write to the new file, using the fieldnames from the reader
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        # Write the header row to the new file
        writer.writeheader()
        
        # Iterate over each row in the original file
        for row in reader:
            # Check if the 'citation_id' column is not empty
            if row['citation_id'].strip():
                # If 'citation_id' is not empty, write the row to the new file
                writer.writerow(row)

print("Filtered CSV file has been created.")