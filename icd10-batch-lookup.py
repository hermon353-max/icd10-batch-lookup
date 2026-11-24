import requests

url = "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search"

def lookup(diagnosis):
    params = {"terms": diagnosis, "sf": "code,name", "maxList": 20}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    results = data[3]

    print("\n" + diagnosis.upper())
    for pair in results:
        print(pair[0], pair[1])

diagnoses = ["asthma", "hypertension", "type 2 diabetes"]

for dx in diagnoses:
    resuls = lookup(dx)
    print("\n" + dx.upper())
    for pair in results:
        print(pair[0], pair[1])
        
def check_code(code):
