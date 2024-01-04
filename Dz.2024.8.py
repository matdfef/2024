class Klass:
   def init(self, data):
       self.data = data
   def iter(self):
       for item in self.data:
           yield item
iterable = Klass([1, 2, 3, 4, 5])
for item in iterable:
   print(item)