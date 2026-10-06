destination=input("Your Destination: ")
distance=float(input("Distance in Kilo Meter(km): "))
average_speed=float(input("Average speed in km/h: "))

time=distance/average_speed

print("\n")
print(f"Destination: {destination}")
print(f"Destance: {distance} km")
print(f"Average Speed: {average_speed} km/h")
print(f"Estimated Travel Time: {time} hours")
print(f"Estimated Travel Time in Minutes:{time*60} mins")