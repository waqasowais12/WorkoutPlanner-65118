def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

def workout_and_diet_plan(bmi):
    if bmi < 18.5:
        return ("Underweight", "Workout: 20 mins/day (light cardio)\nDiet: High-protein, calorie-dense foods")
    elif 18.5 <= bmi < 25:
        return ("Normal", "Workout: 30 mins/day (balanced routine)\nDiet: Balanced meals with fruits, veggies, and lean proteins")
    elif 25 <= bmi < 30:
        return ("Overweight", "Workout: 45 mins/day (cardio + strength)\nDiet: Low-carb, high-fiber diet")
    else:
        return ("Obese", "Workout: 60 mins/day (intense cardio)\nDiet: Very low-calorie, supervised diet plan")

def main():
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()

        # Check for empty inputs
        if not weight_input or not height_input:
            raise ValueError("Input cannot be empty.")

        # Convert inputs to float
        weight = float(weight_input)
        height = float(height_input)

        # Check for non-positive values
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category, plan = workout_and_diet_plan(bmi)

        print(f"\nYour BMI is: {bmi:.2f} ({category})")
        print(plan)

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()
