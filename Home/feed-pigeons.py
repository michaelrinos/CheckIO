"""
 I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?

pigeons

Input: A quantity of portions wheat as a positive integer.

Output: The number of fed pigeons as an integer.

Precondition: 0 < N < 105. 
"""

def checkio(number):
    count = 0
    num = 0
    x = [1]
    while number > 0:
        for i in range(len(x)):
            if x[i] == 1:
                if number < 1:
                    return count
                count+=1
                
            number -= 1
            x[i] += 1
        for i in range(num +2):
            x.append(1)
        
        num += 1
        
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"

