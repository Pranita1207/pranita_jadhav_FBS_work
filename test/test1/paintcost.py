area=int(input("Enter area of one wall:"))
interior_cost=int(input("Enter interior paint cost:"))
exterior_cost=int(input("Enter exterior paint cost:"))

total_area= 7*area              
total_interior_cost= total_area * interior_cost
total_exterior_cost= total_area * exterior_cost

print(f'total_area:{total_area},total_interior_cost :{total_interior_cost},total_exterior_cost:{total_exterior_cost}')