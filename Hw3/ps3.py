def test1(a,b):
    temp = a
    a = b
    b = temp

# # Test 1 
# a = 1
# b = 2
# test(a,b)
# print(b)

def test2(ls):
    ls.append('a')
    
# Test 2
ls = []
test2(ls)
print (ls)
