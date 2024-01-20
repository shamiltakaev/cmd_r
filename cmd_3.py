import sys
nums = sys.argv[1:]
if nums:
    try:
        nums = list(map(int, nums))
        s = 0
        k = 1
        for num in nums:
            s += (num * k)
            k = -k
        print(s)
    except Exception as e:
        print(e.__class__.__name__)
else:
    print("NO PARAMS")