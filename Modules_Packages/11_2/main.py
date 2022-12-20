from mypackage import module1 as m1, module2 as m2
from mypackage.mysubpackage.module3 import people

m1.greet("Pythonista")
m2.depart("Pythonista")

for person in people:
    m1.greet(person)