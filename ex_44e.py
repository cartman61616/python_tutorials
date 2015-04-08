class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"


class Child(Other):

    def __init__(self):
        self.other = Other()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        super(Child, self).altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()

son.override()

son.altered()