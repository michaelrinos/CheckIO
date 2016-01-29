'""
Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").

source: Wikipedia example

An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".
The result will be a morse time string with specific format:

"h h : m m : s s"

where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).
Output: The morse time string as a string.

Precondition:
time_string contains correct time. 

"""

def nsize(size):
    if size == "5":
        return "6"
    elif size == "4":
        return "6"
    else:
        return "5"

def checkio(string):
    temp = ""
    parts = string.split(":")
    size = "4"
    for i in range(len(parts)):
        if len(parts[i])<2:
            temp += (int(size)-2) * '.'
            temp+= " "
            size = nsize(size)
        for j in parts[i]:
            temp += format(int(j), "#0"+ size +"b")[2:]
            temp+=" "
            size = nsize(size)
        temp+= ": "
    temp = temp.replace("1", "-")
    temp = temp.replace("0", ".")
    print()
        
    return temp[:-3]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"


