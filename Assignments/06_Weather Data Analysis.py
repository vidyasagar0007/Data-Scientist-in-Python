import numpy as np
import pandas as pd

# ============================================================
# PROJECT 6: WEATHER DATA ANALYSIS
# ============================================================

# Given Dataset
temperature = np.array([
    [32, 34, 35, 33, 31],
    [28, 30, 31, 29, 27],
    [35, 36, 38, 37, 34],
    [25, 27, 29, 28, 26]
])

# City names and days
cities = [
    "City 1",
    "City 2",
    "City 3",
    "City 4"
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]


# ============================================================
# 1. AVERAGE TEMPERATURE OF EACH CITY
# ============================================================

city_average = np.mean(temperature, axis=1)

print("\n1. Average Temperature of Each City:")

for i in range(len(cities)):
    print(f"{cities[i]}: {city_average[i]:.2f}°C")


# ============================================================
# 2. MAXIMUM TEMPERATURE OF EACH CITY
# ============================================================

city_maximum = np.max(temperature, axis=1)

print("\n2. Maximum Temperature of Each City:")

for i in range(len(cities)):
    print(f"{cities[i]}: {city_maximum[i]}°C")


# ============================================================
# 3. MINIMUM TEMPERATURE OF EACH CITY
# ============================================================

city_minimum = np.min(temperature, axis=1)

print("\n3. Minimum Temperature of Each City:")

for i in range(len(cities)):
    print(f"{cities[i]}: {city_minimum[i]}°C")


# ============================================================
# 4. IDENTIFY THE HOTTEST DAY
# ============================================================

daily_average = np.mean(temperature, axis=0)

hottest_day_index = np.argmax(daily_average)

print("\n4. Hottest Day:")

print(
    f"{days[hottest_day_index]} "
    f"with average temperature "
    f"{daily_average[hottest_day_index]:.2f}°C"
)


# ============================================================
# 5. IDENTIFY THE COOLEST DAY
# ============================================================

coolest_day_index = np.argmin(daily_average)

print("\n5. Coolest Day:")

print(
    f"{days[coolest_day_index]} "
    f"with average temperature "
    f"{daily_average[coolest_day_index]:.2f}°C"
)


# ============================================================
# 6. CITY WITH HIGHEST AVERAGE TEMPERATURE
# ============================================================

hottest_city_index = np.argmax(city_average)

print("\n6. City With Highest Average Temperature:")

print(
    f"{cities[hottest_city_index]} "
    f"with average temperature "
    f"{city_average[hottest_city_index]:.2f}°C"
)


# ============================================================
# 7. CITIES WHOSE AVERAGE TEMPERATURE IS GREATER THAN 30°C
# ============================================================

print("\n7. Cities With Average Temperature Greater Than 30°C:")

for i in range(len(cities)):
    if city_average[i] > 30:
        print(
            f"{cities[i]}: "
            f"{city_average[i]:.2f}°C"
        )


# ============================================================
# 8. STANDARD DEVIATION
# ============================================================

standard_deviation = np.std(temperature)

print("\n8. Standard Deviation of Temperature:")

print(f"{standard_deviation:.2f}°C")


# ============================================================
# 9. CLASSIFY EACH TEMPERATURE AS HOT OR NORMAL
#    Temperature >= 35°C → Hot
#    Temperature < 35°C  → Normal
# ============================================================

classification = np.where(
    temperature >= 35,
    "Hot",
    "Normal"
)

print("\n9. Temperature Classification:")

for i in range(len(cities)):
    print(f"\n{cities[i]}:")

    for j in range(len(days)):
        print(
            f"{days[j]}: "
            f"{temperature[i][j]}°C - "
            f"{classification[i][j]}"
        )


# ============================================================
# 10. CONVERT DATA INTO PANDAS DATAFRAME
# ============================================================

df = pd.DataFrame(
    temperature,
    columns=days,
    index=cities
)

print("\n10. Weather DataFrame:")

print(df)


# ============================================================
# ADD AVERAGE TEMPERATURE COLUMN
# ============================================================

df["Average Temperature"] = df.mean(axis=1)

print("\nFinal DataFrame:")

print(df)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("               WEATHER DATA ANALYSIS")
print("=" * 60)

print(
    f"Hottest Day        : "
    f"{days[hottest_day_index]}"
)

print(
    f"Coolest Day        : "
    f"{days[coolest_day_index]}"
)

print(
    f"Hottest City       : "
    f"{cities[hottest_city_index]}"
)

print(
    f"Highest Temperature: "
    f"{np.max(temperature)}°C"
)

print(
    f"Lowest Temperature : "
    f"{np.min(temperature)}°C"
)

print(
    f"Standard Deviation : "
    f"{standard_deviation:.2f}°C"
)

print("=" * 60)