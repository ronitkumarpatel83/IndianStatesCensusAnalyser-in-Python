"""
    @Name = Ronit Kumar Patel
    @Title = Indian States Census Analyser
"""
import csv
import logging

print("*************************************************************************")
print("             Welcome to Indian States Census Analyser Program            ")
print("*************************************************************************")

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='indian_states_census_analyser.log', filemode='a', format=log, level=logging.DEBUG)

logging.debug("Indian States Census Analyser logging file !")


class StateCensusAnalyser:
    def read_census_analyser_csv(self):
        try:
            with open("csv_data/census_analyser_csv.csv", "r") as obj:
                file = csv.reader(obj)
                next(file)
                # for i in file:
                #     print(iter(i))
                data = list(file)
                count = len(data)
                if count is 29:
                    print("True")
                else:
                    print("False")

        except Exception as e:
            print(e)
            logging.exception(e)


class CSVStateCensus:
    def delimiter_read_census_analyser_csv(self):
        try:
            with open("csv_data/delimiter_read_census_analyser_csv.csv", "r") as obj1:
                file = csv.reader(obj1)
                next(file)
                # for i in file:
                #     print(iter(i))
                data = list(file)
                count = len(data)
                if count is 29:
                    print("True")
                else:
                    print("False")
        except Exception as e:
            print(e)
            logging.exception(e)


class CSVState:
    def csv_state_code(self):
        try:
            with open("csv_data/csv_state_code.csv", "r") as obj1:
                file = csv.reader(obj1)
                next(file)
                # for i in file:
                #     print(iter(i))
                data = list(file)
                count = len(data)
                if count is 37:
                    print("True")
                else:
                    print("False")
        except Exception as e:
            print(e)
            logging.exception(e)


if __name__ == "__main__":
    try:
        while True:
            print("1.read_census_analyser_csv \n2.delimiter_read_census_analyser_csv\n3.State code\n0.Exit")
            choice = int(input("Enter a number : "))
            if choice == 1:
                data = StateCensusAnalyser()
                data.read_census_analyser_csv()
            elif choice == 2:
                delimiter = CSVStateCensus()
                delimiter.delimiter_read_census_analyser_csv()
            elif choice == 3:
                state_code = CSVState()
                state_code.csv_state_code()
            elif choice == 0:
                break
            else:
                print("Enter valid key")
    except Exception as e:
        print(e)
        logging.exception(e)
