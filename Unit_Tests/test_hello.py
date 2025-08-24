from hello import hello
 
def test_dafault():
    assert hello() == "hello, world" 
    
def test_argument():
    assert hello("Pepu") == "hello, Pepu"