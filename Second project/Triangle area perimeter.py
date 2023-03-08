import math
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if side1 + side2 < side3:
    print("This is not a triangle")
elif side1 + side3 < side2:
    print("This is not a triangle")
elif side2 + side3 < side1:
    print("This is not a triangle")

else:
    perimeter = (side1 + side2 + side3)/2
    area = math.sqrt(perimeter*(perimeter-side1)*(perimeter-side2)*(perimeter-side3))

    print("the perimeter is", perimeter)
    print("the area is", area)

