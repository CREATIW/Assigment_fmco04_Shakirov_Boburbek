number_jars = int(input("Enter the number of jars: "))
total = 0
below_range = 0
in_range = 0
above_range = 0
# Here we are checking the volume of jars ------------
def classify(value):
    if value < 248:
        return "Below range" 
    elif 248 <= value <=  252:
        return "In range" 
    elif value > 252:
        return "Above range"
# Here we are counting the total and average volume at all ------------
    
def calculate_average(total,count):
    average_vol = total / count
    return f"Average volume: {(average_vol)} ml"

# Here wea are creating a loop by the length of jars, set to classify() funtion volume jars,Counting the ranges and print it ------------

for i in range(number_jars):
    volume_jars = int(input("Enter the jar volume: "))
    result = classify(volume_jars)
    if result == "Below range":
        below_range += 1
    elif result == "In range":
        in_range += 1
    elif result == "Above range":
        above_range += 1
    total += volume_jars
    print(result)
    
print(f"Total volume: {total} ml")
print(calculate_average(total,number_jars))
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")

# These code was written by FMCO-04 student --- SHAKIROV BOBURBEK ---
    