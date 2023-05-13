import matplotlib.pyplot as plt

gpu_time = [87.786499, 86.529022, 82.63683, 73.865219, 73.785347, 69.511490, 68.471199, 69.852287, 67.654175, \
                  65.667618, 64.739195, 68.114113, 62.804863, 62.060928, 60.407711, 60.846783, 58.505569, 54.442623, \
                  49.385952, 44.994879, 35.569218, 34.096863, 31.421696, 32.099487]
data_x = [i for i in range(len(gpu_time))]

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
plt.plot(data_x, gpu_time, "o-", color='black')

# for i, j in zip(data_x, gpu_time):
#     print(i,j)
#     plt.text(i, j+2, str(j), ha='center', va='bottom')

plt.ylabel("GPU Time Each Iteration(ms)")
plt.xlabel("Iterations")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax.set_xlabel("Iterations", fontsize=18)
ax.set_ylabel("GPU Time Each Iteration(ms)", fontsize=18)
plt.show()