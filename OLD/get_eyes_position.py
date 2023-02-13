import csv


def parse_eye_coordinates(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        header = lines[1].strip().split(" ")
        eye_index = header.index("lefteye_x") + 1
        result = []
        for line in lines[2:]:
            line = line.strip().split()
            filename = line[0]
            lefteye_x = int(line[eye_index])
            lefteye_y = int(line[eye_index + 1])
            righteye_x = int(line[eye_index + 2])
            righteye_y = int(line[eye_index + 3])
            result.append((filename, lefteye_x, lefteye_y, righteye_x, righteye_y))
        return result

data = parse_eye_coordinates('list_landmarks_align_celeba.txt')
        
# Write the list of tuples to a CSV file
with open("data2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["filename", "lefteye_x", "lefteye_y", "righteye_x", "righteye_y"])
    
    # Write the data rows
    writer.writerows(data)