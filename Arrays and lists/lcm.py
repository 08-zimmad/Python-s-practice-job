def lcm(n1,n2):
    gt_n=0    
    if n1>n2:
        gt_n=n1
    else:
        gt_n=n2
    while True:
        if gt_n%n1==0 and gt_n%n2==0:
            lcm=gt_n
            break
        gt_n=gt_n+1

    return lcm


print(lcm(24,32))