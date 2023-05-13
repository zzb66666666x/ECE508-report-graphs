import matplotlib.pyplot as plt

data_x = ["7_5", "7_6", "7_7", "7_8", "7_9"]
cpu_total_time = [15924, 18764, 22874, 28349, 37410]

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
plt.plot(data_x, cpu_total_time, "o-", color='black')

for i, j in zip(data_x, cpu_total_time):
    print(i,j)
    plt.text(i, j+100, str(j), ha='center', va='bottom')

plt.ylabel("CPU Total Time (ms)")
plt.xlabel("Dataset Names")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax.set_xlabel("Dataset Names", fontsize=18)
ax.set_ylabel("CPU Total Time (ms)", fontsize=18)
plt.show()