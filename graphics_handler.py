class Graphics_Handler():
  def __init__(self):
    self.objects_background = []
    self.objects_foreground = []
    
# initilalises the Graphics_Handler class with two empty lists of background and foreground objects

  def add_object(self, background, object):
    if background:
      self.objects_background.append(object)
    else:
      self.objects_foreground.append(object)

# allows an object to be added to either the foreground or background list. taking two parameters of background and object, background checking whether it belongs in the background list or not.
  
  def remove_object(self, background, object):
    if background:
      self.objects_background.remove(object)
    else:
      self.objects_foreground.remove(object)

# allows an object to be removed from either list, taking two parameters and functioning just like add_object()

  def render_objects(self):
    for object in self.objects_background:
      object.draw()
    for object in self.objects_foreground:
      object.draw()

# iterates through every object in each list and calls it's .draw() function in order to render them on the screen.