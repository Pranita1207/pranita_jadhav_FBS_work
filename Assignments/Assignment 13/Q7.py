## Python program to remove the given key  from a dictionary

Dictionary={'a':'happy','b':'birthday','c':'to','d':'you','e':'dear'}

key_to_remove ='e'
if key_to_remove in Dictionary:
    del Dictionary[key_to_remove]
    
print("Remove the given key from the dictionary:",Dictionary)