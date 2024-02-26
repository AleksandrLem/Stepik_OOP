def fun(info):
    a, b = '', ''
    a, b, = info.split()
    print(a, b)


fun('gdf sfdg')
