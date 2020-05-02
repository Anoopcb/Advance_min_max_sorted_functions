### advance min, max, and sorted function

names = ["Anoop", "pi", "Shalinimitra"]


print(min(names, key= lambda  item: len(item)))

print(max(names, key= lambda  item: len(item)))

students = {
    "Anoop": {"score" : 90, "age": 24},
    "Pi" : {"score": 105, "age": 37},
    "Shalini": {"score": 120, "age": 38}

}

print(max(students, key= lambda  item: students[item]["score"]))

## sorted function

names.sort()
print(names)

# you can't use sort() method

## doc string

print(sum.__doc__)

print(max.__doc__)
