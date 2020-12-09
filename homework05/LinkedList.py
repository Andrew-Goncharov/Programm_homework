import random
from typing import Optional

class Node:
    def __init__(self, cont_object, next_node=None):
        self.contained_object = cont_object
        self.next = next_node

class MyQueue:
    def __init__(self):
        self.head: Optional[Node] = None

    def add(self, contained_object):
        new_node = Node(contained_object, self.head)
        self.head = new_node

    def remove(self):
        if self.head == None:
            raise ValueError("Empty queue")
        elif self.head.next == None:
            contained_object = self.head.contained_object
            self.head = None
            return contained_object
        prev, cur = self.head, self.head.next
        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None
        return cur.contained_object

    def clear(self):
        self.head = None

    def to_list(self):
        result = []
        if self.head == None:
            return result
        cur = self.head
        while cur != None:
            result.append(cur.contained_object)
            cur = cur.next
        return result

class Country:
    def __init__(self, name, population, capital, lands):
        self.name = name
        self.population = population
        self.capital = capital
        self.lands = lands
    def __str__(self):
        return "Name of County: {0}, Population: {1}, Capital: {2}, Amount of lands: {3}".format(self.name, self.population, self.capital, self.lands)

Russia = Country("Russia", 146630227, "Moscow", 85)
England = Country("England", 55977500, "London", 9)
Germany = Country("Germany", 83149300, "Berlin", 16)
France = Country("France", 67081000, "Paris", 17)

country_queue = MyQueue()
country_queue.add(str(Russia))
country_queue.add(str(England))
country_queue.add(str(Germany))
country_queue.add(str(France))

digital_queue = MyQueue()
count = random.randint(0, 100)
for digit in range(count):
    digital_queue.add(digit)


print(country_queue.to_list())
print(digital_queue.to_list())