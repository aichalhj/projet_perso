#Cle API : ac7e5560a7b3ec4021bfb9592b708c0e

import requests

api_key=f'ac7e5560a7b3ec4021bfb9592b708c0e'
city="Montpellier"

#URL de la requête 
url= f'https://api.meteomatics.com/2023-10-19T21:30:00.000+02:00--2023-10-20T21:30:00.000+02:00:PT1H/t_2m:C,sun_elevation:d,sunset:dn,is_rain_30min:idx/43.6112422,3.8767337/html?model=mix?accesstoken=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2IjoxLCJ1c2VyIjoiZmFjdWx0ZGVzc2NpZW5jZXNfbGFoamlvdWpfYWljaGEiLCJpc3MiOiJsb2dpbi5tZXRlb21hdGljcy5jb20iLCJleHAiOjE2OTc3NTEyMzgsInN1YiI6ImFjY2VzcyJ9.Qj23gdDGgzgV2Evt7ok7-WK_jffgpyAujR7VvNmn2bPW7mUTdGj1loB3DiHjzFy8HDt5AgQ7GyG6i2Eztw9lAA'

headers = { 'Authorization': f'Bearer {api_key}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    #Les données metéorologiques vont être stokées dans data
    print(data)
else:
    print("Erreur lors de la requête: {response.status_code}")

