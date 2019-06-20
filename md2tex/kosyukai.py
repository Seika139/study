s = "dksagokflpl@l@pl@plvaosdk,lvf"
n = s.find("l@")
print(n)

s = 'abcabcabc'
target = 'abc'
index = -1
while True:
    index = s.find(target, index + 1)
    if index == -1:
        break
    print('start=%d' % index)


t1 = {1,3,4,2,5,"a",1}
print(t1)


t2 = (1,4,5,76,3,1,2,1)
print(t2)

dic = {1:3}
print(type(dic))
type(dic) == dict
