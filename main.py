import requests
import sys
import csv


url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":"Washington,DC,USA","contentType":"csv","unitGroup":"us","shortColumnNames":"0"}

headers = {
    'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
    'x-rapidapi-key': sys.argv[1]
    }

response = requests.request("GET", url, headers=headers, params=querystring)


class WeatherForecast:
    def __init__(self):
        # self.data = data
        self.pogoda = {}
        self.data_pogoda = []

    def zapisz_url_do_pliku(self):
        with open('pogoda.csv', 'w', newline="\n") as f:
            writer = csv.writer(f)
            reader = csv.reader(response.text.splitlines(), delimiter=',', quotechar='"')
            for line in reader:
                writer.writerow(line)

    def wczytaj_plik_i_zapisz_do_slownika(self):
        with open('pogoda.csv') as file:
            reader = csv.reader(file)
            for linia in reader:
                self.pogoda[linia[1]] = linia[21]
                self.data_pogoda.extend([linia[1], linia[21]])

    def __iter__(self):
        for k, v in self.pogoda.items():
            yield k, v

    def __getitem__(self, item):
        return self.pogoda.get(item)

    def items(self):
        for v in self.data_pogoda:
            yield v


wf = WeatherForecast()
wf.zapisz_url_do_pliku()
wf.wczytaj_plik_i_zapisz_do_slownika()
print(wf['12/22/2021'])

for v in wf.items():
    print(v)

for data, pogoda in wf:
    print(data, pogoda)
