with open('customer_record.txt', 'r') as f:
    r = f.read()
    lines = r.split('\n')
    print(lines)
    lines = lines.pop()
    for i in range(len(lines)):
        g=lines.split(',')
        print(g)

        # print('customer no:',i)
        # print('name',g[0],'email',g[1],'\n','total bill:',g[3],'time:',g[4])
        # for j in range(5,len(g)):
        #     print('product id:',g[j],'name of product',g[j+1],'price',g[j+2],'no of items he ordered:',g[j+3])