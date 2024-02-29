import csv

class CSVData:
    def __init__(self, period, env_temperature, date_time, radiation_intensity):
        self.period = period
        self.env_temperature = env_temperature
        self.date_time = date_time
        self.radiation_intensity = radiation_intensity

    def __str__(self):
      return f'{{"period": "{self.period}", "env_temperature": "{self.env_temperature}", "date_time": "{self.date_time}", "radiation_intensity": "{self.radiation_intensity}"}}'

def read_csv(file):
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
            
        next(reader, None)
        for row in reader:
            single = CSVData(row[0], row[1], row[2], row[3])
            data.append(single)

    return data
