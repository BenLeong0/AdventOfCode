x = 952316487
day23_input = [int(i) for i in str(x)]

class Cup:
    def __init__(self,val,next):
        self.val = val
        self.next = next


def cupgame(n, day23_input=day23_input[:], part2=False):
    if part2:
        day23_input.extend(range(10,1_000_001))

    last = max(day23_input)
    prev = lambda c: c.val-1 if c.val>1 else last

    cups, curr = {}, None
    for cup in day23_input[::-1]: curr = cups[cup] = Cup(cup, curr)
    cups[day23_input[-1]].next = curr

    for move in range(n):
        nextVals = [curr.next, curr.next.next, curr.next.next.next]
        curr.next = nextVals[2].next
        dest = cups[prev(curr)]
        while dest in nextVals: dest = cups[prev(dest)]
        dest.next, nextVals[2].next = nextVals[0], dest.next
        curr = curr.next

    return cups[1]


def partOne():
    x = cupgame(100)
    for _ in range(8):
        x = x.next
        print(x.val, end='')
    print()


def partTwo():
    x = cupgame(10_000_000,part2=True)
    a = x.next.val
    b = x.next.next.val
    return print(a*b)

partOne()
partTwo()

# partOne()
# partTwo()
