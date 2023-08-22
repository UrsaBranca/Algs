#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
#Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 42145 Output: 54421
a = 42145
b = str(a)[::-1]
print(b)


#In this kata, you are asked to square every digit of a number and concatenate them.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

#Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
#Note: The function accepts an integer and returns an integer.
a = str(9119)
b = ''.join(map(lambda i: str(int(i)**2), a))
print(b)


#Given an array of integers, find the one that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

#Examples
#[7] should return 7, because it occurs 1 time (which is odd).
#[0] should return 0, because it occurs 1 time (which is odd).
#[1,1,2] should return 2, because it occurs 1 time (which is odd).
#[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
#[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

import collections 

a = [7]
c = collections.Counter(a)
b = list(filter(lambda i: c[i] % 2 !=0, c))
print(b)


#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
#which is the number of times you must multiply the digits in num until you reach a single digit.

#For example (Input --> Output):
#39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
#999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
#4 --> 0 (because 4 is already a one-digit number)

import numpy as np

def persistence(num):
  num_list = list(map(int, str(num)))  # num -> list of ints
  mult = np.prod(np.array(num_list))   # multiply list's elements
  print(num, num_list, mult)
  i = 1
    
  while mult // 10 > 0:
    num = mult
    num_list = list(map(int, str(num)))
    mult = np.prod(np.array(num_list))
    print(num, num_list, mult)
    i += 1

  return i if i > 1 else 0
  
num = 39
print(persistence(num))


#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

import codewars_test as test
import collections

def duplicate_count(text):
    d_count = collections.Counter(text.lower())
    dupl_count = sum(map(lambda chr: d_count[chr] > 1, d_count))
    return dupl_count

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2


#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
#We want to create the text that should be displayed next to such an item.

#Implement the function which takes an array containing the names of people that like an item. 
#It must return the display text as shown in the examples:

#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
#Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    s = ''
    match len(names):
        case 0:
            return_string = 'no one'
            s = 's'
        case 1:
            return_string = names[0]
            s = 's'
        case 2:
            return_string = names[0] + ' and ' + names[1]
        case 3:
            return_string = names[0] + ', ' + names[1] + ' and ' + names[2]
        case _:
            return_string = names[0] + ', ' + names[1] + ' and 2 others'
  
    return f"{return_string} like{s} this"
    
import codewars_test as test

@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
    
#Snail Sort
#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

#array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]
#For better understanding, please follow the numbers of the next array consecutively:

#array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
#snail(array) #=> [1,2,3,4,5,6,7,8,9]    


def snail(array):
    straight_snail = []
    i = len(array)
    # универсальный вариант
    #
    # direction = 1
    # while i > 1:
    #     back = (1 - direction) // 2
    #     m = (i-1)*back
    #     n = (i-1)*(1-back)
    #     for j in range(direction, (i + 1) * direction, direction):
    #         straight_snail.append(array[m][j - 1 + back])
    #     for k in range(direction, i * direction, direction):
    #         straight_snail.append(array[k-back][n])
    #         array[k-back].pop(n)
    #     array.pop(m)
    #     i -= 1
    #     direction *= -1

    # еще 1 вариант - с поворотом уменьшенной на каждом шаге матрицы на 180 гр.
    # т.е., нам не надо каждый раз менять направление обхода и жонглировать номерами строки и столбца
    #
    while i > 1:
        for j in range(0, i):
            straight_snail.append(array[0][j])
        for k in range(1, i):
            straight_snail.append(array[k][i-1])
            array[k].pop(i-1)
        array.pop(0)
        # rotate array by 180
        array = array[::-1]
        for j in range(len(array)):
            array[j] = array[j][::-1]
        # end of rotation
        i -= 1

    straight_snail.append(array[0][0])
    return straight_snail
    
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)


array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
expected = [1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8]


#Trolls are attacking your comment section!
#A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#Your task is to write a function that takes a string and return a new string with all vowels removed.
#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#Note: for this kata y isn't considered a vowel.

import re

def disemvowel(string_):
    vowels = ['e', 'u', 'o', 'a', 'i']
    for chr in vowels:
        pattern = re.compile(chr, re.IGNORECASE)
        string_ = pattern.sub("", string_)
    return string_

import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    @test.it("First fixed test")
    def fixed_test_1():
        test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!", 'Incorrect answer for input="This website is for losers LOL!"\n')
    @test.it("Second fixed test")
    def fixed_test_2():
        test.assert_equals(disemvowel("No offense but,\nYour writing is among the worst I've ever read"), "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd", 'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n')
    @test.it("Third fixed test")
    def fixed_test_3():
        test.assert_equals(disemvowel("What are you, a communist?"), "Wht r y,  cmmnst?", 'Incorrect answer for input="What are you, a communist?"\n')
        
 
#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return false.
#
#Examples (Input --> Output)
#"1234"   -->  true
#"12345"  -->  false
# "a234"   -->  false 

import re

def validate_pin(pin):
    if len(pin) == 4:
        match = re.search(r'\d{4}', pin)
        #print(match[0] if match else 'Not found')
        return True if match else False
    elif len(pin) == 6:
        match = re.search(r'\d{6}', pin)
        return True if match else False
    else:
        return False

import codewars_test as test
from solution import validate_pin

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should return False for pins with length other than 4 or 6")
    def basic_test_cases():    
        test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
        test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
        test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
        test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
        test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
        test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
        test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
        test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
        test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
    
    @test.it("should return False for pins which contain characters other than digits")
    def _():
        test.assert_equals(validate_pin("a234"),False, "Wrong output for 'a234'")
        test.assert_equals(validate_pin(".234"),False, "Wrong output for '.234'")
    
    @test.it("should return True for valid pins")
    def _():
        test.assert_equals(validate_pin("1234"),True, "Wrong output for '1234'")
        test.assert_equals(validate_pin("0000"),True, "Wrong output for '0000'")
        test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("098765"),True, "Wrong output for '098765'")
        test.assert_equals(validate_pin("000000"),True, "Wrong output for '000000'")
        test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("090909"),True, "Wrong output for '090909'")


#Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
#also often referred to as Pascal case). The next words should be always capitalized.
#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    if len(text) == 0:
        return text
    if '_' in text:
        text = text.replace('_', '-')
    dash_match = re.findall(r'-?\w+', text) 
    camel_text = dash_match[0]
    for i in range(1, len(dash_match)):
        camel_text += dash_match[i][1:].capitalize()
    return camel_text

import codewars_test as test

@test.describe("Sample Tests")
def sample_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


#Complete the solution so that it splits the string into pairs of two characters. 
#If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#Examples:
#* 'abc' =>  ['ab', 'c_']
#* 'abcdef' => ['ab', 'cd', 'ef']

import re

def solution(s):    
    if len(s) == 0:
        return []
    match = re.findall(r'\w\w', s)
    if len(s) % 2 != 0:
        match.append(s[len(s)-1] + '_')
    return match

test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)


#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
#* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
#* url = "https://www.cnet.com"                -> domain name = cnet"

import re

def domain_name(url):    
    if len(url) == 0:
        return url
    #dName = re.split(r"((?:http[s*]?://)*)(?:[www\.]*)(\w+)", url)         # тут не работает имя домена через дефис (напр., 'zombie-bites')
    dName = re.split(r"((?:http[s*]?://)*)(?:[www\.]*)(\w+[-*]?\w+)", url)
    return dName[2]

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
test.assert_equals(domain_name("http://github.com/carbonfive/raygun"), "github")
test.assert_equals(domain_name("http://www.zombie-bites.com"), "zombie-bites")
test.assert_equals(domain_name("https://www.cnet.com"), "cnet")

#Classy Extensions
#Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing extends keyword. 
#You will be preloaded with the Animal class, so you should only edit the Cat class.
#Task
#Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
#The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).

from preloaded import Animal

class Cat(Animal):
    def speak(self):        
        return "%s meows." % self.name

from preloaded import Animal
from solution import Cat
import codewars_test as test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it("Testing for Mr Whiskers")
    def mr_whiskers():
        cat = Cat('Mr Whiskers')
        test.assert_equals(cat.speak(),'Mr Whiskers meows.')
        test.expect(isinstance(cat, Animal), "Your Cat class should extend Animal")
    @test.it("Testing for Lamp")
    def lamp():
        cat = Cat('Lamp')
        test.assert_equals(cat.speak(),'Lamp meows.')
    @test.it("Testing for $$Money Bags$$")
    def money_bags():
        cat = Cat('$$Money Bags$$')
        test.assert_equals(cat.speak(),'$$Money Bags$$ meows.')
        

#Classy Classes
#Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
#Task
#Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, 
#complete the get Info property and getInfo method/Info getter which should return 
#johns age is 34

class Person(object):
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

test.describe("Basic tests")
names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    test.it("Testing for %s and %s" %(repr(name),age))
    test.assert_equals(person.info, name+"s age is "+str(age))


#In this kata, your job is to create a class Dictionary which you can add words to and their entries. 
#Example:
#>>> d = Dictionary()
#>>> d.newentry('Apple', 'A fruit that grows on trees')
#>>> print(d.look('Apple'))
#A fruit that grows on trees
#>>> print(d.look('Banana'))
#Can't find entry for Banana

class Dictionary():
    def __init__(self):
        self.dictionary = {}
        
    def newentry(self, word, definition):
        self.dictionary[word] = definition
        
    def look(self, key):
        return self.dictionary.get(key, f"Can't find entry for {key}")

from solution import Dictionary
import codewars_test as test

@test.describe("Sample tests")
def basic_tests():
    
    d = Dictionary()

    @test.it("Testing for key 'Apple', should equal 'A fruit'")
    def _():
        d.newentry("Apple", "A fruit")
        test.assert_equals(d.look("Apple"), "A fruit")

    @test.it("Testing for key 'Soccer', should equal 'A sport'")
    def _():
        d.newentry("Soccer", "A sport")
        test.assert_equals(d.look("Soccer"), "A sport")
    
    @test.it("Testing for non-existing keys")
    def _():
        test.assert_equals(d.look("Hi"), "Can't find entry for Hi")
        test.assert_equals(d.look("Ball"), "Can't find entry for Ball")
    
    @test.it("Testing that entries are case sensitive")
    def _():
        test.assert_equals(d.look("soccer"), "Can't find entry for soccer")
        d.newentry("soccer", "a sport")
        test.assert_equals(d.look("soccer"), "a sport")


'''DefaultList

The collections module has defaultdict, which gives you a default value for trying to get the value of a key which does not exist in the dictionary 
instead of raising an error. Why not do this for a list?
Your job is to create a class (or a function which returns an object) called DefaultList. The class will have two parameters to be given: 
a list, and a default value. The list will obviously be the list that corresponds to that object. 
The default value will be returned any time an index of the list is called in the code that would normally raise an error 
(i.e. i > len(list) - 1 or i < -len(list)). This class must also support the regular list functions extend, append, insert, remove, and pop.
Because slicing a list never raises an error (slicing a list between two indexes that are not a part of the list returns [], slicing will not be tested for.

Example
lst = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
lst[4] = True
lst[80] = 'default_value'lst.extend([104, 1044, 4066, -2])
lst[9] = -2'''

class DefaultList:
    def __init__(self, list, defval = ['Bye']):
        self.list = list
        self.defval = defval
        # defaul value if list is empty
        if self.list == None:
          self.list = defval
          return self.list
    
    def __getitem__(self, index):
        if index >= len(self.list):
            return self.defval
        else:
            return self.list[index]
        
    def extend(self, extention):
        self.list.extend(extention)
        return self.list
    
    def append(self, item):
        self.list.append(item)
        return self.list
    
    def remove(self, item):
        self.list.remove(item)
        return self.list
    
    def insert(self, index, item):
        self.list.insert(index, item)
        return self.list

lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

test.assert_equals(lst[1], 3)
test.assert_equals(lst[333000], 'def')
test.assert_equals(lst[23], 'def')

lst.extend([3, 23, 'hello', 'lists', 'word', 344])

test.assert_equals(lst[9], 'lists')
test.assert_equals(lst[11], 344)
test.assert_equals(lst[12], 'def')

lst.append(233344455)

test.assert_equals(lst[12], 233344455)
test.assert_equals(lst[100], 'def')

lst.remove(2)
lst.remove(1)
lst.remove(3)

lst.insert(-3, 34.34)
test.assert_equals(lst[8], 'word')
test.assert_equals(lst[10], 233344455)


'''
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
   def __init__(self, name, fives, tens, twenties):
       self.name = name
       self.fives = fives
       self.tens = tens
       self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. 
If every student has the same amount, then return "all".
Notes:
Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money'''

def sum(student):
    return student.fives * 5 + student.tens * 10 + student.twenties * 20

def most_money(students):
    max_name = students[0].name
    max_sum = sum(students[0])
    sums = set()
    for s in students:
        curr_sum = sum(s)
        sums.add(curr_sum)
        if curr_sum > max_sum:
            max_name = s.name
            max_sum = curr_sum

    if len(sums) == 1 and len(students) > 1:  # если бы sums было изначально списком, то проверка на равенство элементов выглядела бы как if len(set(sums)) == 1
        return 'all'
    else:
        return max_name
        
from solution import most_money
import codewars_test as test
from preloaded import Student

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Examples")
    def examples():
        
        phil = Student("Phil", 2, 2, 1)
        cam = Student("Cameron", 2, 2, 0)
        geoff = Student("Geoff", 0, 3, 0)
        
        test.assert_equals(most_money([cam, geoff, phil]), "Phil")
        test.assert_equals(most_money([cam, geoff]), "all")
        test.assert_equals(most_money([geoff]), "Geoff")
        

'''
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.'''

# Variant 1

import math

class Vector:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "({})".format(",".join(map(str, self.value)))

    '''def __len__(self):
            return len(self.value)'''

    def check_length(f):
        def wrapper(self, other):
            #if len(self) != len(other):    # if "def __len__(self)..." not commented
            if len(self.value) != len(other.value):
                raise Exception("Vectors must have the same length")
            return f(self, other)
        return wrapper

    @check_length
    def add(self, other):
        return Vector([
            x + y for x, y in zip(self.value, other.value)
            ])

    @check_length
    def subtract(self, other):
        return Vector([
            x - y for x, y in zip(self.value, other.value)
            ])

    @check_length
    def dot(self, other):
        return sum([
            x * y for x, y in zip(self.value, other.value)
            ])

    def norm(self):
        return math.sqrt(sum([
            x * x for x in self.value
        ]))

    def equals(self, other):
        return self.value == other.value

# if __name__ == "__main__":
#     a = Vector([1, 2, 3])
#     b = Vector([3, 4, 5])
#     c = Vector([5, 6, 7, 8])
# 
#     print(a.add(b))  # should return a new Vector([4, 6, 8])
#     print(a.subtract(b))  # should return a new Vector([-2, -2, -2])
#     print(a.dot(b))  # should return 1*3 + 2*4 + 3*5 = 26
#     print(a.norm())  # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
#     print(a.add(c))  # raises an exception

# Variant 2

import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return "(" + ",".join(map(str, self.components)) + ")"

    def equals(self, other):
        return self.components == other.components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        new_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        new_components = [a - b for a, b in zip(self.components, other.components)]
        return Vector(new_components)

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product

    def norm(self):
        norm_value = math.sqrt(sum(a ** 2 for a in self.components))
        return norm_value

# # Test the Vector class
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# print(a.add(b))       # Output: (4,6,8)
# print(a.subtract(b))  # Output: (-2,-2,-2)
# print(a.dot(b))       # Output: 26
# print(a.norm())       # Output: sqrt(14)
# try:
#     a.add(c)
# except ValueError as e:
#     print("Error:", e)  # Output: Error: Vectors must have the same length

from solution import Vector
import codewars_test as test

@test.describe("Vector tests")
def vector_tests():
    
    @test.it("Example tests")
    def example_tests():
        
        a = Vector([1, 2])
        b = Vector([3, 4])
        
        test.expect(a.add(b).equals(Vector([4, 6])))
        
        
        a = Vector([1, 2, 3])
        b = Vector([3, 4, 5])
        
        test.expect(a.add(b).equals(Vector([4, 6, 8])))
        test.expect(a.subtract(b).equals(Vector([-2, -2, -2])))
        test.assert_equals(a.dot(b), 26)
        test.assert_equals(a.norm(), 14 ** 0.5)
        test.assert_equals(str(a), '(1,2,3)')
