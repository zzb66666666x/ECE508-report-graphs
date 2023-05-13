import matplotlib.pyplot as plt

colors = ['black', 'red', 'blue', 'green', 'brown', 'purple', 'orange', 'pink', 'yellow', 'gray', 'olive', 'cyan']
labels = ["7_5", "7_6", "7_7", "7_8", "7_9"]

gpu_time = [
    [73.838593  ,71.574532	,65.991646	,61.280254	,58.332161	,56.251263	,54.312672	,52.626846	,51.38176	,50.451935],
    [91.116508 	,88.365059	,81.795006	,76.127167	,72.647713	,70.283485	,68.864159	,67.552322	,66.473663	,65.498337],
    [54.880257	,41.824257	,42.204128	,40.5504	,40.633343	,40.281631	,40.413696	,40.009857	,40.278526	,39.845886],
    [72.877022	,53.529598	,55.584766	,54.063072	,54.790146	,53.863106	,54.501377	,53.600513	,54.261536	,53.454594],
    [203.255814	,197.781509	,182.886398	,169.931778	,162.486267	,156.654404	,152.785477	,149.738174	,147.22554	,144.554108],
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