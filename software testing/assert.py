from unittest import square
def main():
    print("invoking test square assert")
    test_square_assert()
def test_square_assert():
    assert(square(2)==4) 
    assert(square(3)==9)
    assert(square(-2)==4)
    assert(square(-3)==9)
if __name__=="__main__":
    main()        
