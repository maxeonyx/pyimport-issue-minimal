import random


def do_thing():
    if random.random() < 0.9:
        raise Exception("Random failure")
    else:
        print("Success")


AN_ERROR_TO_CONFIRM_TYPECHECKING_IS_WORKING: int = "qwer"
