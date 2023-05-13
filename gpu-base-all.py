import matplotlib.pyplot as plt

colors = ['black', 'red', 'blue', 'green', 'brown', 'purple', 'orange', 'pink', 'yellow', 'gray', 'olive', 'cyan']
labels = ["7_5", "7_6", "7_7", "7_8", "7_9"]

gpu_time = [
    [1042.716675	,781.805542	,499.873779	,417.73465	,378.333191	,356.102234	,343.041809	,320.241211	,296.592499	,279.219208],
    [1520.728149	,1098.97937	,746.137573	,649.461731	,547.644409	,528.296753	,485.989044	,470.123871	,454.208954	,438.180542],
    [494.945251	,188.602371	,229.718018	,214.023163	,228.807678	,215.493286	,227.428925	,215.07431	,228.200027	,214.187622],
    [494.945251	,188.602371	,229.718018	,214.023163	,228.807678	,215.493286	,227.428925	,215.07431	,228.200027	,214.187622],
    [2659.618896	,2174.368652	,1523.656738	,1320.946655	,1201.880005	,1137.834961	,1076.575317	,1033.969727	,997.73761	,962.896301],
]
data_x = [i for i in range(len(gpu_time[0]))]

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)

for i in range(len(gpu_time)):
    time = gpu_time[i]
    plt.plot(data_x, time, "o-", color=colors[i], label=labels[i])


plt.ylabel("GPU Time Each Iteration(ms)")
plt.xlabel("Iterations")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax.set_xlabel("Iterations", fontsize=18)
ax.set_ylabel("GPU Time Each Iteration(ms)", fontsize=18)
plt.legend(loc='upper right', fontsize=18)
plt.show()