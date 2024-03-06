import csv
import time
from multiprocessing import Process

# Timestamp waarop het programma start (dit wordt het punt Time=0 in de files)
start_time = time.time()

def csv_file():
    '''Lezen van het eerste CSV bestand'''
    filename='2__pressureandflow.xls'
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            current_time = time.time() - start_time
            if current_time < float(row[0]):
                # Wacht juiste tijd af
                time.sleep(float(row[0]) - current_time)
            print(row)

def csv_with_headers():
    '''Lezen van het tweede CSV bestand, met headers waaronder Time'''
    filename='2__monitordata.xls'
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            current_time = time.time() - start_time
            if current_time < float(row['Time']):
                # Wacht juiste tijd af
                time.sleep(float(row['Time']) - current_time)
            print(row)

# Start als verschillende processen zodat ze tegelijk draaien
if __name__ == '__main__':
    p1 = Process(target=csv_file)
    p1.start()
    p2 = Process(target=csv_with_headers)
    p2.start()
    p1.join()
    p2.join()
