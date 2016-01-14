import json

def nums_sum2(obj):
    if isinstance(obj, int):
        return obj
    s = 0
    if isinstance(obj, list):
        for item in obj:
            s += nums_sum2(item)
    elif isinstance(obj, dict):
        for k in obj:
            v = obj[k]
            if v == 'red':
                return 0
            s += nums_sum2(v)
    return s

def nums_sum(s):
    return nums_sum2(json.loads(s))

def main():
    cases = {'[1,2,3]': 6, '{"a":2,"b":4}': 6, '[[[3]]]': 3, '{"a":{"b":4},"c":-1}': 3, '[1,{"c":"red","b":2},3]': 4, '{"d":"red","e":[1,2,3,4],"f":5}': 0, '[1,"red",5]': 6}
    for k in cases:
        assert(cases[k] == nums_sum(k))

    print nums_sum(file('input12').read())

main()
