# Import the Pandas library
import pandas as pd

# Create a Dataframe with the data you want to process
data = pd.DataFrame({
    "age": [18, 20, 22, 25, 27, 29, 30, 32, 35],
    "gender": ["male", "male", "female", "female", "female", "male", "male", "female", "female"]
})

# Use the GroupBy function to group the data by gender
gender_groups = data.groupby("gender")

# Use the apply() function to apply a custom function to each group of data
age_sum = gender_groups["age"].apply(lambda x: sum(x))
gender_sum = gender_groups["gender"].apply(lambda x: len([group["age"] for group in gender_groups if group["gender"] == x]))

# Use the reduce() function to combine the results of the apply() function and produce a final result
final_result = gender_sum.reduce(lambda x, y: x + y) / len(gender_sum)

# Print the final result
print(final_result)