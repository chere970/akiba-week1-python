

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
  


