#tabindex='1'
#012345678901
def changed(tabs_number, increment):
    change = 'bindex="'
    f = open('cc.txt', 'r+')
    target = open('ss.txt', 'w+')

    for line in f: # seach for tabindex in each line
        string_list = line.split()
        for index_list in range(len(string_list)): #how many tabindex in each line
            if change in string_list[index_list]:
               new_tab=list(string_list[index_list])
               end_quotation=0
               for quotation_end in range(-1, -20, -1):
                    if '"' == new_tab[quotation_end]:
                        end_quotation=quotation_end
                        break
               new_tab[10:end_quotation]=list(str(tabs_number))
               string_list[index_list]=''.join(new_tab)
               tabs_number += increment
        target.write(" ".join(string_list))
    f.closed
    target.close()

changed(1,2)