import matplotlib.pyplot as plt

colors = ['black', 'red', 'blue', 'green', 'brown', 'purple', 'orange', 'pink', 'yellow', 'gray', 'olive', 'cyan']
labels = ["7_5", "7_6", "7_7", "7_8", "7_9"]

gpu_time = [
    [73.926659	,71.857155	,66.394081	,61.987839	,59.547649	,85.118591	,84.677315	,89.002655	,89.973824	,89.643074],
    [102.875107	,99.238914	,91.412483	,84.998146	,81.804291	,110.292419	,108.276482	,112.317955	,114.912766	,113.228668],
    [54.603775	,41.617374	,42.194942	,41.069534	,41.769985	,49.343327	,50.277058	,49.657921	,51.064865	,50.834175],
    [65.031136	,49.351681	,50.916351	,49.549313	,50.325504	,62.724064	,62.363201	,64.281219	,64.663651	,62.872673],
    [204.008453	,198.558716	,183.755783	,171.638779	,165.449722	,216.502213	,223.518524	,227.224609	,225.571747	,221.957214],
]
gpu_old_time = [
    [88.305634	,87.11779	,80.183296	,79.965187	,65.583107	,63.707134	,62.255009	,60.976864	,59.914753	,58.984447],
    [108.082176	,107.095039	,96.618462	,97.189857	,81.759201	,79.674301	,78.255875	,77.188065	,76.134018	,75.278496],
    [55.013344	,49.53907	,49.723392	,48.731136	,41.735168	,40.846306	,41.567329	,40.683426	,41.262848	,40.555649],
    [74.344444	,65.782784	,66.485245	,67.629059	,55.667713	,54.403423	,55.335617	,54.158241	,55.261024	,54.082977],
    [191.602692	,193.321991	,174.603271	,181.752838	,149.906433	,146.164551	,143.792709	,141.738693	,140.044647	,138.633789],
]
data_x = [i for i in range(len(gpu_time[0]))]

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)

for i in range(len(gpu_time)):
    time = gpu_time[i]
    oldtime = gpu_old_time[i]
    plt.plot(data_x, time, "o-", color=colors[i], label=labels[i])
    plt.plot(data_x, oldtime, "--", color=colors[i])


plt.ylabel("GPU Time Each Iteration(ms)")
plt.xlabel("Iterations")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
ax.set_xlabel("Iterations", fontsize=18)
ax.set_ylabel("GPU Time Each Iteration(ms)", fontsize=18)
plt.legend(loc='upper right', fontsize=18)
plt.show()