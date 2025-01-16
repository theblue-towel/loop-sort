from middleman import Middleman

middleman = Middleman()
testingList = [66, 60, 40, 38, 64, 75, 73, 58, 52, 60, 70, 72, 62, 60, 84, 57, 47, 46, 58, 39, 60, 50, 82, 60, 51, 53, 56, 71, 45, 70, 59, 61, 49, 49, 60, 72, 38, 58, 57, 65]

res = middleman.sort(testingList)
print(res)