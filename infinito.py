def calcu(x, y):
    rats = []
    for j in range(len(x)):
        rats.append(x[j]/y[j])
    rats_final = list()
    rats_final.append(rats[0])
    rats_final.append(rats[1])
    rats_final.append((rats[2]*0.4))
    rats_final.append((rats[3]*0.3))
    rats_final.append((rats[4] * 0.15))
    rats_final.append((rats[5] * 0.15))
    print(rats)
    print(rats_final)
    print()
    print()
    net = 0
    comparer = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]
    i = 0
    # lower = upper = 0
    if rats_final[0] < 1:
        while rats_final[0] < comparer[i]:
            if i == len(comparer) - 1:
                lower = comparer[0]
                break
            else:
                lower = comparer[i+1]
            upper = comparer[i]
            i = i + 1
        summ = lower + rats_final[0] + upper
        aver = round((summ/3), 2)
        print(lower)
        print(rats_final[0])
        print(upper)
    elif rats_final[0] >= 1:
        aver = 1
    print("Average for Beta is:", aver)
    print()
    print()

    i = 0
    if rats_final[1] < 1:
        lowerp = upperp = 0
        while rats_final[1] < comparer[i]:
            if i == len(comparer) - 1:
                lowerp = comparer[0]
                break
            else:
                lowerp = comparer[i+1]
            upperp = comparer[i]
            i += 1
        summp = lowerp + rats_final[1] + upperp

        averp = round((summp/3), 2)
    elif rats_final[1] >= 1:
        averp = 1
    print("Average for % short float:", averp)
    print()
    print()
    comparer1 = [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]
    i = 0
    if rats[2] < 1:
        lowerp1 = upperp1 = 0
        while rats_final[2] < comparer1[i]:
            if i == len(comparer1) - 1:
                lowerp1 = comparer1[0]
                break
            else:
                lowerp1 = comparer1[i + 1]
            upperp1 = comparer1[i]
            i += 1
        summp1 = lowerp1 + rats_final[2] + upperp1
        averp1 = round((summp1/3), 2)
        print(lowerp1)
        print(rats_final[2])
        print(upperp1)
    elif rats[2] >= 1:
        averp1 = 0.4
    print("Average for ROE is", averp1)
    print()
    print()

    comparer2 = [0.3, 0.15, 0.075, 0.0375, 0.01875, 0.009375]
    i = 0
    if rats[3] < 1:
        lowerp12 = upperp12 = 0
        while rats_final[3] < comparer2[i]:
            if i == len(comparer2) - 1:
                lowerp12 = comparer2[0]
                break
            else:
                lowerp12 = comparer2[i + 1]
            upperp12 = comparer2[i]
            i += 1
        summp12 = lowerp12 + rats_final[3] + upperp12
        averp12 = round((summp12 / 3), 2)
        print(lowerp12)
        print(rats_final[3])
        print(upperp12)
    elif rats[3] >= 1:
        averp12 = 0.3
    print("Average for ROA is", averp12)
    print()
    print()

    comparer3 = [0.15, 0.075, 0.0375, 0.01875, 0.009375, 0.0046875]
    i = 0
    if rats[4] < 1:
        lowerp123 = upperp123 = 0
        while rats_final[4] < comparer3[i]:
            if i == len(comparer3) - 1:
                lowerp123 = comparer3[0]
                break
            else:
                lowerp123 = comparer3[i + 1]
            upperp123 = comparer3[i]
            i += 1
        summp123 = lowerp123 + rats_final[4] + upperp123
        averp123 = round((summp123 / 3), 2)
        print(lowerp123)
        print(rats_final[4])
        print(upperp123)
    elif rats[4] >= 1:
        averp123 = 0.15
    print("Average for ROCE is", averp123)
    print()
    print()
    i = 0
    if (rats[5] < 1):
        lowerp1234 = upperp1234 = 0
        while rats_final[5] < comparer3[i]:
            if i == len(comparer3) - 1:
                lowerp1234 = comparer3[0]
                break
            else:
                lowerp1234 = comparer3[i]
            upperp1234 = comparer3[i]
            i += 1
        summp1234 = lowerp1234 + rats_final[5] + upperp1234
        averp1234 = round((summp1234 / 3), 2)
        print(lowerp1234)
        print(rats_final[5])
        print(upperp1234)
    elif rats[5] >= 1:
        averp1234 = 0.15
    print("Average for 3 year sales growth is", averp1234)
    print()
    print()
    net2 = averp1 + averp12 + averp123 + averp1234
    net3 = 1 - net2
    net = aver + averp + net3
    rating_final = round(net, 3)
    print("RATING:", rating_final)
    print()
    print()
    return rating_final

