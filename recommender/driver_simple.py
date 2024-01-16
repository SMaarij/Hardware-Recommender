import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    print("Welcome To Laptop/Desktop Selector")

    engine.activate('bc_simple_rules') # activating rule file here

    
    try:
        with engine.prove_goal('bc_simple_rules.what_to_buy($buy)') as gen: 
            for vars, plan in gen:
                print("You should buy: %s" % (vars['buy']))

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


