# Enter your answrs for chapter 6 here
# Name:


# Ex. 6.6
'''
def first(word): return word[0] //returns the first letter from string
def last(word): return word[-1]	//returns last letter of string
def middle(word): return word[1:-1] //returns middle letters of the string
'''
'''
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print is_palindrome('meet')
print is_palindrome('bob')
print is_palindrome('otto')
print is_palindrome('redivider')
'''




# Ex 6.8

def gcd(a,b):
	if  isinstance(a, str) or  isinstance(b,str):
		print "a and b be should not be string"

	if b==0:
		return a;
	else:
		r=a%b
		return gcd(b,r)


