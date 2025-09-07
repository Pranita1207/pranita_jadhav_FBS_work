## Create three lists numbers, their squares and cubes

numbers=[2,4,6,8]
square_root=[]
cube_root=[]

for i in numbers:
    square_root.append(i* i)
    cube_root.append(i*i*i)
    
print("Numbers",numbers)
print("Squares",square_root)
print("Cubes",cube_root)