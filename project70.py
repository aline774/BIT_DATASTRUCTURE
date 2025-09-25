# Project 70: Startup Incubator Applicants

import array

print("\n--- INTEGERS ---")
# Integer values (e.g., number of applicants scored in different rounds)
applicant_scores = [45, 60, 75, 50, 90, 85]

# Compute total, average, min, max
total = sum(applicant_scores)
average = total / len(applicant_scores)
minimum = min(applicant_scores)
maximum = max(applicant_scores)

print("Scores:", applicant_scores)
print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)


print("\n--- STRINGS ---")
# Formatted report using f-strings
report = (
    f"Total number of applicants' scores recorded: {len(applicant_scores)}\n"
    f"The average applicant score is: {average:.2f}"
)
print(report)


print("\n--- BOOLEANS ---")
# Apply threshold condition
threshold = 65
if average > threshold and maximum >= 90:   # compound condition
    print("Status: Above Standard")
else:
    print("Status: Below Standard")


print("\n--- LISTS ---")
# Maintain a list of applicant names
applicant_names = ["Alice", "Brian", "Clara", "David", "Ella"]
print("Original list:", applicant_names)

# Add a new applicant
applicant_names.append("Frank")

# Remove one based on a condition (remove if name starts with 'B')
applicant_names = [name for name in applicant_names if not name.startswith("B")]

# Sort
print("Modified list before sorting:", applicant_names)
applicant_names.sort()
print("Sorted list after modifications:", applicant_names)


print("\n--- ARRAYS ---")
# Use Python's array module
arr_scores = array.array("i", [45, 60, 75])  # fixed-size numeric subset
print("Array scores:", arr_scores.tolist())

# Sum of array
arr_sum = sum(arr_scores)
print("Sum of array:", arr_sum)

# Compare with list sum
print("Is array sum equal to list total?", arr_sum == total)


print("\n--- DICTIONARIES ---")
# List of dictionaries for applicants
applicants = [
    {"id": 1, "name": "Alice", "value": 45},
    {"id": 2, "name": "Brian", "value": 60},
    {"id": 3, "name": "Clara", "value": 75},
    {"id": 4, "name": "David", "value": 50},
]

print("Original applicants:", applicants)

# Update one record
applicants[2]["value"] = 80   # Update Clara's value

# Delete another (remove Brian with id=2)
applicants = [app for app in applicants if app["id"] != 2]

# Compute total of values
value_total = sum(app["value"] for app in applicants)

print("Updated applicants:", applicants)
print("Total of 'value' field:", value_total)
