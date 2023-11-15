import re
lst = [0, 1, 245.0, 3.17, "2.50", "eight", False, "", True]

for i in lst:
    var_type = str(type(i))
    index1 = int(var_type.index("'"))+1
    index2 = int(var_type.rfind("'"))
    print(var_type[index1: index2])
