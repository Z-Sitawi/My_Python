if __name__ == '__main__':
    from Activité1 import Point, TroisPoints

    """ la patie du class Point """
    def print_points(p_list):
        i = 1
        for x in p_list:
            print(f"p{i}{x}", end=" ")
            i += 1
        print("")

    p1 = Point(2, 2)
    p2 = Point(4, 1)

    print("================================ Point ====================================\n")
    print_points([p1, p2])
    print("_______________________________________________________\n")
    print(f"La point au milieu de p1 et p2 est: pm{p1.calculermilieu(p2)}")
    print("_______________________________________________________\n")
    print(f"la distance entre p1 et p2 = {round(p1.calculerdistance(p2), 2)} m\n")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    """ la patie du class TroisPoints """
    print("\n================================ TroisPoints ==============================\n")

    def test_sontalignes(my_object):

        if my_object.sontalignes():
            print("===> les points p1 , p2 et p3 sont alignés <===")
        else:
            print("===> les points p1 , p2 et p3 sont (( pas )) alignés <===")
        print("\n_______________________________________________________\n")

    def test_estisocele(my_object):
        if my_object.estisocele() == 100:
            print("les trois points ne forment pas un triangle")
            return ""
        elif my_object.estisocele():
            print("===> les points p1 , p2 et p3 forment un triangle isocèle <===")
        else:
            print("===> les points p1 , p2 et p3 ne forment (( pas )) un triangle isocèle <===")
        print("\n_______________________________________________________")


    p3 = Point(3, 2)
    _P1_P2_P3_ = TroisPoints(p1, p2, p3)

    print_points([_P1_P2_P3_.point1, _P1_P2_P3_.point2, _P1_P2_P3_.point3])
    print("_______________________________________________________\n")
    test_sontalignes(_P1_P2_P3_)
    test_estisocele(_P1_P2_P3_)

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Modifer l'abssice et ordonee des points:")
    _P1_P2_P3_.point2 = _P1_P2_P3_.point3 = p1
    print_points([_P1_P2_P3_.point1, _P1_P2_P3_.point2, _P1_P2_P3_.point3])
    print("_______________________________________________________\n")
    test_sontalignes(_P1_P2_P3_)
    test_estisocele(_P1_P2_P3_)

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Modifer l'abssice et ordonee des points:")
    _P1_P2_P3_.point1.abs = _P1_P2_P3_.point1.ord = _P1_P2_P3_.point3.ord = 1

    print_points([_P1_P2_P3_.point1, _P1_P2_P3_.point2, _P1_P2_P3_.point3])
    print("_______________________________________________________\n")
    test_sontalignes(_P1_P2_P3_)
    test_estisocele(_P1_P2_P3_)

    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
