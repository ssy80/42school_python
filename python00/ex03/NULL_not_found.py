

def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, bool):
        if object is False:
            print(f"Fake: {object} {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int):
        if object == 0:
            print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str):
        if len(object) == 0:
            print(f"Empty: {type(object)}")
        else:
            print("Type not Found")
    return 1
