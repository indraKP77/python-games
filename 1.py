def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight and height.

    Parameters:
    - weight (float): Weight in kilograms.
    - height (float): Height in centimeters.

    Returns:
    - bmi (float): Body Mass Index.
    """
    height_m = height / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

def calculate_daily_calories(weight, height, age, gender, activity_level):
    """
    Calculate daily calorie intake required to maintain, gain, or lose weight based on BMI and other factors.

    Parameters:
    - weight (float): Weight in kilograms.
    - height (float): Height in centimeters.
    - age (int): Age in years.
    - gender (str): 'male' or 'female'.
    - activity_level (str): One of 'sedentary', 'light', 'moderate', 'active', 'very active'.

    Returns:
    - target_calories (float): Daily calorie intake required.
    - action (str): Recommended action ('gain', 'maintain', 'lose').
    - bmi (float): Calculated BMI.
    """

    # Step 1: Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Step 2: Calculate BMR using Harris-Benedict equation
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")

    # Step 3: Adjust BMR based on activity level to get TDEE
    if activity_level == 'sedentary':
        tdee = bmr * 1.2
    elif activity_level == 'light':
        tdee = bmr * 1.375
    elif activity_level == 'moderate':
        tdee = bmr * 1.55
    elif activity_level == 'active':
        tdee = bmr * 1.725
    elif activity_level == 'very active':
        tdee = bmr * 1.9
    else:
        raise ValueError("Invalid activity level. Choose from 'sedentary', 'light', 'moderate', 'active', 'very active'.")

    # Step 4: Determine recommended calorie change based on BMI range
    if bmi < 18.5:
        action = "gain"
        target_calories = tdee * 1.10  # Increase by 10% for underweight
    elif 18.5 <= bmi <= 24.9:
        action = "maintain"
        target_calories = tdee  # Maintain current calorie intake for normal weight
    elif 25 <= bmi <= 29.9:
        action = "lose"
        target_calories = tdee * 0.90  # Decrease by 10% for overweight
    elif 30 <= bmi <= 34.9:
        action = "lose"
        target_calories = tdee * 0.85  # Decrease by 15% for Obesity Class I
    elif 35 <= bmi <= 39.9:
        action = "lose"
        target_calories = tdee * 0.80  # Decrease by 20% for Obesity Class II
    else:  # bmi >= 40
        action = "lose"
        target_calories = tdee * 0.75  # Decrease by 25% for Obesity Class III

    return target_calories, action, bmi

# Example usage

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ").lower()
activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()
target_calories, action, bmi = calculate_daily_calories(weight, height, age, gender, activity_level)
print(f"Your BMI is: {bmi:.0f}")
print(f"To {action} weight, your target daily calorie intake should be around: {target_calories:.0f} calories.")