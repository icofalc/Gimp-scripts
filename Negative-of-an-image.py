#getting the negative of an image
def sc():
    img=gimp.image_list()[0]
    layer_copy=img.layers[0].copy()
    img.add_layer(layer_copy,3)
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x, y)[0]
            g=layer_copy.get_pixel(x, y)[1]
            b=layer_copy.get_pixel(x, y)[2]
            #print(r)
            r=255-r
            g=255-g
            b=255-b
            layer_copy.set_pixel(x, y, (r,g,b,))
            
    pdb.gimp_drawable_update(layer_copy, 0, 0, layer_copy.width, layer_copy.height)
    
