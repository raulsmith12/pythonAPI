from urllib.request import urlopen
import json

url = 'https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=7afe7233-fae0-4024-bc98-3a72f05675bd&limit=5'
url_result = urlopen(url)
raw_data = url_result.read()
json_data = json.loads(raw_data)
result = json_data['result']
records = result['records']

filename = 'Storm_Tide_Data.csv'
f = open(filename, 'w')

headers = 'Site, DateTime, Water Level, Prediction, Residual\n'
f.write(headers)

for record in records:
    row_string = ''
    row_string += record['Site'] + ','
    row_string += record['DateTime'] + ','
    row_string += str(record['Water Level']) + ','
    row_string += str(record['Prediction']) + ','
    row_string += str(record['Residual']) + '\n'
    f.write(row_string)
