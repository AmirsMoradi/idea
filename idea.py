import numpy as np
import matplotlib.pyplot as plt
# Set the number of data
n_samples = 1000

# Generate random data from different distributions
normal_data = np.random.normal(loc=0, scale=1, size=n_samples)
uniform_data = np.random.uniform(low=-3, high=3, size=n_samples)
exponential_data = np.random.exponential(scale=1, size=n_samples)

# Set charts
plt.figure(figsize=(15, 5))

# Histogram for normal distribution
plt.subplot(1, 3, 1)
plt.hist(normal_data, bins=30, color='blue', alpha=0.7, label='Normal Distribution')
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Histogram for uniform distribution
plt.subplot(1, 3, 2)
plt.hist(uniform_data, bins=30, color='green', alpha=0.7, label='Uniform Distribution')
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()


# Histogram for exponential distribution
plt.subplot(1, 3, 3)
plt.hist(exponential_data, bins=30, color='red', alpha=0.7, label='Exponential Distribution')
plt.title('Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

#final setting
plt.tight_layout()
plt.show()