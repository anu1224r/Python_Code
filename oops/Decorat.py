def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)
hello()
