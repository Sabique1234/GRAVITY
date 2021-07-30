import csv

rows = []

with open("main.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

headers[0] = 'row_num'

for data in star_data_rows:
    star_mass = data[3]
    if star_mass == '?':
        star_data_rows.remove(data)
        continue
    star_mass_value = star_mass.split(' ')[0]
    star_mass_value = star_mass_value.split('–')[0]
    try:
        star_mass_value = int(star_mass_value)
    except:
        star_mass_value = float(star_mass_value)
    star_mass_value = float(star_mass_value*1.989e+30)
    data[3] = star_mass_value

for data in star_data_rows:
    star_radius = data[4]
    if star_radius == '?':
        star_data_rows.remove(data)
        continue
    star_radius_value = star_radius.split(' ')[0]
    star_radius_value = star_radius_value.split('-')[0]
    star_radius_value = star_radius_value.split('–')[0]
    try:
        star_radius_value = int(star_radius_value)
    except:
        star_radius_value = float(star_radius_value)
    star_radius_value = float(star_radius_value*6.957e+8)
    data[4] = star_radius_value

star_gravity = ["Gravity", ]
star_names = []
star_masses = []
star_radii = []

for data in star_data_rows:
    if data[3] == '?' or data[4] == '?':
        star_data_rows.remove(data)
        continue
    star_names.append(data[1])
    star_masses.append(data[3])
    star_radii.append(data[4])

for index, name in enumerate(star_names):
    gravity = (float(star_masses[index])/(float(star_radii[index])**2))*6.674e-11
    star_gravity.append(gravity)

for index, data in enumerate(star_data_rows):
    star_data_rows[index].append(star_gravity[index])

with open("gravity.csv", 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data_rows)