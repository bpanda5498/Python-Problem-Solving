import json

with open('country_code_name_data.json', 'r') as file:
    country_data = json.load(file)

with open('api_clean_data.json', 'r') as file:
    country_value = json.load(file)

country_code_map = {item['Country Code']: item['Country Name'] for item in country_data}
for item in country_value:
    country_code = item['country_code_value']
    item['country_code_value'] = country_code_map[country_code]
def write_to_file(final_clean_data:list,output_file:str):
    try:
        with open(output_file,'w') as file:
            clean_data_json_str=json.dumps(final_clean_data)
            file.write(clean_data_json_str)
        return 'Successfully write the data to a file.'
    except Exception as e:
        return e
output_file='country_clean_data.json'
status=write_to_file(country_value,output_file)
print(status)