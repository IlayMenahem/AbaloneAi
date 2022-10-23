from PIL import Image, ImageDraw

def row_length(row):
    if(row<5):
        return row+5
    else:
        return 13-row

def state2pic(board):
    #1 empty
    #2 white
    #3 black
    ''' create image og width w and height h
    assign each pixel x,y with op(x,y) '''
    img = Image.new(mode='L', size=(900,900), color=255)
    mat = img.load()
    for x in range(900):
        for y in range(900):
            mat[x,y] = 127
    for row in range(9):
        l = row_length(row)
        distance_between_centers = 60
        radius = 20
        min_x = 450-int(distance_between_centers/2)*(l-1)
        y = 450 + int((row-4)*distance_between_centers/1.118)

        for index in range(l):
            val = board[row][index]
            if(val==1):
                #draws a ghost
                current_x=min_x+distance_between_centers*index
                current_y=y
                for pixel_x in range(current_x-radius,current_x+radius):
                    for pixel_y in range(current_y-radius,current_y+radius):
                        if((current_x-pixel_x)**2+(current_y-pixel_y)**2<radius**2):
                            mat[pixel_x,pixel_y] = 140
            if(val==2):
                #draws white
                current_x=min_x+distance_between_centers*index
                current_y=y
                #print(current_x,current_y)
                for pixel_x in range(current_x-radius,current_x+radius):
                    for pixel_y in range(current_y-radius,current_y+radius):
                        if((current_x-pixel_x)**2+(current_y-pixel_y)**2<radius**2):
                            mat[pixel_x,pixel_y] = 255
            elif(val==3):
                #draws black
                current_x=min_x+distance_between_centers*index
                current_y=y
                for pixel_x in range(current_x-radius,current_x+radius):
                    for pixel_y in range(current_y-radius,current_y+radius):
                        if((current_x-pixel_x)**2+(current_y-pixel_y)**2<radius**2):
                            mat[pixel_x,pixel_y] = 0
    img.show()
