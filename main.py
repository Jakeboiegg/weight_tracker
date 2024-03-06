# main, but with new data structure
import json
import datetime

data_file = "weight_data.json"

def main():
    print()
    option = input ("read, write, or replace weight data: ")
    print()

    match option.lower():

        case "read":
            option_read(data_file)

        case "write":
            option_write(data_file)

        case "replace":
            option_replace(data_file)

        case "dev":
            option_dev(data_file)

        case others:
            print ("Invalid input")

    print()

def read(file_name):
    with open(file_name,"r") as file:
        data = json.load(file)
        return data

def write(file_name,data_entry):
    with open(file_name,"w") as file:
        json.dump(data_entry,file)

def option_read(data_file):
    data = read(data_file)
    for date,array in data.items():
        weight = array[0]
        print (f"{date} : {weight}")

def option_write(data_file):
    current_date = str(datetime.date.today())
    new_weight = float(input("What is your weight at this moment: "))

    data = read(data_file)
    if current_date in data.keys():
        number_of_entrys = data[current_date][1]
        old_weight = float(data[current_date][0])

        average_weight = ((old_weight * number_of_entrys) + new_weight)/(number_of_entrys + 1)
        average_weight = round(average_weight,1)
        data[current_date] = [str(average_weight),number_of_entrys+1]
    else:
        data[current_date] = [str(new_weight),1]

    write(data_file,data)
    print(\nsuccess)

def option_replace(data_file):
    data = read(data_file)
    display_last_x(data,3)
    print()

    date_to_edit = input("What is the date to edit: ")

    if (date_to_edit in data) == False:
        print("\ninvaild date")
    else:
       new_weight = float(input("What is your new edited weight: "))
       new_weight = str(round(new_weight,1))
       data[date_to_edit] = [new_weight,1]

       print(new_weight)
       print(data[date_to_edit])

       write(data_file,data)
       print("\nsucess")

def display_last_x(data,number_to_display):
    entrys_displayed = 0

    for date,array in sorted(data.items(), reverse=True):
        weight = array[0]
        print(f"{date} : {weight}")

        entrys_displayed += 1
        if entrys_displayed >= number_to_display: break


def option_dev(data_file):
    if data_file == "dev_data.json":
        data = {
            "2024-03-01":["44.3",1],
            "2024-03-02":["43.5",3],
            "2024-03-03":["43.7",2],
            "2024-03-04":["44.2",5],
            "2024-03-05":["42.5",4],
        }
        write(data_file,data)
        print("written file")
    else:
        print("file not dev_data.json, change data_file variable")

if __name__ == "__main__":
    main()
