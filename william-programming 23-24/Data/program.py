import os
import csv
class record:
    def __init__(self):
        self.name = "William"
        self.food = "Robux"
        self.movie = "None"
        self.card = 0
        self.city = "HaErBin"

people = list()

current_directory = os.path.dirname(__file__)

data_file = "data.csv"  

data_file_path=os.path.join(current_directory,  data_file)

with open(data_file_path, "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    first = next(csv_reader)
    people.append(first)
    second = next(csv_reader)
    people.append(second)
    print(people[1])
    for person in csv_reader:
        people.append(person)
    pos=int(input())
    print("The information of the",pos,"-th person:", people[pos-1])
    print()
    
    input_food=input()
    sum=0
    for person in people:
        print(person[1].lower())
        if person[1].lower()==input_food.lower():
            sum=sum+1
    print(sum)
    
    start=input()

    sum=0
    for person in people:
        if person[0][0]==start:
            sum=sum+1
    print(sum)
    
    input_place=input()
    sum=0
    for person in people:
        if person[4].lower() ==input_place.lower() :
            sum=sum+1
    print(sum)
    
    sum=0
    counter=0
    for person in people:
        if int(person[3])%2==0:
            sum=sum+1
        counter=counter+1
    print("There are ",sum,"/",counter," people's cards are even number ")
