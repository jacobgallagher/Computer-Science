# dictionairy is a type of collection like a list
# a list is a colletion of items in a sequence
# a dictionairy is different
# dicitionaires store data in key-value pairs
# you can retrieve data quickly by using a unique key
# instead of retrieving it by index (position)

# example
# lists use brackets [], dictionaries use braces {}

jacob = {
    "name": "Jacob",
    "age": 17,
    "city": "Saint Michael",
    "pets": 1,
    "height": 5.8,
    5: 6
}

# each key must be unique                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                        
# retrieving values from a dictionary                                                                                                                                                                                                                                                                       
print(jacob["name"])  # prints the name                                                                                                                                                                                                                                                                     
print(jacob["age"]) # prints the age                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        
# this will error if you give a key that doesnt exist                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                        
#print(jacob["country"]) this errors                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        
# .get allows you to retrieve a value without erroring                                                                                                                                                                                                                                                                      
# when the key doesnt exist                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        
print((jacob.get("height")))                                                                                                                                                                                                                                                                        
print(jacob.get("country", "Country not found"))                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        
# you can add new values to an existing dict                                                                                                                                                                                                                                                                        
jacob["country"] = "USA"                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                        
# you can modify existing vlues                                                                                                                                                                                                                                                                     
jacob["age"] = 16                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                        
# you can remove ecisting values                                                                                                                                                                                                                                                                        
jacob.pop("pets")                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                        
# iterate through a dictionairy using a for loop!                                                                                                                                                                                                                                                                       
for key, value in jacob.items():                                                                                                                                                                                                                                                                        
    print(str(key) + " = " + str(value))                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                        
# dictionairy functions                                                                                                                                                                                                                                                                     
print(jacob.keys())     #returns all keys                                                                                                                                                                                                                                                                       
print(jacob.values())   #returns all values                                                                                                                                                                                                                                                                     
print(jacob.items())    #returns all key value pairs                                                                                                                                                                                                                                                                        
print(jacob.clear())    #returns all items from the dictionairy                                                                                                                                                                                                                                                                     