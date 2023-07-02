import csv

def extract_bullet_points_from_md(md_file):
    with open(md_file, 'r') as file:
        lines = file.readlines()

    bullet_points = []
    for line in lines:
        line = line.strip()
        if line.startswith('* ') or line.startswith('- '):
            bullet_points.append(line[2:])
        elif line.startswith('1. '):
            bullet_points.append(line[3:])

    return bullet_points

def write_to_csv(bullet_points, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for point in bullet_points:
            writer.writerow([point])

# Usage
md_file = 'example.md'
csv_file = 'bullet_points.csv'

bullet_points = extract_bullet_points_from_md(md_file)
write_to_csv(bullet_points, csv_file)
