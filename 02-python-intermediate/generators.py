def my_generators():
    yield "First Value"
    print("This is the block under the first yield statement")
    yield "Second Value"
    print("This is the block under the second yield statement")
    yield "Third Value"
    print("This is the block under the third yield statement")

def main():
    try:
        g=my_generators()
        print(g)
        print(next(g))
        print(sorted(g))
        
    except StopIteration as e:
        print(f"ERROR:{e}")
        
if __name__=="__main__":
    main()