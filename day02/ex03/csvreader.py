#!/bin/usr/python3


class CsvReader():

    def __init__(self, csv, sep=",", header=False, skip_top=0, skip_bottom=0):
        self.MAX_LINES = 400
        self.error = None
        try:
            self.csv = open(csv, "r")
            if self.__line_number(self.csv) > self.MAX_LINES:
                raise RuntimeError
        except FileNotFoundError:
            self.error = "CSV file not found."
        except RuntimeError:
            self.error = "File is corrupted."
        else:
            self.sep = sep
            self.header = header
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
        pass

    def __enter__(self):
        if self.error is not None:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if type is not None:
            print(self.error)
            print(value)
        else:
            self.csv.close()
        return True

    def get_data(self):
        data = []
        actual = self.csv.tell()
        if self.header is True:
            self.csv.readline()
        d = self.csv.readline()
        while (len(d) > 0):
            data.append(self.__parse_line(d))
            d = self.csv.readline()
        self.csv.seek(actual)
        return data

    def get_header(self):
        if self.header is False:
            print("No header available.")
            return None
        else:
            actual = self.csv.tell()
            h = self.csv.readline()
            h = self.__parse_line(h)
            self.csv.seek(actual)
            return h

    def __parse_line(self, line):
        line = line.rstrip('\n')
        line = line.split(self.sep)
        line = [i.strip() for i in line]
        return line

    @staticmethod
    def __line_number(file):
        now = file.tell()
        count = 0
        for line in file:
            count += 1
        file.seek(now)
        return count


if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as csv:
        data = csv.get_data()
        header = csv.get_header()
        print(header)
        print(data)
    with CsvReader('bad.csv', header=True) as csv:
        if csv is None:
            print("File is corrupted.")
