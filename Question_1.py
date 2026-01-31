threshold_value = int(input("Choose a threshold value: ")) #Get input from user

#Set both product_value and multiplier_value to one as base value
product_value = 1
multiplier_value = 1

#While loop that works only when product_value is less or equal to the threshold,
#it keeps on multiplying the product value by the multiplier value and then increments the
#muplitplier by one until the product value becomes greater than the threshold value
while product_value <= threshold_value:
    product_value = product_value * multiplier_value
    multiplier_value += 1

print(f'''Final Product: {product_value} 
Integer Responsible For Multiplying Beyond Threshold: {multiplier_value - 1}''')
#Subtract one from multiplier_value because of the extra one added in the while loop.