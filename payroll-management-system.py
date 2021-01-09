'''
                    PAYROLL MANAGEMENT SYSTEM                                                                     
'''
from os import remove, rename

# Addition of records for New Employees in Employee File
def addrec():
    p = []
    no = empcode()    
    fout = open('EMPLOYEE_FILE.TXT', 'a')
    for no in range(n):
        no = no + 1
        while True:
            # Input Employee Name
            na = input('Employee Name? ')
            if not na.isalnum() or na.isdigit():
                print('Please enter proper Employee Name')
                na = input('Employee Name? ')
            elif na.isalpha() and len(na) <= 2 :
                print('Please enter proper Employee Name')
                na = input('Employee Name? ')
            else:
                break
        # Input Employee Gender
        gender = input('Gender [F/M]? ')
        while True:
            if not gender.isalpha():
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            elif gender.isalpha() and len(gender) != 1 :
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            elif gender.upper() != 'F' and gender.upper() != 'M' :
                print('Please enter Gender as either F- Female or M- Male')
                gender = input('Gender [F/M]? ')
            else:
                break
        # Input Date of Birth details
        print('Enter Employee Date of Birth details')
        dob = dateval()
        while len(dob) != 10:
            print(dob)
            print('Please enter Correct Date of Birth')
            dob = dateval()
        # Input Date of Joining details
        print('Enter Employee Date of Joining details')
        doj = dateval()
        while len(doj) != 10:
            print(doj)
            print('Please enter Correct Date of Joining')
            doj = dateval()
        # Input the Employee's Designation
        des = input('Employee Designation? ')
        # Input Basic Salary
        bs = input('Basic Salary? ')
        # Input the Employee's Phone number
        pn = input('Phone Number? ')
        validphone = phonevalidate(pn)
        if len(pn) == 10:
            while validphone == 1:
                print('Please enter New Phone Number as it already exists')
                pn = input('Phone Number? ')
                validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        else:
            print('Please enter New Phone Number with 10 digits')
            pn = input('Phone Number? ')
            validphone = phonevalidate(pn)
            while True:
                if pn in p:
                    print('Please enter New Phone Number as it already exists')
                    pn = input('Phone Number? ')
                else:
                    p += [pn]
                    break
        # Input the Employee's Mobile number                
        mob = input('Mobile Number? ')
        # Input the Employee's Address
        add = input('Address? ')
        
        data = str(no) +  ',' +  na.upper() +  ',' +  gender.upper() +  ',' +  dob +  ',' +  doj +  ',' +  des.upper() +  ',' +  bs +  ',' +  str(pn) +  ',' +  mob +  ',' +  add.upper() +  '\n'
        fout.write(data)
    print('\nEMPLOYEE RECORDS ADDED SUCCESSFULLY!\n')
    fout.close()
    
# Modification of existing records in Employee File except Employee Number and Employee Name

# Modification in Basic Salary
def modif1():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee's Designation
    desig = input('Designation to change Basic Salary? ')
    # Input amount by which Basic Salary has to be increased
    inc = int(input('Amount by which Basic Salary to be increased? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if arr[5] == desig.upper():
            found = 1
            arr[6] = str(int(arr[6]) + inc)
        print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n] ')
        if ch == 'Y' or ch == 'y':            
            print('BASIC SALARY UPDATED SUCCESSFULLY!\n')
        else:
            print('BASIC SALARY NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: DESIGNATION NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Modification in Designation
def modif2():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = input('Employee Number to change Designation? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Designation:', arr[5], '\t\t', 'Basic Salary :', arr[6])
            newdes = input('New Designation? ')
            newbs = input('New Basic Salary? ')
            if not newdes.isalnum() or newdes.isdigit():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            elif newdes.isalpha():
                print('Please enter proper Designation')
                newdes = input('New Designation? ')
            else:
                break
            print('Are you sure you want to change:\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdes.upper()
                arr[6] = newbs
                print('DESIGNATION UPDATED SUCCESSFULLY!\n')
            else:
                print('DESIGNATION NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')
    

# Modification in Gender
def modif3():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    found = 0
    # Input Employee Number
    no = input('Employee Number to change Gender? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Gender:', arr[2])
            gender = input('Gender [F/M]? ')
            while True:
                if not gender.isalpha():
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')  
                elif gender.isalpha() and len(gender) != 1:
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                elif gender.upper() != 'F' and gender.upper() != 'M':
                    print('Please enter Gender as either F- Female or M- Male')
                    gender = input('Gender [F/M]? ')
                else:
                    print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
                    ch = input('Enter your Choice [Y/y or N/n]? ')
                    if ch == 'Y' or ch == 'y':
                        arr[2] = gender
                        print('GENDER UPDATED!\n')
                    else:
                        print('GENDER NOT UPDATED!\n')
                        break    
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Modification in Date of Birth
def modif4():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = input('Employee Number to change Date of Birth? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Date of Birth:', arr[3])
            print('Enter a Correct Data of Birth')
            newdob = dateval()
            while len(newdob) != 10:
                print(newdob)
                print('Please enter Correct Date of Birth')
                newdob = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[4] = newdob
                print('DATE OF BIRTH UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF BIRTH NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Modification in Date of Joining
def modif5():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Date of Joining? '))
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name:', arr[1])
            print('Date of Joining:', arr[4])
            print('Enter a Correct Data of Joining')
            newdoj = dateval()
            while len(newdoj) != 10:
                print(newdoj)
                print('Please enter Correct Data of Joining')
                newdoj = dateval()
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[5] = newdoj
                print('DATE OF JOINING UPDATED SUCCESSFULLY!\n')
            else:
                print('DATE OF JOINING NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

# Modification in Phone Number
def modif6():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Phone Number? '))
    # Input New Phone Number
    newpn = input('New Phone Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Phone Number:', arr[7])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[7] = newpn
                print('Phone Number updated!\n')
            else:
                print('Phone Number not updated!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Modification in Mobile Number
def modif7():
    fin = open('EMPLOYEE_FILE.TXT')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Employee Number to change Mobile Number? '))
    # Input New Mobile Number
    newmob = input('New Mobile Number? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Mobile Number:', arr[8])
            print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                arr[8] = newmob
                print('MOBILE NUMBER UPDATED SUCCESSFULLY!\n')
            else:
                print('MOBILE NUMBER NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Modification in Address
def modif8():
    fin = open('EMPLOYEE_FILE.TXT')
    fout = open('TEMPORARY.TXT', 'w')
    # Input Employee Number
    no = int(input('Enter the Number for changing the Address- '))
    # Input New Address
    newadd = input('New address? ')
    found = 0
    for data in fin:
        data = data.strip()
        arr = data.split(',')
        if int(arr[0]) == no:
            found = 1
            print('Name :', arr[1])
            print('Address :', arr[9])
        print('Are you sure you want to change?\n\tY/y for Yes or N/n for No')
        ch = input('Enter your Choice [Y/y or N/n]? ')
        if ch == 'Y' or ch == 'y':
            arr[9] = newadd.upper()
            print('ADDRESS UPDATED SUCCESSFULLY!\n')
        else:
            print('ADDRESS NOT UPDATED!\n')
        rec = (',').join(arr)
        fout.write(rec  + '\n')
    if found == 0:
        print('\nERROR: EMPLOYEE NUMBER NOT FOUND!\n')
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT', 'EMPLOYEE_FILE.TXT')

# Searching in Employee File using following fields: Employee Number and Employee Name

# Searching using Employee Number
def search1():
    fout = open('EMPLOYEE_FILE.TXT', 'r')
    no = int(input('Employee Number? '))
    found = 0
    for line in fout:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            found = 1
            print(75 * '-')
            print('Employee Number :', arr[0], '\t\t\t\tEmployee Name :', arr[1])
            print('Gender :', arr[2], '\t\t\t\t\tDesignation :', arr[5])
            print('Date of Birth :', arr[3], '\t\t\tDate of Joining :', arr[4])
            print('Basic Salary : $'+ str(arr[6]))
            print('Phone Number :', arr[7], '\t\t\tMobile Number :', arr[8])
            print('Address :', arr[9])
            print(75 * '-')
    if found:
        print('\nEMPLOYEE SUCCESSFULLY DISPLAYED!\n')
    else:
        print('\nEMPLOYEE RECORD NOT FOUND!\n')
    fout.close()
    
# Searching using Employee Name
def search2():
    fout = open('EMPLOYEE_FILE.TXT', 'r')
    na = input('Employee Name? ')
    found = 0
    for line in fout:
        line = line.strip()
        arr = line.split(',')
        if arr[1] == na.upper():
            found = 1
            print(75 * '-')
            print('Employee Number :', arr[0], '\t\t\t\tEmployee Name :', arr[1])
            print('Gender :', arr[2], '\t\t\t\t\tDesignation :', arr[5])
            print('Date of Birth :', arr[3], '\t\t\tDate of Joining :', arr[4])
            print('Basic Salary : $'+ str(arr[6]))
            print('Phone Number :', arr[7], '\t\t\tMobile Number :', arr[8])
            print('Address :', arr[9])
            print(75 * '-')
    if found:
        print('\nEMPLOYEE SUCCESSFULLY DISPLAYED!\n')
    else:
        print('\nEMPLOYEE RECORD NOT FOUND!\n')
    fout.close()
        
# Input Number of days worked and other deductions of each Employee in Monthly Pay File
def mpayfile():
    arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    m, y = 0, 1
    maxdays_work = 0
    while True:
        if m not in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12] and y < 2015 :
            # Input Month
            m = int(input('Month? '))
            # Input Year
            y = int(input('Year? '))
        else:
            break
    if m in [1, 3, 5, 7, 8, 9, 10, 12]:
        maxdays_work = 27
    elif m in [4, 6, 9, 11]:
        maxdays_work = 26
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxdays_work = 25
        else:
            maxdays_work = 24
    file_name = 'Monthly_pay' + '_' + arr[m-1] + '_' + str(y) + '.txt'        
    fout = open(file_name, 'a')
    # Input Emplyee Number
    no = input('Employee Number? ')
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    for line in fin:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == str(no):
            print('Employee Name  :', arr[1])
            act_basic = int(arr[6])
            print('Basic  :', act_basic)
            #Validation for Number of working days
            #Calculation of Basic Salary
            leaves = int(input('Number of leaves taken in the month? '))
            if leaves >= 0 and leaves <= maxdays_work:
                days = maxdays_work - leaves
                mon_sal = (act_basic // maxdays_work) * days
            else:
                while leaves >= 0 and leaves <= maxdays_work:
                    print('Please enter valid Number of leaves')
                    leaves = int(input('Number of leaves taken in the month? '))
                    days = maxdays_work - leaves
            if days >= 0 and leaves <= days:
                mon_sal = (act_basic // maxdays_work) * days
                da = round(0.55 * mon_sal)
                hra = round(0.35 * mon_sal)
                conv = round(0.15 * mon_sal)
                gross = round(mon_sal + da + hra + conv)
                itax = round(0.05 * mon_sal)
                loan = round(0.1 * mon_sal)
                ded = round(itax + loan)
                net = round(gross - ded)
                print('\nBasic\tDA\tHRA\tConveyance\tGross\tItax\tLoan\tDeductions\tNet')
                print('-' * 90)
                print(str(mon_sal) +  '\t' +  str(da) +  '\t' +  str(hra) +  '\t' +  str(conv) +  '\t\t' +  str(gross) +  '\t' +  str(itax) +  '\t' +  str(loan) +  '\t' +  str(ded) +  '\t\t' +  str(net), '\n\nAdded in Monthly Pay File!\n')
                data = str(no) +  ',' +  arr[1].upper() + ',' +  arr[5].upper() +  ',' +  str(days) +  ',' +  str(mon_sal) +  ',' +  str(da) +  ',' +  str(hra) +  ',' +  str(conv) +  ',' +  str(gross) +  ',' +  str(itax) +  ',' +  str(loan) +  ',' +  str(net) +  '\n'
                fout.write(data)
    fout.close()

# Displaying Slary Statement
def sal_statement():
    arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    a = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    print('\n')
    print('*' * 36, ' XYZ COMPANY ', '*' * 36, '\n')
    print('Salary Statement for the month of:', a[m - 1], str(y))
    print(87 * '-')
    print('ENO\t NAME\t\t DESIGNATION\t BASIC\t GROSS\t DEDUCTIONS\t NET')
    print(87 * '-')
    file_name = 'Monthly_pay' + '_' + arr[m - 1] + '_' + str(y) + '.txt' 
    try: 
        with open(file_name, 'r') as fin:
            for line in fin:
                line = line.strip()
                arr = line.split(',')
                ded = int(arr[9]) +  int(arr[10])
                print(arr[0], '\t', arr[1], '\t', arr[2], '\t', arr[4], '\t', arr[8], '\t', ded, '\t\t', arr[11])
        print(87 * '-')
        print('\nSALARY STATEMENT DISPLAYED SUCCESSFULLY!\n')
    except:
        print("\nMONTHLY PAY FILE FOR", a[m - 1],str(y), "DOESN'T EXIST!\n")
             
# Displaying Slary Slip
def sal_slip():
    arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    a = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    # Input Employee Number
    no = input('Employee Number to display Salary Slip? ')
    file_name = 'Monthly_pay' + '_' + arr[m - 1] + '_' + str(y) + '.txt'
    try: 
        fout = open(file_name, 'r')
        print('\n')
        print('*' * 36, ' XYZ COMPANY ', '*' * 36, '\n')
        print('Salary Slip for the month of:', a[m - 1], str(y))
        for line in fout:
            line = line.strip()
            arr = line.split(',')
            if arr[0] == str(no):
                print(87 * '=')
                print('Employee Number :', arr[0] + '\t\t\t\t\tEmployee Name :', arr[1])
                print(87 * '-')
                print('Basic\t\t ' + '$' + arr[4] + '\t\t\t\t\tDeductions\t' + '$' + str(int(arr[9]) + int(arr[10])))
                print('DA\t\t', '$' + arr[5])
                print('HRA\t\t', '$' + arr[6])
                print('Conveyance\t', '$' + arr[7])
                print(87 * '-')
                print('Gross Pay\t' + ' $' + arr[8] + '\t\t\t\t\tNet\t\t' + '$' + arr[11])
                print(87 * '=')
                print("\n" + arr[1] + "'S SALARY SLIP FOR", a[m - 1], str(y), "DISPLAYED SUCCESSFULLY!\n")
                break
        else:
            print("EMPLOYEE NUMBER", no, "DOESN'T EXIST!\n")
        fout.close()
    except:
        print("MONTHLY PAY FILE FOR", a[m - 1], str(y), "DOESN'T EXIST!\n")

# Delete Employee records
def delete():
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fout = open('TEMPORARY.TXT', 'a')
    # Input Employee Number
    no = int(input('Employee Number to delete? '))
    # Input Employee Name
    na = input('Employee Name to delete? ')
    found = 0
    for data in fin:
        arr = data.split(',')
        if int(arr[0]) == no and arr[1] == na.upper():
            print('Name:', arr[1], '\t\t\t\t', 'Employee Number:', arr[0])
            print('Designation:', arr[5], '\t\t\t', 'Basic Salary :', arr[6])
            print('Date of Birth:', arr[3], '\t\t\t\t','Date of Joining:', arr[4])
            print('Are you sure you want to delete?\n\tY/y for Yes or N/n for No')
            ch = input('Enter your Choice [Y/y or N/n]? ')
            if ch == 'Y' or ch == 'y':
                print('RECORD SUCCESSFULLY DELETED!\n')
            else:
                print('RECORD NOT DELETED!\n')
        else:
            fout.write(data)
    fout.close()
    fin.close()
    if found == 0:
        print('\nERROR: RECORD NOT FOUND!\n')
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')
    
# Displaying Employee File   
def display_emp():
    fin = open('EMPLOYEE_FILE.TXT','r')
    print('\n')
    print(70 * "*", " EMPLOYEE PAY FILE ", 69 * "*")
    print(160 * '-')
    print('ENO  NAME\tGENDER DOB\t  DOJ\t     DESIGNATION\t\t      BASIC($)  PHONE       MOBILE      ADDRESS')
    print(160 * '-')
    for line in fin:
        line = line.strip()
        data = line.split(',')
        eno, na, gen, dob, doj, desig, bs, pnum, mnum, add = int(data[0]), data[1], data[2], data[3], data[4], data[5], float(data[6]), int(data[7]), int(data[8]), data[9]
        print('%i %-10s %s      %4s %s %-32s %-7.0f   %i  %i  %s'%(eno, na, gen, dob, doj, desig, bs, pnum, mnum, add))
    print(160 * '-')
    print('\nEMPLOYEE FILE DISPLAYED SUCCESSFULLY!')
    fin.close()
    print('\n')
    
# Displaying Monthly Pay File
def display_mon():
    x = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    a = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    print('\n')
    print('*' * 23,'\tMONTHLY PAY FILE (' +  x[m - 1] + '-', str(y) + ')\t', '*' * 22)
    print(87 * '-')
    print('ENO\t NAME\tDESIGNATION\t\t\tBASIC\t GROSS\t DEDUCTIONS\t NET')
    print(87 * '-')
    file_name = 'Monthly_pay' + '_' + x[m - 1] + '_' + str(y) + '.txt' 
    try: 
        fin = open(file_name, 'r')
        for line in fin:
            line = line.strip()
            arr = line.split(',')
            ded = int(arr[9]) + int(arr[10])
            print(arr[0], '\t', arr[1], '\t', arr[2], '\t', arr[4], '\t', arr[8], '\t', ded, '\t\t', arr[11])
        print(87 * '-')
        print('\nMONTHLY PAY FILE FOR',a[m - 1],str(y),'DISPLAYED SUCCESSFULLY!\n') 
    except:
        print("\nERROR: MONTHLY PAY FILE FOR",a[m - 1],str(y),"DOESN'T EXIST!\n")

# Automatic generation of Employee code       
def empcode():
    code = 1000
    fin = open('EMPLOYEE_FILE.TXT', 'r')
    fin.seek(0)
    first_char = fin.read(1)
    if not first_char:
         code = 1000
    else:
        for line in fin:
            line = line.strip()
            rec = line.split(',')
            code = int(rec[0])
    return(code)

# Validation for inputted date
def dateval():
    # Input Day
    d = int(input('Day? '))
    # Input Month
    m = int(input('Month? '))
    # Input Year
    y = int(input('Year? '))
    maxd = 0
    if m in [1, 3, 5, 7, 8, 9, 10, 12]:
        maxd = 31
    elif m in [4, 6, 9, 11]:
        maxd = 30
    elif m == 2: 
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            maxd = 29
        else:
            maxd = 28
    if maxd == 0:
        print('Please input valid Month')
    elif d < 1 or d > maxd:
        print('Please input valid Day')
    elif y < 1950 and y > 2001:
        print('Please input valid Year between 1950 and 2001')
    else:
        if len(str(m)) == 1:
            m = '0' +  str(m)
        if len(str(d)) == 1:
               d = '0' +  str(d)
        return (str(d) + '-' + str(m) + '-' + str(y))

# Validation for Phone Number
def phonevalidate(n):
    fin = open('EMPLOYEE_FILE.TXT','r')
    fin.seek(0)
    found = 0
    for line in fin:
        line = line.strip()
        rec = line.split(',')
        ph = rec[7]
        if ph == n:
            found = 1
            print('Same Phone Number found in records')
            break
    if len(fin.read()) == 0:
        found = 0
    return(found)

# Menu
while True:
    print('''Main Menu:
1. Addition of New Employee records in Employee File
2. Addition of Employee Pay File records in Monthly Pay File
3. Modification in existing records
4. Search for Employee records
5. Delete existing Employee records
6. Display files
7. Print Salary Statement
8. Print Salary Slip
0. Exit Main Menu\n''')
    ch = int(input('Choice[0-8]? '))
    if ch == 1:
        n = int(input('Number of Employees to be added? '))
        addrec()
    elif ch == 2:
        mpayfile()
    elif ch == 3:
        print('''\nModification in Employee details Menu:
1. Modify Basic Salary
2. Modify Designation
3. Modify Gender
4. Modify Date of Birth
5. Modify Date of Joining
6. Modify Phone Number
7. Modify Mobile Number
8. Modify Address
0. Exit Modification Menu\n''')
        a = int(input('Choice[0-8]? '))
        while True:
            if a == 1:
                modif1()
            elif a == 2:
                modif2()
            elif a == 3:
                modif3()
            elif a == 4:
                modif4()
            elif a == 5:
                modif5()
            elif a == 6:
                modif6()
            elif a == 7:
                modif7()
            elif a == 8:
                modif8()
            elif a == 0:
                break 
    elif ch == 4:
        print('''\nSearching for Employee details Menu:
1. Searching by Employee Number
2. Searching by Employee Name
0. Exit Search Menu\n''')
        a = int(input('Choice[0-2]? '))
        while True:
            if a == 1:
                search1()
                break
            elif a == 2:
                search2()
                break
            elif a == 0:
                break
    elif ch == 5:
        delete()
    elif ch == 6:
        print('''\nDisplay File Menu:
1. Display Employee File
2. Display Monthly Pay File
0. Exit Display Menu\n''')
        a = int(input('Choice[0-2]? '))
        if a == 1:
            display_emp()
        elif a == 2:
            display_mon()
        elif ch == 0:
            break
    elif ch == 7:
        sal_statement()
    elif ch == 8:
        sal_slip()
    elif ch == 0:
        print('\n', '*'* 54,'Thank You for Visiting!!','*'* 55, '\n')
        break
