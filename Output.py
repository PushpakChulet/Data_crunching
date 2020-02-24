import csv

file_1 = "user_email_hash.1m.tsv"
file_2 = "ip_1m.tsv"
file_3 = "plain_32m.tsv"
outputFile = "output.tsv"

dict_1 = {}
with open(file_1, 'r') as src:
    for item in src:
        row = item.strip().split("\t")
        dict_1[row[2]] = row

dict_2 = {}
with open(file_2, 'r') as src:
    for item in src:
        row = item.strip().split("\t")
        dict_2[row[0]] = row[1]

with open(file_3, 'r') as src, open(outputFile, 'w') as out:
    csvWriter = csv.writer(out, delimiter='\t')
    csvWriter.writerow(['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip'])
    for item in src:
        email, pwd = item.strip().split("\t")
        if email in dict_1:
            row = dict_1[email]
            ID = row[0]
            if ID in dict_2:
                IP = dict_2[ID]
                row.append(pwd)
                row.append(IP)
                csvWriter.writerow(row)
                  
