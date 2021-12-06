import unittest 
from time import perf_counter

from collections import defaultdict 


# function to implement
# O(n2) 
def is_unique_chars_brute_force(str) : 

    for i in range(len(str)) : 

        for j in range(i+1,len(str)) : 

            if str[i] == str[j] : 

                return False 

    
    return True 

# using sorted based on Asicil values
# O(nlog(n)) 
def is_unique_chars_sorted(st) : 

    str = sorted(st) 

    
    for i in range(len(str) - 1) : 

        if str[i] == str[i+1] : 

            return False 

    return True 


# using set 

def is_unique_chars_set(st) : 

    str = set(st) 
    # if len of string unique len of set of string 
    if (len(st) != len(str)) : 
        return False 

    
    return True 


    

class Test(unittest.TestCase) : 

    testcases = [

        ("abce",True), 
        ("s4fad",True), 
        ("",True), 
        ("23ds2",False), 
        ("hd 627jh=j ()",False), 
        ("".join([chr(val) for val in range (128)]),True), 
        ("".join([chr(val//2) for val in range(129)]),False),
    ]
     
    
    test_functions = [
        is_unique_chars_brute_force, 
        is_unique_chars_sorted, 
        is_unique_chars_set
    ]

    def test_unique_chars(self) : 

        num_runs = 1000 
        function_runtimes = defaultdict(float) 

        for _ in range(num_runs) : 

            for text,expected in self.testcases :

                for is_unique_chars in self.test_functions : 

                    start =  perf_counter() 

                    assert(
                        is_unique_chars(text) == expected 
                    ), f"{is_unique_chars.__name__} fail for value :{text}" 

                    function_runtimes[is_unique_chars.__name__] += (
                        perf_counter() - start 
                    ) *1000 
        
        print (f"\n{num_runs} runs") 

        for function_name, runtime in function_runtimes.items() : 

            print(f"{function_name} : {runtime:.1f} ms")


if __name__ == "__main__" : 

    unittest.main()