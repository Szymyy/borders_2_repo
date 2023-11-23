class graphics_handler():
  def __init__(self):
    self.objects_background = []
    self.objects_object = []

  def add_object(self, background, object):
    if background:
      self.objects_background.append(object)
    else:
      self.objects_object.append(object)

  def remove_object(self, background, object):
    if background:
      self.objects_background.remove(object)
    else:
      self.objects_object.remove(object)

  def render_objects(self):
    for object in self.objects_background:
      object.draw()
    for object in self.objects_object:
      object.draw()