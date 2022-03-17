import json, random

def test1():
    output = twoSum([2,7,11,15],9)
    output.sort()
    return json.dumps(output) == json.dumps([0,1])


def test2():
    output = twoSum([1,2,4],6)
    output.sort()
    return json.dumps(output) == json.dumps([1,2])

def test3():

    results = []
    for i in range(1,4):
        target = random.randint(2,50)
        nums = []
        for e in range(0,random.randint(0,15)):
            nums.append(random.randint(1,50))

        option1 = target - random.randint(1,target-1)
        option2 = target - option1
        nums.append(option1)
        nums.append(option2)
        random.shuffle(nums)

        output = twoSum(nums,target)
        result = (nums[output[0]] + nums[output[1]] == target)
        results.append(result)

        print("========")
        print("Dynamic test " + str(i))
        print("twoSum("+json.dumps(nums)+","+str(target)+")")
        print("Output: " + json.dumps(output))
        if(result):
            print("[PASS]")
        else:
            print("[FAIL]")
        print("")

    for r in results:
        if r == False:
            return False
    return True
