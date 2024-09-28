import re

# import argparse # start code for arguments

# parser = argparse.ArgumentParser()

# parser.add_argument("-t", "--text", help="the input for your brackets", type=str)
# parser.add_argument("-l", "--loglevel", help="The level of logs/ Values are: 1..5", type=int)

# argmt = parser.parse_args()


# import logging # start code for loggers

# handler = logging.StreamHandler()
# handler.setFormatter("%(%d/%m/%Y %I:%M:%S %p)s |%(levelname)s| %(message)s")
# handler.setLevel(int(argmt.loglevel)*10)

# logger = logging.getLogger()
# logger.addHandler(handler)



# if argmt.t:
#     s = argmt.t
# else:
#     s = input("Enter brackets: ")




# def func(text1):
#     for c1 in text1+" ":
#         if c1 == "{":
#             text2 = text1.replace("{", "", 1)
#             for c2 in text2+" ":
#                 if c2 == "}":
#                     text3 = text2.replace("}", "", 1)
#                     if func(text3):
#                         return True
#                     else:
#                         return False
#                 elif c2 == "{":
#                     continue
#                 else:
#                     return False
#         elif c1 == "}":
#             return False
#         else:
#             return True



# if "[}{]" in s:
#     for c in s:
#         if c != "[}{]":
#             s.replace(c, "")
#     if func(s):
#         print("Well done!")
#         input("Press <Enter> to continue...")
#     else:
#         print("You haven't closed or openned a bracket!")
#         input("Press enter to continue...")
# else:
#     print("You didn't entered any brackets.\nWe have nothing to do.")

s = input("Enter:")



def func(text1):
    text2 = text1.replace("{}", "")
    if text2 == "":
        return True
    elif text2 == text1:
        return False
    elif func(text2):
        print("Well done!")
    else:
        print("You did somthing wrong!")


if "[}{]" in s:
    for c in s:
        if c != "[}{]":
            s.replace(c, "")
    func(s)
else:
    print("we have nothing to do.")




