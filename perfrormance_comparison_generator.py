import matplotlib.pyplot as plt
import numpy as np
import os
import math
# Sample real test data (Replace with actual measured values)
num_simulations =  np.array([i for i in range(1, 21)])

# Execution times before and after optimization (replace with real data)
before_optimization = np.array([5 * i for i in range(1,21)])  # Assuming each simulation takes 10s in the old system
after_optimization = np.array([5 + 5 * (math.ceil(i/4)-1) for i in range(1, 21)])  # Example results from the optimized system
print([math.floor(i/5) for i in range(1, 21)])
# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(num_simulations, before_optimization, label="До оптимизации (1 контейнер)",
         color='red', linestyle='--', marker='o')
plt.plot(num_simulations, after_optimization, label="После оптимизации (4 контейнера)",
         color='blue', marker='s')

# Labels and title
plt.xlabel("Количество одновременных эмуляций")
plt.ylabel("Общее время выполнения (секунд)")
plt.title("Сравнение производительности: до и после оптимизации")
plt.legend()
plt.grid(True)

# Save the plot to a Windows-accessible location
save_path = os.path.join(os.environ["USERPROFILE"], "Documents", "performance_comparison.png")
plt.savefig(save_path, dpi=300)

# Show the plot
plt.show()

print(f"Graph saved at: {save_path}")
