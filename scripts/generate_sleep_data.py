# Import necessary libraries
import random
from datetime import time, datetime, timedelta
import pandas as pd

# Define user behavior profiles for sleep simulation
profiles = [
    {
        "name": "heavy phone user",
        "screen_time": (7 * 60, 23 * 60),  # in minutes
        "duration_of_sleep": (1 * 60, 6 * 60),  # in minutes
        "time_of_going_to_bed": (time(0, 0), time(6, 0)),
        "dark_mode": 0.2,
        "type_of_apps": ["Instagram", "TikTok"]
    },
    {
        "name": "average phone user",
        "screen_time": (4 * 60, 6 * 60),
        "duration_of_sleep": (6 * 60, 8 * 60),
        "time_of_going_to_bed": random.choice([(time(22, 30), time(23, 59)), (time(0, 0), time(1, 0))]),
        "dark_mode": 0.5,
        "type_of_apps": ["Reddit", "YouTube", "Instagram"]
    },
    {
        "name": "healthy phone use",
        "screen_time": (1 * 60, 3 * 60),
        "duration_of_sleep": (8 * 60, 10 * 60),
        "time_of_going_to_bed": (time(21, 30), time(22, 30)),
        "dark_mode": 0.8,
        "type_of_apps": ["YouTube", "Long content"]
    }
]

# Function to compute a sleep quality score based on behavioral features
def compute_sleep_quality(screen_time, sleep_duration, bedtime, dark_mode, app_used):
    score = 10.0  # start from base score

    # Penalize excessive screen time (e.g. 30 min = -0.25)
    score -= (screen_time / 60) * 0.5

    # Penalize sleep duration deficit (< 7h = 420 min)
    score -= max(0, (420 - sleep_duration) / 60) * 1.0

    # Penalize late bedtime (after midnight)
    bedtime_hour = int(bedtime.split(":")[0])
    if bedtime_hour >= 0 and bedtime_hour < 6:
        score -= 1.0

    # Bonus for using dark mode
    if dark_mode:
        score += 0.5

    # Bonus for relaxing apps
    if app_used in ["YouTube", "Long content"]:
        score += 0.5

    # Clamp score between 1 and 10
    return max(1.0, min(10.0, round(score, 2)))

# Function to generate one night of sleep data from a random profile
def generate_night():
    profile = random.choice(profiles)

    screen_time = random.randint(*profile["screen_time"])
    sleep_duration = random.randint(*profile["duration_of_sleep"])

    min_time = profile["time_of_going_to_bed"][0]
    max_time = profile["time_of_going_to_bed"][1]

    min_minutes = min_time.hour * 60 + min_time.minute
    max_minutes = max_time.hour * 60 + max_time.minute

    if max_minutes < min_minutes:
        valid_minutes = list(range(min_minutes, 1440)) + list(range(0, max_minutes + 1))
    else:
        valid_minutes = list(range(min_minutes, max_minutes + 1))

    random_minutes = random.choice(valid_minutes)
    bedtime_hour = random_minutes // 60
    bedtime_minute = random_minutes % 60
    bedtime = time(bedtime_hour, bedtime_minute)
    bedtime_str = bedtime.strftime("%H:%M")

    dark_mode_used = random.random() < profile["dark_mode"]
    app_used = random.choice(profile["type_of_apps"])

    base_date = datetime(2025, 1, 1)
    random_days = random.randint(0, 30)
    sleep_date = (base_date + timedelta(days=random_days)).date()

    # Compute sleep quality score using defined logic
    sleep_quality_score = compute_sleep_quality(
        screen_time,
        sleep_duration,
        bedtime_str,
        dark_mode_used,
        app_used
    )

    return {
        "date": sleep_date,
        "profile": profile["name"],
        "screen_time_min": screen_time,
        "sleep_duration_min": sleep_duration,
        "bedtime": bedtime_str,
        "dark_mode": int(dark_mode_used),
        "app_used": app_used,
        "sleep_quality_score": sleep_quality_score
    }

# Generate multiple nights and store them in a list
simulated_nights = [generate_night() for _ in range(100)]

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(simulated_nights)

# Save the simulated data to a CSV file
df.to_csv("data/simulated_sleep_data.csv", index=False)

print("100 nights of simulated sleep data generated and saved to data/simulated_sleep_data.csv")
