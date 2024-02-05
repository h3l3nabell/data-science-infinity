# working with strings

string1 = "data"
string2 = "science"
string3 = "infinity"

len(string1)

string1.index("d")

string1[3]

string3[3:6]

string1a = string1.replace("d","p")
print(string1 + "" + string1a)

string1.upper()

string1.lower()

string1.title()

string1.split("a")
string1.count("a")

#escape characters
print("don\'t know")

a=123
b=str(a)
type(a)
type(b)

#later versions since 3.6 of python have string formatting with 'f strings'
level = "RED"
error = "Meltdown"
sector = "7G"
contact = "Homer"

alert_string = f"{level} ALERT - {error} in sector {sector}.  Please contact: {contact}"
print(alert_string)

#earlier approach of string formatting
alert_string2 = "{0} ALERT - {1} in sector {2}.  Please contact: {3}".format(level,error,sector,contact)
print(alert_string2)

#super original approach for string formatting for the ancient scripts
alert_string3 = "%s ALERT - %s in sector %s.  Please contact: %s" % (level,error,sector,contact)
print(alert_string3)

