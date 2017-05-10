"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


class Node(object):

    def __init__(self, data):
        self.next = None
        self.data = data


class LL(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node):

        if self.head == node:
            self.head = node.next

            if self.tail == node:
                self.tail = None
            return

        current_node = self.head
        while current_node:
            if current_node.next == node:
                current_node.next = current_node.next.next

                if self.tail == node:
                    self.tail = current_node

            current_node = current_node.next


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    people = LL()
    for n in range(1, num_people + 1):
        people.append(n)

    person = people.head

    while people.head != people.tail:
        for i in range(kill_every - 1):
            if person == people.tail:
                person = people.head
            else:
                person = person.next

        if person == people.tail:
            next = people.head
        else:
            next = person.next

        people.remove(person)
        person = next

    return people.head.data



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
