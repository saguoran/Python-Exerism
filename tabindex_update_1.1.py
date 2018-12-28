with open(r'C:\Users\NonlicenseKnight\Desktop\test.txt','r') as rf:
    with open(r'C:\Users\NonlicenseKnight\Desktop\te.txt', 'w') as wf:
        import re
        from itertools import count
        index = count(1,2)
        for line in rf:
            rgex = re.compile(r'(tabindex="\d+")')
            groups = rgex.findall(line)
            new_line=line
            if groups:
                new_line = re.sub(rgex, 'SubstituteHere', line)
                for i in range(len(groups)):
                    new_line = new_line.replace('SubstituteHere', f'tabindex="{next(index)}"',1)
            wf.write(new_line)

