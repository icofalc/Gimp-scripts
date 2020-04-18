def normalizza():
    img=gimp.image_list()[0]
    layer_copy=img.layers[0].copy()
    img.add_layer(layer_copy,3)
    print(img.layers)
    array_temp=[]
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x,y)[0]
            array_temp.append(r)
    
    massimo=max(array_temp)
    minimo=min(array_temp)
    print(minimo)
    print(massimo)
    
    costante=float(float(255) / float(massimo - minimo))
    print(costante)
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x, y)[0]
            
            if r >= minimo and r<=massimo:
                r=r-minimo
                r=r*costante
            layer_copy.set_pixel(x, y, (int(r),))
            
            
    pdb.gimp_drawable_update(layer_copy, 0, 0, layer_copy.width, layer_copy.height)
