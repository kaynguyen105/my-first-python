# a="abcdefg"
# print(a[:-3])


a = [1,2,3,4,5,6,7,8]
b = (3,4,1,2,7,6,5,8)
c = {5,6,7,8,1,2,3,4}
#*********************************************************


b_list = list(b)
c_list = list(c)
b_sort = b_list.sort()


print(b_list)
print(c_list)
print(a)

if b_list == c_list == a:
    print("True")
else:
    print("False")
