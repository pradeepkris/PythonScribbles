

def Multiply_by_2(main_class):
    def wrapper_func(*args, **kwargs):
        x = main_class(*args, **kwargs)
        return "Result = " + str(x * 2)
    return wrapper_func

@Multiply_by_2
def Add_Hundred(x):
    return (x + 100)

@Multiply_by_2
def Div_Four(y):
    return (y / 4)

print Add_Hundred(20)
print Div_Four(40)

##########################################

def Extra_Func(fn_ptr):
    # 3. When wrapper called with parameter
    def Wrapper_Func(*args, **kwargs):
        # 1. Call the passed in functions and add extra functionality
        # 4. Execute the passed in function with parameter
        return "Add Extra to " + fn_ptr(*args, **kwargs)

    Wrapper_Func.data = 3 # Optional: Add attributes to functions

    # 2. Returns the pointer to wrapper function
    return Wrapper_Func

@Extra_Func
def Orig_Func(p1, p2):
    return "Original Func " + p1 + " " + p2

print Orig_Func("Yo", "Yo")
print Orig_Func.data
