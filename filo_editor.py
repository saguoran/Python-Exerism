

 #for changing
def changed(tabs_number, increment):
    change = 'bindex="'
    f = open('cc.txt', 'r+')
    target = open('ss.txt', 'w+')
    for line in f:
        if change in line:
            index = line.index(change)+len(change)
            newline = list(line)
            if tabs_number < 10:
                newline[index:index+1]=list(str(tabs_number))
            else:
                newline[index:index+2] = list(str(tabs_number))
            target.write(''.join(newline))
            tabs_number += increment
            continue
        else:
            target.write(str(line))
    f.closed
    target.close()

changed(1,2)#
 #for changing
#def changed():
#    tabs_number = int(input('Enter start index: '))
#    increment = int(input('Enter increment: '))
#    file=input("Enter the file name: ")
#    change = input("Enter the string before the target element: ")
#    target_file=input('Enter the new file name: ')
#    f = open(file, 'r+')
#    target = open(target_file, 'w+')
#    element_index = lambda x: x + len(change)
#    for line in f:
#        if change in line:
#            index=element_index(line.in#dex(change))
#            newline=list(line)
#            if tabs_number in range(50):
#                newline[index:index + 1] = list(str(tabs_number))
#            else:
#                newline[index:index + 2] = list(str(tabs_number))
#            target.write(''.join(newline))
#            tabs_number += int(increment)
#            continue
#        else:
#            target.write(str(line))
#    f.closed
#
#
#changed()
#

# get the indexs of lines
# get the indexs of the elements that need to be changed
# list the line and change the elements