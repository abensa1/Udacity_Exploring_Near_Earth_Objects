import csv, json

def neos(file='data/neos.csv', lines=5):
    with open(file, 'r') as f:
        neo = csv.DictReader(f)
        for index, row in enumerate(neo):
            if index >= lines:
                break
            print(row['pdes'], row["name"], row["diameter"], row['pha'])
        file = {neo1['pdes']: index for index, neo1 in enumerate(neo)}
        print(list(file.items())[:5])
            
            
def cad(filename='data/cad.json', lines=5):
    with open(filename, 'r') as f:
        json_file = json.load(f)
    json_file = [dict(zip(json_file["fields"], data)) for data in json_file["data"]]
    for index, row in enumerate(json_file):
        if index >= lines:
            break
        print(row['des'], row['cd'], row['dist'], row['v_rel'])
            
neos()
# cad()
        