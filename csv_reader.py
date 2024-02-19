import csv

class CSVData:
    def __init__(self, period, env_tempeture, date_time, radiation_intensity):
        self.period = period
        self.env_tempeture = env_tempeture
        self.date_time = date_time
        self.radiation_intensity = radiation_intensity

    def __str__(self):
        return f'Periodo: {self.period}\nTemperatura ambiente: {self.env_tempeture}\nData e hora: {self.date_time}\nIntensidade da radiação: {self.radiation_intensity}\n'

def read_csv(file):
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
            
        next(reader, None)
        for row in reader:
            single = CSVData(row[0], row[1], row[2], row[3])
            data.append(single)

    return data
