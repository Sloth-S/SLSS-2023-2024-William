a = []
questions = ["Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call your grandma?"]

for i in range(4):
    print(questions[i])
    a.append( input().lower() )

count=0
for ans in a:
    if ans == "yes":
        count+=1

if count == 0:
    print("I'm coming over")
elif count < 3:
    print("Ok")
else:
    print("Good!")
