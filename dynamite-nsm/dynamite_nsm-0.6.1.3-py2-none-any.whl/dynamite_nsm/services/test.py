cpu_count = 10
cpus = [c for c in range(0, cpu_count)]
if cpu_count > 1:
    pinned_cpus = cpus[:-1]
    lb_procs = len(pinned_cpus)
else:
    pinned_cpus = cpus
    lb_procs = 1

print(lb_procs, cpus)
