#write code to print out all the meals in the menu, but with spam remove

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if(item == "spam"):
            del meal[top_index - index]
    print(meal)
            
