def eq():
    img=gimp.image_list()[0]
    layer_copy=img.layers[0].copy()
    img.add_layer(layer_copy,3)
    array_temp=[]
    
    M=layer_copy.width
    M=float(M)
    N=layer_copy.height
    N=float(N)
    
    print(M*N)
    
    for i in range(0,256):
        highlights = pdb.gimp_histogram(layer_copy, 0, i, i)
        count=float(highlights[4]/(M*N))
        array_temp.append(count)
        
    #print(array_temp)
    Tri=[]#in Tri ho i valori equalizzati
    for i in range(0,256):
        accumulatore=0
        for j in range(0,i+1):
            accumulatore=accumulatore+array_temp[j]
        Tri.append(int(round(255*accumulatore)))
    print(Tri)
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x, y)[0]
            
            finale=Tri[r]
            
            layer_copy.set_pixel(x, y, (int(finale),))
            
            
    pdb.gimp_drawable_update(layer_copy, 0, 0, layer_copy.width, layer_copy.height)
