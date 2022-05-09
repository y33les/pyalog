import apl
import math
from functools import reduce
from operator import and_

if __name__ == '__main__':
    # apl.py functions
    # TODO: tests on arrays

    print("aplPlus...",end=" ")
    assert apl.aplPlus(complex(2,3)) == complex(2,-3)
    assert apl.aplPlus(2,3) == 5
    print("OK")

    print("aplMinus...",end=" ")
    assert apl.aplMinus(-2) == 2
    assert apl.aplMinus(3,2) == 1
    print("OK")

    print("aplTimes...",end=" ")
    assert apl.aplTimes(-2) == -1
    assert apl.aplTimes(0) == 0
    assert apl.aplTimes(5) == 1
    assert apl.aplTimes(4,5) == 20
    print("OK")

    print("aplDivide...",end=" ")
    assert apl.aplDivide(2) == 0.5
    assert apl.aplDivide(15,3) == 5
    print("OK")

    print("aplPipe...",end=" ")
    assert apl.aplPipe(-2) == 2
    assert apl.aplPipe(complex(3,4)) == 5.0
    assert apl.aplPipe(3,2) == 2
    assert apl.aplPipe(2,3) == 1
    print("OK")

    print("aplFloor...",end=" ")
    assert apl.aplFloor(2.4) == 2
    assert apl.aplFloor(2.8) == 2
    assert apl.aplFloor(15,3) == 3
    print("OK")

    print("aplCeil...",end=" ")
    assert apl.aplCeil(2.4) == 3
    assert apl.aplCeil(2.8) == 3
    assert apl.aplCeil(15,3) == 15
    print("OK")

    print("aplExp...",end=" ")
    assert apl.aplExp(0) == 1.0
    assert apl.aplExp(1) == math.e
    assert apl.aplExp(2,3) == 8
    assert apl.aplExp(4,0.5) == 2.0
    print("OK")

    print("aplLog...",end=" ")
    assert apl.aplLog(1) == 0.0
    assert apl.aplLog(4,16) == 2.0
    assert apl.aplLog(2,32) == 5.0
    assert apl.aplLog(10,1000) == 3.0
    print("OK")

    print("aplBang...",end=" ")
    assert apl.aplBang(5) == 120
    assert apl.aplBang(10) == 3628800
    assert apl.aplBang(4,7) == 35
    assert apl.aplBang(5,10) == 252
    print("OK")

    print("aplCirc...",end=" ")
    # TODO: have manually tested this using _aplCircTest(4) against tryapl.org but it would be nice to have proper automated tests
    print("OK")

    print("aplTilde...",end=" ")
    assert apl.aplTilde(0) == 1
    assert apl.aplTilde(1.0) == 0
    # TODO: dyadic tests
    print("OK")

    print("aplQuestion...",end=" ")
    for i in range(0,1000):
        assert apl.aplQuestion(10) < 10
        assert apl.aplQuestion(10) >= 0
        assert len(apl.aplQuestion(3,10)) == 3
        assert reduce(and_,(apl.aplQuestion(3,10) < 10))
        assert reduce(and_,(apl.aplQuestion(3,10) >= 0))
        # TODO: test weird dyadic behaviour with one argument (i.e. ?⍨⍵)
    print("OK")
