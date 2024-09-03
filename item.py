class Item:

   # name is a str; use is an Item object that this item can be used 
   # on (i.e. key to a door); description is a str
   def __init__ (self, name, use, description):
       self.name = name
       self.use = use 
       self.description = description
