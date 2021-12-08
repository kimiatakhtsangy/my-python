myTuple = (12, False, 1, "HUT", False, "HUT")


def find_twelve(myTuple):
    print("aya 12 vojood darad??")
    if 12 in myTuple:
        print("bale,12 hast!")
    else:
        print("na,12 nist!")


find_twelve(myTuple)
changeable = list(myTuple)
print("new changeable data structure:", type(changeable))
changeable2 = list(dict.fromkeys(changeable))
print("baghi mande bedoon tekrar:", changeable2)
