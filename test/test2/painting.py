wall_length=float(input("Enter the length of one wall:"))
wall_height=float(input("Enter the height of the wall:"))
cost_per_sq_meter=float(input("Enter the cost of painting per sq:"))
num_coats=int(input("Enter the number of cost:"))

if wall_length <= 0 or wall_height <= 0 or cost_per_sq_meter <=0 or num_coats<=0:
    print("Error:All inputs must be positive values.")

area_one_wall=wall_length * wall_height

total_wall_area= 4* area_one_wall

paintable_area=total_wall_area* num_coats
total_cost=paintable_area * cost_per_sq_meter

print(f'painting cost calculation')
print(f'Area of one wall:{area_one_wall}')
print(f'Total area of four walls:{total_wall_area}')
print(f'total paintable area{num_coats}')
print(f'Total cost of painting:{total_cost}')



