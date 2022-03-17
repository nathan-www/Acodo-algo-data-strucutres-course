import json, random

def test1():
    output = isPalindrome(123)
    return output == False

def test2():
    output = isPalindrome(-686)
    return output == False

def test3():
    output = isPalindrome(112232211)
    return output == True

def test4():
    results = []

    for i in range(1,4):
        expected = [True,False][random.randint(0,1)]
        if expected:
            input = gen_palindrome()
            output = isPalindrome(input)
        else:
            input = gen_non_palindrome()
            output = isPalindrome(input)

        print("========")
        print("Dynamic test " + str(i))
        print("isPalindrome("+str(input)+")")
        print("Output: " + str(output))
        print("Expected: " + str(expected))
        if(expected == output):
            print("[PASS]")
            results.append(True)
        else:
            print("[FAIL]")
            results.append(False)

    for r in results:
        if r == False:
            return False
    return True



def gen_palindrome():
    palindrome = ""

    num = random.randint(1,9)
    for i in range(0,random.randint(1,5)):
        palindrome += str(num)

    for i in range(0,random.randint(1,5)):
        num = random.randint(1,9)
        for i in range(1,random.randint(1,5)):
            palindrome = str(num) + palindrome + str(num)

    return int(palindrome)

def gen_non_palindrome():
    np = ""

    for i in range(0,2):
        num = random.randint(1,9)
        np += 3*str(num)

    for i in range(0,random.randint(1,5)):
        np += str(random.randint(1,9))

    return int(''.join(random.sample(np,len(np))))
