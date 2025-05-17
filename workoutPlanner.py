def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def workout_and_diet_plan(bmi):
    if bmi < 18.5:
        return ("Underweight", "Workout: 20 mins/day (light cardio)", "Workout Location: Home")
    elif 18.5 <= bmi < 25:
        return ("Normal", "Workout: 30 mins/day (balanced routine)", "Workout Location: Home or Gym")
    elif 25 <= bmi < 30:
        return ("Overweight", "Workout: 45 mins/day (cardio + strength)", "Workout Location: Gym preferred")
    else:
        return ("Obese", "Workout: 60 mins/day (intense cardio)", "Workout Location: Gym strongly recommended")

def main():
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()

        if not weight_input or not height_input:
            raise ValueError("Input cannot be empty.")

        weight = float(weight_input)
        height = float(height_input)

        bmi = calculate_bmi(weight, height)
        category, plan, location = workout_and_diet_plan(bmi)

        print(f"\nYour BMI is: {bmi:.2f} ({category})")
        print(plan)
        print(location)

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
