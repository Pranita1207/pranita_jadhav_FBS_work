Seconds=int(input("Enter the Seconds:"))

Hours = Seconds // 3600
Hours = Seconds % 3600

Minutes = Hours // 60

Seconds = Hours % 60
print(f'Hours{Hours},Minutes{Minutes}Seconds{Seconds}')