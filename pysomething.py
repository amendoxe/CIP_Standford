# containers type
# list, dictionary, tuple
tuplies = ("something", "another", "anothother")
print(type(tuplies))

listing = ["one", "two", "three", "four"]

print(type(listing))

dictating = {"one": "word", "two": "wording", "three": "warding", "four": "werdaining"}

print(type(dictating))
print("now some slicing I suppose")

print(f"middle one:\n {tuplies[0:2]}")
print("third one:\n ", listing[1:3])
print("last one:\n", dictating["two"])
