import functions
from datetime import date, time, datetime
import re
import sys
import openpyxl
from tabulate import tabulate

#Created for further flexibility
class Record:
    def __init__(self, event, classification, sex):
        if int(classification[1:]) > 64 :
            raise ValueError('Class does not exist')
        self._event = event
        self._classification = classification
        self._sex = sex
        ...

def main():
    inputs = []
    try:
        while True:
            events = ['Long Jump','100 m', '200 m', '400 m', '800 m', '1500 m', '5000 m', '10000 m', 'High Jump', 'Javelin', 'Discus Throw','Shot Put', 'Triple Jump']
            print('Welcome')
            # user options select sex
            while True:
                print('Please select your sex using options: \n1. Male \n2. Female')
                sex = input('')
                if sex not in ['1', '2']:
                    print('Invalid Input \nTry Again!')
                    continue
                else:
                    break
            if sex == '1':sex = 'M'
            if sex == '2':sex = 'W'
            # options select event
            while True:
                print('Please Enter your event:')
                event = input('')
                if event not in events:
                    print('Invalid Input \nTry Again!')
                    continue
                else:
                    break
            if sex == 'M':
                event = f"Men's {event}"
            elif sex =='W':
                event = f"Women's {event}"
            classification = input('What class are you searching for(T or F):').upper()
            record = Record(event,classification, sex)
            inputs.append(record._event)
            inputs.append(record._classification)
            inputs.append(record._sex)
    except EOFError:
        inputs.append(record._event)
        inputs.append(record._classification)
        inputs.append(record._sex)
        database(inputs, input('Time/Distance for comparision:'))

def comparision(wr, time, event):
    field_events = [
    "Men's Long Jump", "Men's High Jump", "Men's Shot Put", "Men's Javelin","Men's Discus Throw", "Men's Triple Jump",
    "Women's Long Jump", "Women's High Jump", "Women's Shot Put", "Women's Javelin","Women's Discus Throw", "Women's Triple Jump"
]
    track_events = [
        "Men's 100 m", "Men's 200 m", "Men's 400 m", "Men's 800 m", "Men's 1500 m", "Men's 5000 m",
        "Women's 100 m", "Women's 200 m", "Women's 400 m", "Women's 800 m", "Women's 1500 m", "Women's 5000 m"
    ]
    if time.strip() == '':
        return 'N/A'
    elif event in track_events:
        wr = wr.split(':')
        mins = int(wr[0]) * 60
        if ':' in time:
            min, time = time.split(':')
            mins1 = int(min) * 60
        else:
            mins1 = 0
        percentage = (mins+float(wr[1])) / (mins1+float(time))* 100
        percentage = round(percentage, 2)
        percentage =f"{percentage}%"
        return percentage

    elif event in field_events:
        percentage = float(time) / float(wr)* 100
        percentage = round(percentage, 2)
        percentage =f"{percentage}%"
        return percentage

    elif event in ["Men's 10000 m", "Women's 10000 m"]:
        wr = wr.split(':')
        mins = int(wr[1]) * 60
        if ':' in time:
            mins1, seconds = time.split(':')
            mins1 = int(mins1) * 60
        else:
            mins1 = 0
        percentage = (mins+float(wr[2])) / (mins1+float(seconds))* 100
        percentage = round(percentage, 2)
        percentage =f"{percentage}%"
        return percentage





def database(inputs, time):
    info = []
    reps = int(int(len(inputs)) / 3)
    y = 0
    path =  "2022_07_12 World Para Athletics Online Records.xlsx"
    wb = openpyxl.load_workbook(path)
    ws =  wb.active
    sex = 2
    event = 0
    classification = 1
    for z in range(1,reps):
        y = 0
        for x in ws.iter_rows():
            try:
                y+= 1
                if y > 6:
                    sex_col = x[1].value
                    event_col = x[2].value
                    classification_col = x[3].value

                    if sex_col == inputs[sex] and inputs[event] == event_col and inputs[classification] ==  classification_col:
                        wr = x[9].value

                        comp = comparision(wr, time, inputs[event])
                        info.append({
                            'EVENT':x[2].value,
                            'FIRST':x[6].value,
                            'LAST':x[5].value,
                            'CLASSIFICATION':classification_col,
                            'TIME/DISTANCE':x[9].value,
                            'NPC':x[7].value,
                            'BIRTH':x[8].value,
                            'WIND':x[10].value,
                            'DATE':x[14].value,
                            'COMPARISION': comp
                        })

            except:
                continue

        sex = sex + 3
        event = event + 3
        classification = classification + 3
    print(table(info))



def table(table):
    return tabulate(table,headers='keys',tablefmt='grid')

if __name__ == '__main__':
    main()
