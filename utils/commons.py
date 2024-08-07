import csv, random

class CsvReader:
    def __init__(self, filePath) -> None:
        try:
            self.file = open(filePath)
            self.reader = csv.DictReader(self.file)
        except FileNotFoundError as err:
            print(err)
            
    def read_file(self):
        return random.choice(list(self.reader))
        