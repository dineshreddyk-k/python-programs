def grosssalary(basicsalary):
    if basicsalary <= 10000:
        hra = basicsalary * 20 / 100
        da = basicsalary * 80 / 100
    elif basicsalary <= 20000:
        hra = basicsalary * 25 / 100
        da = basicsalary * 90 / 100
    else:
        hra = basicsalary * 30 / 100
        da = basicsalary * 95 / 100
    gross = basicsalary + hra + da
    print("Basic Salary =", basicsalary)
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gross)
salary = float(input("Enter basic salary: "))
grosssalary(salary)