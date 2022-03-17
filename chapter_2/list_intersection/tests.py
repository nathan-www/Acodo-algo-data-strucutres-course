import random, json

def test1():

    listC = generate_linked_list([8,4,5])
    listA = generate_linked_list([4,1],listC)
    listB = generate_linked_list([5,6,1],listC)

    return findIntersect(listA,listB) == listC

def test2():

    listA = generate_linked_list([2,6,4])
    listB = generate_linked_list([1,5])

    return findIntersect(listA,listB) == None


def test3():

    results = []

    for i in range(1,4):
        listA = []
        listB = []
        listC = []

        for e in range(1,random.randint(1,6)):
            listA.append(random.randint(1,99))
        for e in range(1,random.randint(1,6)):
            listB.append(random.randint(1,99))
        for e in range(1,random.randint(1,6)):
            listC.append(random.randint(1,99))

        print("========")
        print("Dynamic test " + str(i))
        print("findIntersect("+json.dumps(listA + listC)+","+json.dumps(listB + listC)+")")

        listC = generate_linked_list(listC)
        listA = generate_linked_list(listA,listC)
        listB = generate_linked_list(listB,listC)
        result = findIntersect(listA,listB)

        try:
            print("Output: " + str(result.val))
        except:
            print("Output: " + str(result))

        try:
            print("Expected: " + str(listC.val))
        except:
            print("Expected: None")

        if(result == listC):
            print("[PASS]")
            results.append(True)
        else:
            print("[FAIL]")
            results.append(False)

    for r in results:
        if r == False:
            return False
    return True

def generate_linked_list(arr,head=None):
    arr.reverse()
    for i in arr:
        head = ListNode(i,head)
    return head
