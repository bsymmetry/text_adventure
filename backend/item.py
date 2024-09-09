class Item:

   # name is a str; use is an Item object that can be used 
   # on this item (i.e. key to a door); description is a str
   def __init__ (self, name, use, description, useDescription):
       self.name = name
       self.use = use 
       self.description = description
       self.useDescription = useDescription
