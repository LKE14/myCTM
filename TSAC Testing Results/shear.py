import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'C:/Users/39334/CTM/ct7/SES/Bending Tests/3.Runde/27_03_2025_Versuche/Scherung_03_3_resampled.csv'
df = pd.read_csv(file_path)

# Ensure the columns are numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Extract necessary columns
x = df.iloc[:, 2]  # Deflection
y1 = df.iloc[:, 1]  # Load


# Print maximum value of the second column (Load)
max_force = y1.max()  # Find maximum value of Load (second column)
print(f'Maximum Load: {str(max_force).replace(".", ",")} N')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Load-Deflection Curve')

# Add labels and legend
plt.xlabel('Deflection [mm]')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Show the plot
plt.show()
