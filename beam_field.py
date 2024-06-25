import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the range of x and y values
x = np.linspace(-5, 5, 100)  # 100 points between -5 and 5
y = np.linspace(-5, 5, 100)  # 100 points between -5 and 5

# Step 2: Create the meshgrid
X, Y = np.meshgrid(x, y)

# Step 3: Define the parameters a and b
a = 1
b = 5

# Step 4: Apply the function to the meshgrid
Z = np.exp(1j * a * X) + np.exp(1j * b * Y)

# Step 5: Extract the real and imaginary parts of the function
Z_real = np.real(Z)
Z_imag = np.imag(Z)

# Step 6: Visualize the real part of the function
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.contourf(X, Y, Z_real, cmap='gray')
plt.colorbar(label='Real Part')
plt.title(f"Real Part of $\\exp(i {a} x) + \\exp(i {b} y)$")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Step 7: Visualize the imaginary part of the function
plt.subplot(1, 2, 2)
plt.contourf(X, Y, Z_imag, cmap='gray')
plt.colorbar(label='Imaginary Part')
plt.title(f"Imaginary Part of $\\exp(i {a} x) + \\exp(i {b} y)$")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.tight_layout()
plt.show()
