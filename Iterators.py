class cntr:

    def __init__(self, inputnum):
        self.i = 0
        self.n = inputnum

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i = i + 1

            return i
        else:
            raise StopIteration()

y = cntr(3);
print y.next()
print y.next()

###################################
class Reverse_Iter(object):

    def __init__(self, lst):
        self.i = lst

    def __iter__(self):
        return self

    def next(self):
        loc_lst = self.i
        for j in loc_lst[::-1]:
            self.i = list(loc_lst[:len(loc_lst)-1])
            return j

        raise StopIteration()

###################################
x = Reverse_Iter([1,2,3,4])
print sum(Reverse_Iter([1,2,3,4]))

print sum(x)
try:
    print x.next()
except StopIteration:
    print 'Failed to Iterate, since sum(x) exhausted the iteration'
    print ''

###################################
y = Reverse_Iter([1,2,3,4])
print y.next()
print y.next()
print y.next()
print y.next()

###################################
