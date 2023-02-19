class Button:
    def __init__(self,x,y,hitbox_width,hitbox_height,image):
        self.x = x
        self.y = y
        hitbox = (x,y,hitbox_width,hitbox_height)
        self.image = image