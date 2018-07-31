gotCitiesCSV = "King's Landing,Braavos,Volantis,Old Valyria,Free Cities,Qarth,Meereen"

lotrCitiesList = ["Mordor","Gondor","Rohan","Beleriand","Mirkwood","Dead Marshes","Rhun","Harad"]

bestThing = "The best thing about a boolean is even if you are wrong you are only off by a bit"

print ( "1. Display an list from the cities in gotCitiesCSV ")
print (gotCitiesCSV.split(','))

print ("2. Display an list of words from the sentence in bestThing")
print (bestThing.split(" "))

print ("3. Display a string separated by semi-colons instead of commas from gotCitiesCSV")
print (gotCitiesCSV.replace(',',':'))

print ("4. Display a CSV (comma-separated) string from the lotrCitiesList")
print (','.join(lotrCitiesList))

print('5. Display the first 5 cities in lotrCitiesList')
print(lotrCitiesList[0:5])

print('6. Display the last 5 cities in lotrCitiesList')
print(lotrCitiesList[-5:])

print('7. Display the 3rd to 5th city in lotrCitiesList')
print(lotrCitiesList[2:5])

print('8. Using built-in methods, remove "Rohan" from lotrCitiesList')
lotrCitiesList.remove('Rohan')
print(lotrCitiesList)

print('9. Using built-in methods, remove all cities after "Dead Marshes" in lotrCitiesList')
lotrCitiesList=lotrCitiesList[0:lotrCitiesList.index("Dead Marshes")+1]
print (lotrCitiesList) 

print('10. Using built-in methods, add "Rohan" back to lotrCitiesList right after "Gondor"')
lotrCitiesList.insert(lotrCitiesList.index("Gondor")+1,"Rohan")
print(lotrCitiesList)

print('11. Using built-in methods, rename "Dead Marshes" to "Deadest Marshes" in lotrCitiesList')
lotrCitiesList[lotrCitiesList.index("Dead Marshes")] = 'Deadest Marshes'
print(lotrCitiesList)

print('12. Using built-in methods, display the first 14 characters from bestThing')
print (bestThing[0:14])

print('13. Using built-in methods, display the last 12 characters from bestThing')
print (bestThing[-12:])

print('14. Using built-in methods, display characters between the 23rd and 38th position of bestThing (i.e., "boolean is even")')
print (bestThing[23:39])

print('15. Find and display the index of "only" in bestThing')
print(bestThing.find('only'))

print('16. Find and display the index of the last word in bestThing')
print( bestThing.rfind(' ')+1)

print('17. Find and display all cities from gotCitiesCSV  that use double vowels ("aa","ee", etc.)')
print ([word for word in gotCitiesCSV.split(',') if any(x in word for x in ['aa','ee','ii','oo','uu'])])

print('18. Find and display all cities from lotrCitiesList that end with "or"')
print ([city for city in lotrCitiesList if city.endswith('or')])

print('19. Find and display all the words in bestThing that start with a "b"')
print ([word for word in bestThing.split(" ") if word.startswith('b')])

print('20. Display "Yes" or "No" if lotrCitiesList includes "Mirkwood"')
if "Mirkwood" in lotrCitiesList:
    print("Yes")
else: 
    print("No") 

print('21. Display "Yes" or "No" if lotrCitiesList includes "Hollywood"')
if "Hollywood" in lotrCitiesList:
    print("Yes")
else: 
    print("No") 

print('22. Display the index of "Mirkwood" in lotrCitiesList')
print(lotrCitiesList.index("Mirkwood"))

print('23. Find and display the first city in lotrCitiesList that has more than one word')
index=None
for i in range(0,len(lotrCitiesList)):
    if ' ' in lotrCitiesList[i]:
        index=i
        break
print (index)

print('24. Reverse the order in lotrCitiesList')
lotrCitiesList.reverse()
print(lotrCitiesList)

print('25. Sort lotrCitiesList alphabetically')
lotrCitiesList.sort()
print(lotrCitiesList)

print('26. Sort lotrCitiesList by the number of characters in each city (i.e., shortest city names go first)')
lotrCitiesList.sort(key=len)
print (lotrCitiesList)

print('27. Using built-in methods, remove the last city from lotrCitiesList')
removed_city=lotrCitiesList.pop()
print (lotrCitiesList)

print('28. Using built-in methods, add back the city from lotrCitiesList that was removed in #29 to the back of the list')
lotrCitiesList.append(removed_city)
print (lotrCitiesList)

print('29. Using built-in methods, remove the first city from lotrCitiesList')
removed_city=lotrCitiesList.pop(0)
print (lotrCitiesList)

print('30. Using built-in methods, add back the city from lotrCitiesList that was removed in #31 to the front of the list')
lotrCitiesList.insert(0,removed_city)
print (lotrCitiesList)