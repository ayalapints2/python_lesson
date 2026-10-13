import csv


def count_word(file):
   with open(file,"r") as f:
       content = f.read()
       count =  content.count(" ")
       return count+1

x=count_word("try.text")
print(x)

# ex 2

def get_list(list):

    with open("people.csv","w") as fileCSV:
        content=csv.writer(fileCSV)
        content.writerows(list)
        print(content)
list=[{"name": "ayala"},
      {"less": "pints"},
      {"age": 19},
      {"adress": 105}]
get_list(list)


def create_and_read(dic):
    with open("data.json", "w") as filejson:
        content = csv.writer(filejson)
        content.writerows(dic)
        read=filejson.read()
        print(read)


list2={"name": "ayala",
      "less": "pints",
      "age": 19,
      "adress": 105}
create_and_read(list2)