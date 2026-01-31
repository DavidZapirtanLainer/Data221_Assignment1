import math #Importing the math library in order to do calculations with pi


def circle_area_coverage(radius_of_circle1, radius_of_circle2):
    #Using a conditional to only allow positive integers be used in the function
    if (not isinstance(radius_of_circle1, int) or radius_of_circle1 < 0) or (not isinstance(radius_of_circle2, int) or radius_of_circle2 < 0):
        return "INVALID INPUT. THE RADII OF THE CIRCLES NEED TO BE POSITIVE INTEGERS"

    #Calculating the area of both circles with the formula pi multiplied by r squared
    area_of_circle1 = math.pi * (radius_of_circle1 ** 2)
    area_of_circle2 = math.pi * (radius_of_circle2 ** 2)


    #Conditionals that check which area is larger,
    #Find how much of the bigger circle can be covered by the smaller one
    #Then returns a string stating which circle is larger how much of the bigger circle can be covered by the smaller one
    if area_of_circle1 > area_of_circle2:
        percentage_of_larger_circle_covered_by_smaller_circle = (area_of_circle2/area_of_circle1) * 100
        return f"Circle one is the bigger circle and {percentage_of_larger_circle_covered_by_smaller_circle}% of it can be covered by circle one"


    elif area_of_circle1 < area_of_circle2:
        percentage_of_larger_circle_covered_by_smaller_circle = (area_of_circle1/area_of_circle2) * 100
        return f"Circle two is the bigger circle and {percentage_of_larger_circle_covered_by_smaller_circle}% of it can be covered by circle one"

    elif area_of_circle1 == area_of_circle2:
        return "Both circles have the same area, therefore they can both cover 100% of each other."



example_radius_of_circle1 = 10
example_radius_of_circle2 = 8

print(circle_area_coverage(example_radius_of_circle1, example_radius_of_circle2))


