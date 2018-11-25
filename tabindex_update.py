def changed(tabs_number, increment):
    change = 'bindex="'
    end_of_tab='"'
    f = open('cc.txt', 'r+')
    target = open('ss.txt', 'w+')
    for line in f:
        if change in line:
            print(line)
            index = line.index(change)+len(change)
            newline = list(line)
            quotation_index=index+1
            while True:
                print(str(index)+" "+end_of_tab,end='quotation: ')
                print(newline[quotation_index],end='quotation_index: ')
                if end_of_tab == newline[quotation_index]:
                    print(quotation_index)
                    break
                quotation_index+=1
            newline[index:quotation_index] = list(str(tabs_number))
            target.write(''.join(newline))
            tabs_number += increment
            continue
        else:
            target.write(str(line))
    f.closed
    target.close()

changed(1,2)