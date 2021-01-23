"""
Dunder Name e Dunder Main


Dunder --> double underline

Dunder Name --> __name__
Dunder Main --> __main__


The Python community use dunder to create functions, attributes, properties, etc, \
using Double Under to avoid conflict with the names of these elements in programming.


Why __name__ and __main__?

- In C language, we inicialize a program in the following way:
int main(){
    return 0;
}
- In Java language, the program have:
public static void main(String[] args){

}

Python doesn't need any of those. If we execute a python module in command line, \
the compilar will attribute the __main__ value to the variable __name, indicating \
this module is the principal execution module.
 - __name__ is an attribute every python file .py have.
"""

# In order for your python modules to not run script when you import
# them, you should add to the file:
if __name__ == '__main__':
    print("Your script should be entirely inside this block.")

