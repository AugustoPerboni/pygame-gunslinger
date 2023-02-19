class Button:
    ''' Defines a button given a position, image and hitbox. '''
    def __init__(self,x,y,hitbox_width,hitbox_height,image):
        self.x = x
        self.y = y
        self.hitbox = (x,y,hitbox_width,hitbox_height)
        self.image = image