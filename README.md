# Weight tracker
just a fun project to track my declining bmi

## features (that are implemented)
- read, write weights
- replace weight that are mistakenly typed in

## to be implemented
- graph
- bmi
- height?
- gui

# dev stuff
just to remind your stupid dev

there is a separate data file, set the file at the top of 'main'

### data format:
{ date, [ weight, number_of_entrys ] } 
{ "2024-03-05", [ "43.7", 3 ] }

where:
- date is date (string)
- weight is weight (string) (because float is not allowed in array)
- number_of_entrys is number of times user entered weight that day (int)
number_of_entrys is to more accurately compute average of weights


