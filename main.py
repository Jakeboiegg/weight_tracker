import datetime
import jakes.json
import math

def main():
    current_date = str(datetime.date.today())
    option = input("Read, write, or replace weight data: ")
    match option.lower():
        case "read":
            data = jakes.json.read("data.json")
            display_formatted(data)

        case "write":
            new_weight = round(float(input("weight: ")),1)
            data = jakes.json.read("data.json")

            if current_date in data:
                old_weight = data[current_date]

                average_weight  = round((new_weight + old_weight)/2,1)
                new_weight = average_weight

            data[current_date] = new_weight
            jakes.json.write("data.json",data)
        
        case "replace":
            new_weight = round(float(input("weight: ")),1)
            data = jakes.json.read("data.json")
            data[current_date] = new_weight
            jakes.json.write("data.json",data)


        case other:
            print("invalid input")

def display_formatted(data):
    for date,weight in data.items():
        print("{} : {}".format(date,weight))

if __name__ == "__main__":
    main()
