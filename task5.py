#Print days in month
mon=input("Enter month:\n")
mon = mon.lower()
if mon in["april","june","september","november"]: print(30)
elif mon == "february": print(28+"or"+29)
else: print(31)
