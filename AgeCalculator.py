from datetime import datetime

def calculate_age(dob):
    # Assuming dob is in the format 'YYYY-MM-DD'
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Calculate the difference between current date and date of birth
    age_difference = current_datetime - dob_date
    
    # Extract years, months, and days
    years = age_difference.days // 365
    months = (age_difference.days % 365) // 30
    days = (age_difference.days % 365) % 30
    
    # Extract hours, minutes, and seconds
    hours, remainder = divmod(age_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return years, months, days, hours, minutes, seconds

# Example usage
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
years, months, days, hours, minutes, seconds = calculate_age(date_of_birth)
print(f"You are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds old.")
