def bramma(n, source, helper, target):
    if n > 0:
        print "working for : " + str(n-1)
        # move tower of size n-1 to helper:
        bramma(n-1, source, target, helper)

        # move disk from source peg to target peg
        if source:
            print "popping"
            target.append(source.pop())

        # move tower of size n-1 from helper to target
        bramma(n-1, helper, source, target)


source = [4, 3, 2, 1]
target = []
helper = []

bramma(4, source, helper, target)
