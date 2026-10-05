

def calculate_area_and_perimeter():
  length=float(input("Enter length in meter: "))
  width=float(input("Enter width in meter: "))
  
  print("\n")
  
  area=length * width
  perimeter=2 * (length+width)
  
  print(f"Area: {area} sqm")
#   print("\n")
  print(f"Perimeter: {perimeter} m")
  
  
if __name__=="__main__":
    calculate_area_and_perimeter()
  

# Goal
# Practice numeric values and arithmetic operators.
# Imagine you are building a small construction tool.
# Ask the user for:
# Length
# Width
# Calculate:
# Area
# Perimeter
# Then display the results.
# Example
# Length: 10
# Width: 5

# Area: 50 m²
# Perimeter: 30 m

# Concepts
# Numbers • arithmetic operators • input conversion
