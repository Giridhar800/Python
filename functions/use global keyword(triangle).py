base = 0.0
height = 0.0

def read():
    global base,height
    base = float(input("Enter Base:"))
    height = float(input("Enter Height:"))

def find_area():
    area = 0.5*base*height
    print(f" Area of a triangle is {area:.2f}")

read()
find_area()
                       
