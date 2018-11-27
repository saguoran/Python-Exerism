f=open("region.txt",'w+')
for i in range(1,int(input('how many question do you want to creat?  '))+1):
    f.write('#region Q'+str(i))
    f.write('\n#endregion\n')
f.close