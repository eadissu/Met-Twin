import pandas as pd
import requests

# URL of the Met Museum Open Access API
url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'

# Making a GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    if 'total' in data:
        print(f"Total objects in the collection: {data['total']}")
    else:
        print("Key 'total' not found in the response data")
else:
    print(f'Failed to retrieve data: {response.status_code}')


'''
# Path to the CSV file
csv_file_path = 'openaccess/MetObjects.csv'

# Read the CSV file
data = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe
print(data)
'''