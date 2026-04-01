import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'C:/Users/39334/CTM/ct7/SES/Bending Tests/3.Runde/27_03_2025_Versuche/Aramid_03_3.5_resampled.csv'
df = pd.read_csv(file_path)

# Ensure the columns are numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Extract necessary columns
x = df.iloc[:, 2]  # Deflection
y1 = df.iloc[:, 1]  # Load

# Compute stiffness gradient
stiffness_gradient = np.gradient(np.gradient(y1, x), x)

# Always start the linear elastic region at the first data point
x_linear = [x.iloc[0]]
y_linear = [y1.iloc[0]]

# Iterate through the data to detect the end of the linear region
for i in range(1, len(x)):
    x_linear.append(x.iloc[i])
    y_linear.append(y1.iloc[i])
    
    # Fit a line to the growing linear region
    coeffs = np.polyfit(x_linear, y_linear, 1)  # Linear fit
    predicted_y = np.polyval(coeffs, x_linear)  # Compute predicted values

    # Compute deviation from the trend line
    deviation = np.abs(np.array(y_linear) - predicted_y)

    # Set a threshold (e.g., 1% of max Load) to define when non-linearity starts
    threshold = 0.01 * max(y1)  

    # Stop if deviation exceeds the threshold
    if deviation[-1] > threshold:
        x_linear.pop()  # Remove last point since it's non-linear
        y_linear.pop()
        break  

# Fit a final straight line to the detected linear elastic region
coeffs = np.polyfit(x_linear, y_linear, 1)
linear_fit = np.polyval(coeffs, x_linear)

# Define points to highlight (including first and last point of linear region)
highlight_points = [(x_linear[0], y_linear[0]), (x_linear[-1], y_linear[-1])]

# Print coordinates of the highlighted points
print('Start/Endpoint linear elastic region:')
for point in highlight_points:
    print(f'({str(point[0]).replace(".", ",")}, {str(point[1]).replace(".", ",")})')

# Print maximum value of the second column (Load)
max_force = y1.max()  # Find maximum value of Load (second column)
print(f'Maximum Load: {str(max_force).replace(".", ",")} N')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Load-Deflection Curve')
plt.plot(x, stiffness_gradient, label='Stiffness Gradient', color='orange')

# Highlight specific points (first and last of the linear region)
for point in highlight_points:
    plt.scatter(point[0], point[1], color='green', s=50, zorder=3)
    plt.annotate(f'({point[0]:.3f}, {point[1]:.3f})',
                 (point[0], point[1]),
                 textcoords="offset points",
                 xytext=(-20, 10),
                 ha='left',
                 fontsize=10,
                 color='black')

# Add labels and legend
plt.xlabel('Deflection [mm]')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Show the plot
plt.show()
