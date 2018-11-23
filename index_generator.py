def changed(tabs_number, increment):
    change = 'bindex="'
    f = open('cc.txt', 'r+')
    target = open('ss.txt', 'w+')
    for line in f:
        if change in line:
            index = line.index(change)+len(change)
            newline = list(line)
            if tabs_number < 10:
                newline[index:index+1] = list(str(tabs_number))
            else:
                newline[index:index+2] = list(str(tabs_number))
            target.write(''.join(newline))
            tabs_number += increment
            continue
        else:
            target.write(str(line))
    f.closed
    target.close()


def generator_from_blank(tabs_number, increment):
    end_with = 'type="'
    f = open('cc.txt', 'r+')
    target = open('ss.txt', 'w+')
    for line in f:
        if end_with in line:
            index = line.index(end_with)
            newline = list(line)
            newline[index - 1:index] = list(' tabindex="' + str(tabs_number) + '" ')
            target.write(''.join(newline))
            tabs_number += increment
            continue
        else:
            target.write(str(line))
    f.closed
    target.close()


generator_from_blank(1, 2)
