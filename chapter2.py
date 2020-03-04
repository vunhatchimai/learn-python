import sys
import os

# Global Variables
global_string = "I'm global"

# Global Functions
def get_sale_item_amz(item_name1, item_name2):
    # return item_name1[len(item_name1):len(item_name1)//2-1:-1] + " and " + item_name2
    # return item_name1[::-1]
    a = 4.0
    b = 2

    if a % b == 0:
        return a/b
    else:
        return a+b

# string concantenate (+)

# Class definitions (inside properties, class functions)

def main():
    print(str(get_sale_item_amz("book", "jeans")) + " dep zai " * 10)
    print(global_string)

# Main
if __name__ == "__main__":
    main()

