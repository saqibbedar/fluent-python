x = "global"

def f():
    y = "local"
    print(locals())
    print(locals() is globals())    # False: because here locals() is tied to function call and its private local namespace, hence, output of print(locals()) is {'y': 'local'}

f()

print(locals() is globals())        # True: because locals() and global() at top level shares same dict.