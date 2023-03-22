import pytest

def acceptOptionInput():
    return input("Select an option: ")

def displayOptions():
    print("1. Calculate BMI")
    print("2. Exit")

def calculateBMI(weight, height):
    # Calculate BMI
    weight = convertWeight(weight)
    height = convertHeight(height)
    bmi = doMath(weight, height)
    print("BMI: " + str(bmi))
    return bmi

def classify(bmi):
    # Classify BMI
    if bmi < 18.5:
        classification = "Underweight"
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        classification = "Normal Weight"
        print("Normal Weight")
    elif bmi >= 25 and bmi < 30:
        classification = "Overweight"
        print("Overweight")
    else:
        classification = "Obese"
        print("Obese")
    
    return classification

def convertWeight(weight):
    # Convert weight from lbs to kg
    return weight * 0.45

def convertHeight(height):
    # Convert height from inches to m
    return height * 0.025

def doMath(weight, height):
    # Calculate BMI
    return weight / height**2
    
def main():
    # Main function
    while True:
        displayOptions()
        option = acceptOptionInput()
        if option == "1":
            weight = float(input("Enter weight in lbs: "))
            height = float(input("Enter height in inches: "))
            classify(calculateBMI(weight, height))
        elif option == "2":
            break
        else:
            print("Invalid option")

def test_convertWeight():
    assert convertWeight(100) == 45

def test_convertHeight():
    assert convertHeight(100) == 2.5

def test_doMath():
    assert doMath(45, 2.5) == 7.2

def test_calculateBMI():
    assert calculateBMI(100, 100) == 7.2

def test_classify():
    assert classify(18.4) == "Underweight"
    assert classify(18.5) == "Normal Weight"
    assert classify(20) == "Normal Weight"
    assert classify(24.9) == "Normal Weight"
    assert classify(25) == "Overweight"
    assert classify(26) == "Overweight"
    assert classify(29.9) == "Overweight"
    assert classify(30) == "Obese"


if __name__ == "__main__":
    main()