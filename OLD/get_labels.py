import csv

with open("list_attr_celeba.txt", "r") as file:
    # Skip first line with number of rows
    file.readline()
    
    # Read the header
    header = file.readline().strip().split(" ")
    
    # Get the index of the "Narrow_Eyes" column
    narrow_eyes_index = header.index("Narrow_Eyes") + 1
    
    # Initialize the list of tuples
    data = []
    
    # Loop over the rest of the lines
    for line in file:
        # Split the line into values
        values = line.strip().split()
        
        # Extract the image filename and the Narrow_Eyes value
        filename = values[0]
        narrow_eyes = int(values[narrow_eyes_index])
        
        # Append the tuple to the data list
        data.append((filename, 0 if narrow_eyes == -1 else 1))
        
# Write the list of tuples to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["filename", "closed_eyes"])
    
    # Write the data rows
    writer.writerows(data)