def polinom(pol_1, pol_2):
    pol_1 = pol_1.split()
    pol_2 = pol_2.split()
    pol_3 = []

    if len(pol_1) >= len(pol_2):
        for i in range(0, len(pol_1) - len(pol_2), 2):
            pol_2.insert(0, '+')
            pol_2.insert(0, '0x')
        for i in range(0, len(pol_1) - 3, 2):
            pol_3.append(str(int(pol_1[i][:pol_1[i].find('x')]) + int(pol_2[i][:pol_2[i].find('x')])) + pol_1[i][
                                                                                                        pol_1[i].find(
                                                                                                            'x'):] + ' +')
        pol_3.append(str(int(pol_1[-3]) + int(pol_2[-3])) + ' = 0')

    if len(pol_2) > len(pol_1):
        for i in range(0, len(pol_2) - len(pol_1), 2):
            pol_1.insert(0, '+')
            pol_1.insert(0, '0x')
        for i in range(0, len(pol_2) - 3, 2):
            pol_3.append(str(int(pol_2[i][:pol_2[i].find('x')]) + int(pol_1[i][:pol_1[i].find('x')])) + pol_2[i][
                                                                                                        pol_2[i].find(
                                                                                                            'x'):] + ' +')
        pol_3.append(str(int(pol_2[-3]) + int(pol_1[-3])) + ' = 0')

    return ' '.join(pol_3)
