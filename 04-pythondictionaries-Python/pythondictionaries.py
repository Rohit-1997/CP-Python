"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def alphaAsia():
    result = []
    asia_data = locations['Asia']
    city_list = asia_data['India']
    city_list.sort()
    for city in city_list:
        ele = city + " - " + 'India'
        result.append(ele)
    return result
    
        

locations = {'North America': {'USA': ['Mountain View', 'Atlanta']}, 'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']}, 'Africa': {'Egypt': ['Cairo']}}
print(locations['North America']['USA'])
print(alphaAsia())

