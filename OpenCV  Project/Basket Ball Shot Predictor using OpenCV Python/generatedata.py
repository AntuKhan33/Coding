import pandas as pd
import numpy as np

# Generate synthetic dataset of basketball shots
np.random.seed(42)
data = []

for i in range(200):
    # Random quadratic coefficients (simulate trajectories)
    A = -np.random.uniform(0.0005, 0.002)  # negative for downward parabola
    B = np.random.uniform(0.5, 2.0)        # initial velocity effect
    C = np.random.uniform(100, 200)        # initial height offset
    
    # Simulated hoop height at y=590
    c_new = C - 590
    
    # Solve quadratic for landing x at hoop height
    discriminant = B**2 - 4*A*c_new
    if discriminant < 0:
        continue
    
    x1 = (-B + np.sqrt(discriminant)) / (2*A)
    x2 = (-B - np.sqrt(discriminant)) / (2*A)
    
    # Pick a realistic landing x
    landing_x = x1 if 0 < x1 < 1000 else x2
    
    # Add label: shot made if landing_x is within hoop range (330–430)
    label = 1 if 330 < landing_x < 430 else 0
    
    data.append([A, B, C, landing_x, 590, label])

# Create dataframe
df = pd.DataFrame(data, columns=["A", "B", "C", "landing_x", "landing_y", "label"])

# Save to CSV
df.to_csv("synthetic_shot_dataset.csv", index=False)

print("Dataset generated and saved as synthetic_shot_dataset.csv")
print(df.head())
