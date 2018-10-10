path="/Users/mcadena/Day01/ex01/numbers.txt"
def readfile(p):
    file_object  = open(p, 'r')
    return file_object.read()

num_list=readfile(path)
num_list=num_list.split(",")

for num in  num_list:
    print(num)
