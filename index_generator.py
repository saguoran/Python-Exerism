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

changed(1,2)
