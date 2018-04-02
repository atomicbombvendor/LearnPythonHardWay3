
from htbin import athletemodel, yate
import glob

data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("select an athlete from the list to work with"))

for each_athlete in athletes:
    print(yate.radio_button("Which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home" : "/index.html"}))