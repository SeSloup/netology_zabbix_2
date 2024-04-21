import os, sys, psutil 
def check_param(param):
    if param=='ram':
        tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[1].split()[1:][:3])
        print("%.2f" % (used_m/tot_m*100))

    elif param=='cpu':
        l1,l5,l15=psutil.getloadavg()
        print("%.2f" % (l5/os.cpu_count()*100))

check_param(sys.argv[1])


