import requests, json
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/ISO_3166-1_numeric"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", class_="wikitable sortable")
all_data = []
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    country_code = cells[0].text.strip()
    country_name = cells[1].text.strip()
    all_data.append({"Country Code": country_code, "Country Name": country_name})
json_file = "country_code_name_data.json"
with open(json_file, "w") as f:
    json.dump(all_data, f, indent=4)
print(f"My Data saved to {json_file}")