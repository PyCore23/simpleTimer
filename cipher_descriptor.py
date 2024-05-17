
class Cipher:
     """
     This class is now in develop.
     Im so sad because
     of descriptors concept complexity :(
     """
     def __set_name__(self, owner, name):
          self.attr = f"_{name}"

     def __get__(self, obj, owner):
          self.obj = obj
          return getattr(self.obj, self.attr)

     def __set__(self, owner, value):
          if isinstance(value, int):
               if value <= 0 or value > 60:
                    setattr(owner, self.attr, 0)
               else:
                    setattr(owner, self.attr, value)

     def __iadd__(self, number):
          current_value = getattr(self.obj, self.attr)
          new_value = current_value + number
          if new_value > 60:
               setattr(self.obj, self.attr, 0)
          else:
               setattr(self.obj, self.attr, new_value)