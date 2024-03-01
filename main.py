import datetime
import jakes.json
import math

def main():
    data_file = "weight_data.json" #weight_data.json or dev_data.json

    current_date = str(datetime.date.today())
    option = input("read, write, or replace weight data: ")
    print()

    match option.lower():
        case "read":
            data = jakes.json.read(data_file)
            display_formatted(data)

        case "write":
            new_weight = input("weight: ")
            print()

            new_weight = round(float(new_weight),1)
            data = jakes.json.read(data_file)

            if current_date in data:
                old_weight = data[current_date]
                old_weight = float(old_weight)

                average_weight  = round((new_weight + old_weight)/2,1)
                new_weight = average_weight

            data[current_date] = new_weight
            jakes.json.write(data_file,data)

            print("success\n")
        
        case "replace":
            data = jakes.json.read(data_file)
            
            display_last_x(data,3)

            entry_to_change = input("which entry would you like to change: ")
            print()

            if (entry_to_change in data) == False:
                print("invalid input\n")

            else:
                new_weight = input("what is the new weight: ")
                print()
                data[entry_to_change] = new_weight

                jakes.json.write(data_file,data)

                print("success\n")

        case other:
            print("invalid input\n")

def display_formatted(data):
    print()
    for date,weight in data.items():
        print("{} : {}".format(date,weight))

def display_last_x(data,number_of_entrys):
    entrys_displayed = 0
    print()

    reversed_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    for date,weight in reversed_data:
        print(f"{date} : {weight}")
        entrys_displayed += 1

        if entrys_displayed == number_of_entrys:
            break

    print()

if __name__ == "__main__":
    print()
    main()
