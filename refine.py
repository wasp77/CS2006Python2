import sys
import time

start_time = time.time()
file = sys.argv[1]
file2 = 'refined_census.csv'
f = open(file, 'r')
title = f.readline()
bad_data = []
inconsistent = False

region = ['E12000001', 'E12000002', 'E12000003', 'E12000004','E12000005',
'E12000006', 'E12000007', 'E12000008', 'E12000009', 'W92000004']
residence_type = ['C', 'H']
family_composition = ['1', '2', '3', '4','5', '6', '-9']
population_base = ['1', '2', '3']
sex = ['1', '2']
age = ['1', '2', '3', '4', '5', '6', '7', '8']
marital_status = ['1', '2', '3', '4', '5']
student = ['1', '2']
county_of_birth = ['1', '2', '-9']
health = ['1', '2', '3', '4', '5', '-9']
ethnic_group = ['1', '2', '3', '4', '5', '-9']
religion = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-9']
economic_activity = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-9']
occupation = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-9']
industry = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '-9']
hours_per_week = ['1', '2', '3', '4', '-9']
approx_social_grade = ['1', '2', '3', '4', '-9']

for line in f:
    line = line.strip()
    fields = line.split(',')
    if len(fields) > 18:
        inconsistent = True
        bad_data.append(line)
        continue
    if len(fields) < 18:
        inconsistent = True
        bad_data.append(line)
        continue
    for num in range(1, 18):
        if num == 1:
            if fields[num] not in region:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 2:
            if fields[num] not in residence_type:
                print(fields[num])
                inconsistent = True
                bad_data.append(line)
                break
        if num == 3:
            if fields[num] not in family_composition:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 4:
            if fields[num] not in population_base:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 5:
            if fields[num] not in sex:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 6:
            if fields[num] not in age:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 7:
            if fields[num] not in marital_status:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 8:
            if fields[num] not in student:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 9:
            if fields[num] not in county_of_birth:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 10:
            if fields[num] not in health:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 11:
            if fields[num] not in ethnic_group:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 12:
            if fields[num] not in religion:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 13:
            if fields[num] not in economic_activity:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 14:
            if fields[num] not in occupation:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 15:
            if fields[num] not in industry:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 16:
            if fields[num] not in hours_per_week:
                inconsistent = True
                bad_data.append(line)
                break
        if num == 17:
            if fields[num] not in approx_social_grade:
                inconsistent = True
                bad_data.append(line)
                break

if inconsistent == True:
    f2 = open(file2, 'w')
    f.seek(0)
    for line in f:
        if line.strip('\n') in bad_data:
            continue
        f2.write(line)
    f2.close()

f.close()

print("My program took", time.time() - start_time, "to run")
