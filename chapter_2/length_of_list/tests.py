import random, json

def test1():
    output = listLength(generate_linked_list([1,2,3,4]))
    return output == 4

def test2():
    output = listLength(generate_linked_list([5,5,2,6,1,8,0]))
    return output == 7

def test3():
    output = listLength(generate_linked_list([]))
    return output == 0

def test4():
    results = [];
    for i in range(1,4):
        arr = []
        for e in range(0,random.randint(0,20)):
            arr.append(random.randint(0,100))

        result = listLength(generate_linked_list(arr))

        print("========")
        print("Dynamic test " + str(i))
        print("listLength("+json.dumps(arr)+")")
        print("Output: " + str(result))
        print("Expected: " + str(len(arr)))
        if(result == len(arr)):
            print("[PASS]")
            results.append(True)
        else:
            print("[FAIL]")
            results.append(False)

    for r in results:
        if r == False:
            return False
    return True



def generate_linked_list(arr):
    arr.reverse()
    head = None
    for i in arr:
        head = ListNode(i,head)
    return head
