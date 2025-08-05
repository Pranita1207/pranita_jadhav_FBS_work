basic=int(input("Enter basic salary:"))

da_amt=(basic*10)/100
ta_amt=(basic*12)/100
hra_amt=(basic*15)/100

total_salary= basic+ ta_amt +hra_amt+da_amt

print(f'total salary is:{total_salary}')