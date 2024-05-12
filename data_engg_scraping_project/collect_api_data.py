import json, requests

def collect_data(api_link:str):
    try:
        res=requests.get(api_link)
        if res.status_code==200:
            return res.json()
    except Exception as e:
        return e
def data_pre_processing(datas:json):
    final_data=[]
    count=0
    for data in datas:
        pre_processing_data={
            "country_count":count,
            "country_code":data.get("cca3"),
            "country_code_value":data.get("ccn3"),
            "is_independent":data.get("independent"),
            "region":data.get("region"),
            "subregion":data.get("subregion"),
            "area_size":data.get("area"),
            "population":data.get("population"),
            "language":data.get("languages").get(list(data.get("languages").keys())[0]),
            "timezone":data.get("timezones"),
            "currency":data.get("currencies").get(list(data.get("currencies").keys())[0]).get("name")
        }
        final_data.append(pre_processing_data)
        count=count+1
    return final_data
def write_to_file(final_clean_data:list,output_file:str):
    try:
        with open(output_file,'w') as file:
            clean_data_json_str=json.dumps(final_clean_data)
            file.write(clean_data_json_str)
        return 'Successfully write the data to a file.'
    except Exception as e:
        return e
url="https://restcountries.com/v3.1/independent?status=true"
res_data=collect_data(url)
clean_data=data_pre_processing(res_data)
output_file='api_clean_data.json'
status=write_to_file(clean_data,output_file)
print(status)