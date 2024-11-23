# Create calculate_insurance_cost() function below: 


# Create calculate_insurance_cost() function below: 


# Initial variables for Maria 
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  

# Estimate Maria's insurance cost
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print("The estimated insurance cost for Maria is " + str(insurance_cost) + " dollars.")

# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

# Estimate Omar's insurance cost 
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print("The estimated insurance cost for Omar is " + str(insurance_cost) + " dollars.")

def calculate_insurance_cost():
    pass


def calculate_insurance_cost():
    estimated_cost = 1000
    print("The estimated insurance cost for this person is " + str(estimated_cost) + " dollars.")
    return estimated_cost


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 1000
    print("The estimated insurance cost for this person is " + str(estimated_cost) + " dollars.")
    return estimated_cost


250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500


maria_insurance_cost = calculate_insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)


# Removed initial variables and print statement for Omar

omar_insurance_cost = calculate_insurance_cost(age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1)


def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost

print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")

maria_insurance_cost = calculate_insurance_cost(name="Maria", age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)

maria_message, maria_insurance_cost = calculate_insurance_cost(name="Maria", age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)
omar_message, omar_insurance_cost = calculate_insurance_cost(name="Omar", age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1)

print(maria_message)
print(omar_message)

# Calculate the difference
calculate_cost_difference(maria_insurance_cost, omar_insurance_cost)
smoker=0



