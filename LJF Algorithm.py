def LJF(n, at, bt):
    wt = [0] * n # waiting time
    tat = [0] * n # turn around time
    rt = [0] *n # remaining time

    for i in range(n):
        rt[i] = bt[i]
    t = 0 # current time
    first = 0
    complete = 0
    check = False
    take = False
    while(complete != n):
        for j in range(n):
            if((at[j] <= t)and (rt[j]>0)):
                if (take):
                    if (bt[j] > bt[first]):
                        first = j
                    else:
                        continue
                else:
                    first = j
                check = True
                take = True
        take = False
        if(check == False):
            t += 1
            continue
        rt[first] =0
        t += bt[first]
        complete += 1

        wt[first] = (t - bt[first] - at[first]) #handeling -ve calculations
        if wt[first] < 0:
            wt[first] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT =total_wt / n
    ATT= total_tat /n
    return ATT,AWT
