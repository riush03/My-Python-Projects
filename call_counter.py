class Counter:
    def __init__(self,func):
        self.func = func
        self.first_count = 0
    def __call__(self, *args, **kwargs):
        self.incremental_counts += 1
        return self.func(*args,**kwargs)

if __name__ == "__main__":
    @Counter
    def calling_counter():
        print("Calling...")
    calling_counter.first_count
    print("\n------------------next")
    

