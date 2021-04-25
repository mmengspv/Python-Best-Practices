yearList = [1600, 2000, 1500, 2004, 2008, 2010]

for year in yearList:
    if(year%400 == 0):
        isLeapyear = "true"
    elif(year%100 != 0 and year%4 == 0):
        isLeapyear = "true"
    else:
        isLeapyear = "false"
    print(year," -> ", isLeapyear)
