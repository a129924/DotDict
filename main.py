from collection.dot_dict import DotDict

mydict = DotDict()

mydict[123][789] = 456
mydict["ABC"] = "CDE"
# mydict["ABC"]["BCD"] = "123"

print(mydict)