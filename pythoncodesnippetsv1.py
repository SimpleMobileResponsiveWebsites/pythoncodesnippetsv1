import streamlit as st

def get_code_snippet(statement):
    snippets = {
        'continue': 'for i in range(5):\n    if i == 2:\n        continue\n    print(i)',
        'def': 'def greet(name):\n    return f"Hello, {name}!"',
        'del': 'my_list = [1, 2, 3, 4]\ndel my_list[1]\nprint(my_list)',
        'elif': 'x = 10\nif x > 15:\n    print("x is greater than 15")\nelif x > 5:\n    print("x is greater than 5 but not greater than 15")\nelse:\n    print("x is not greater than 5")',
        'else': 'x = 3\nif x > 5:\n    print("x is greater than 5")\nelse:\n    print("x is not greater than 5")',
        'except': 'try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")',
        'for': 'fruits = ["apple", "banana", "cherry"]\nfor fruit in fruits:\n    print(fruit)',
        'global': 'global_var = 10\n\ndef modify_global():\n    global global_var\n    global_var = 20\n\nmodify_global()\nprint(global_var)',
        'if': 'x = 5\nif x > 0:\n    print("x is positive")',
        'import': 'import math\nprint(math.pi)',
        'nonlocal': 'def outer():\n    x = "local"\n    def inner():\n        nonlocal x\n        x = "nonlocal"\n    inner()\n    print(x)',
        'pass': 'class EmptyClass:\n    pass',
        'raise': 'def validate_age(age):\n    if age < 0:\n        raise ValueError("Age cannot be negative")',
        'return': 'def add(a, b):\n    return a + b\n\nresult = add(3, 4)\nprint(result)',
        'try': 'try:\n    result = 10 / 2\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")\nelse:\n    print(f"The result is {result}")',
        'while': 'count = 0\nwhile count < 5:\n    print(count)\n    count += 1',
        'with': 'with open("example.txt", "w") as file:\n    file.write("Hello, World!")',
        'yield': 'def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor number in countdown(5):\n    print(number)'
    }
    return snippets.get(statement, "No example available for this statement.")

def get_set_example(method):
    examples = {
        'add': "my_set = {1, 2, 3}\nmy_set.add(4)\nprint(my_set) # Output: {1, 2, 3, 4}",
        'clear': "my_set = {1, 2, 3}\nmy_set.clear()\nprint(my_set) # Output: set()",
        'copy': "original = {1, 2, 3}\ncopied = original.copy()\nprint(copied) # Output: {1, 2, 3}",
        'difference': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nprint(set1.difference(set2)) # Output: {1, 2}",
        'difference_update': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nset1.difference_update(set2)\nprint(set1) # Output: {1, 2}",
        'discard': "my_set = {1, 2, 3}\nmy_set.discard(2)\nprint(my_set) # Output: {1, 3}",
        'intersection': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nprint(set1.intersection(set2)) # Output: {3, 4}",
        'intersection_update': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nset1.intersection_update(set2)\nprint(set1) # Output: {3, 4}",
        'isdisjoint': "set1 = {1, 2, 3}\nset2 = {4, 5, 6}\nprint(set1.isdisjoint(set2)) # Output: True",
        'issubset': "set1 = {1, 2}\nset2 = {1, 2, 3, 4}\nprint(set1.issubset(set2)) # Output: True",
        'issuperset': "set1 = {1, 2, 3, 4}\nset2 = {1, 2}\nprint(set1.issuperset(set2)) # Output: True",
        'pop': "my_set = {1, 2, 3}\npopped = my_set.pop()\nprint(popped, my_set) # Output: 1 {2, 3} (order may vary)",
        'remove': "my_set = {1, 2, 3}\nmy_set.remove(2)\nprint(my_set) # Output: {1, 3}",
        'symmetric_difference': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nprint(set1.symmetric_difference(set2)) # Output: {1, 2, 5, 6}",
        'symmetric_difference_update': "set1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\nset1.symmetric_difference_update(set2)\nprint(set1) # Output: {1, 2, 5, 6}",
        'union': "set1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.union(set2)) # Output: {1, 2, 3, 4, 5}",
        'union_update': "set1 = {1, 2, 3}\nset2 = {3, 4, 5}\nset1.update(set2)\nprint(set1) # Output: {1, 2, 3, 4, 5}"
    }
    return examples.get(method, "No example available for this method.")

def get_dict_example(method):
    examples = {
        'clear': "my_dict = {'a': 1, 'b': 2}\nmy_dict.clear()\nprint(my_dict) # Output: {}",
        'copy': "original = {'a': 1, 'b': 2}\ncopied = original.copy()\nprint(copied) # Output: {'a': 1, 'b': 2}",
        'get': "my_dict = {'a': 1, 'b': 2}\nprint(my_dict.get('c', 'Not found')) # Output: Not found",
        'items': "my_dict = {'a': 1, 'b': 2}\nprint(list(my_dict.items())) # Output: [('a', 1), ('b', 2)]",
        'keys': "my_dict = {'a': 1, 'b': 2}\nprint(list(my_dict.keys())) # Output: ['a', 'b']",
        'pop': "my_dict = {'a': 1, 'b': 2}\npopped = my_dict.pop('a')\nprint(popped, my_dict) # Output: 1 {'b': 2}",
        'popitem': "my_dict = {'a': 1, 'b': 2}\npopped = my_dict.popitem()\nprint(popped, my_dict) # Output: ('b', 2) {'a': 1}",
        'setdefault': "my_dict = {'a': 1}\nmy_dict.setdefault('b', 2)\nprint(my_dict) # Output: {'a': 1, 'b': 2}",
        'values': "my_dict = {'a': 1, 'b': 2}\nprint(list(my_dict.values())) # Output: [1, 2]",
        'update': "my_dict = {'a': 1}\nmy_dict.update({'b': 2, 'c': 3})\nprint(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3}"
    }
    return examples.get(method, "No example available for this method.")

def get_example(topic):
    examples = {
        'Overview of Modules in Python': "# Importing a module\nimport math\n\n# Using a function from the module\nprint(math.sqrt(16))",
        'Simple Two-Module Example': "# module1.py\ndef greet(name):\n return f'Hello, {name}!'\n\n# module2.py\nfrom module1 import greet\n\nprint(greet('Alice'))",
        'Variations on the "import" Statement': "# Different import styles\nimport math\nfrom math import sqrt\nfrom math import *\nimport math as m\nfrom math import sqrt as square_root",
        'Using the "__all__" Symbol': "# In mymodule.py\n__all__ = ['public_function']\n\ndef public_function():\n pass\n\ndef _private_function():\n pass\n\n# In main.py\nfrom mymodule import *\npublic_function() # This works\n# _private_function() # This would raise an error",
        'Public and Private Module Variables': "# In mymodule.py\npublic_var = 'This is public'\n_private_var = 'This is meant to be private'\n\n# In main.py\nimport mymodule\nprint(mymodule.public_var) # This is fine\n# print(mymodule._private_var) # This is discouraged",
        'The Main Module and "__main__"': "# script.py\ndef main():\n print('This is the main function')\n\nif __name__ == '__main__':\n main()",
        'Gotcha! Problems with Mutual Importing': "# Avoid circular imports like this:\n# module1.py\nfrom module2 import function2\n\ndef function1():\n function2()\n\n# module2.py\nfrom module1 import function1\n\ndef function2():\n function1()",
        'RPN Example: Breaking into Two Modules': "# rpn_math.py\ndef add(x, y):\n return x + y\n\ndef subtract(x, y):\n return x - y\n\n# rpn_main.py\nfrom rpn_math import add, subtract\n\ndef evaluate_rpn(expression):\n stack = []\n for token in expression.split():\n if token in ['+', '-']:\n b, a = stack.pop(), stack.pop()\n if token == '+':\n stack.append(add(a, b))\n else:\n stack.append(subtract(a, b))\n else:\n stack.append(float(token))\n return stack.pop()",
        'RPN Example: Adding I/O Directives': "# rpn_io.py\ndef get_input():\n return input('Enter RPN expression: ')\n\ndef display_result(result):\n print(f'Result: {result}')\n\n# rpn_main.py\nfrom rpn_math import evaluate_rpn\nfrom rpn_io import get_input, display_result\n\ndef main():\n expression = get_input()\n result = evaluate_rpn(expression)\n display_result(result)\n\nif __name__ == '__main__':\n main()",
        'Adding Line-Number Checking': "def check_line_numbers(code):\n lines = code.split('\\n')\n for i, line in enumerate(lines, 1):\n if line.strip().startswith(str(i)):\n print(f'Line {i} starts with its line number')\n else:\n print(f'Line {i} does not start with its line number')",
        'Adding Jump-If-Not-Zero': "def jump_if_not_zero(value, jump_to):\n if value != 0:\n return jump_to\n return None"
    }
    return examples.get(topic, "No example available for this topic.")

def get_example(topic):
    examples = {
        'Adjusting Axes with "xticks" and "yticks"': """
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xticks([0, np.pi, 2*np.pi], ['0', 'π', '2π'])
plt.yticks([-1, 0, 1])
plt.show()
""",
        '"numpy" Mixed-Data Records': """
import numpy as np

# Define a structured array
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
a = np.array([('Alice', 25, 55.0), ('Bob', 30, 70.5)], dtype=dt)

print(a['name'])  # Access the 'name' field
print(a[a['age'] > 27])  # Filter based on age
""",
        'Reading and Writing "numpy" Data from Files': """
import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Write to a file
np.save('my_array.npy', arr)

# Read from the file
loaded_arr = np.load('my_array.npy')
print(loaded_arr)
""",
        'Overview of Modules in Python': """
# Importing a module
import math

# Using a function from the module
print(math.sqrt(16))

# Importing specific functions
from random import randint
print(randint(1, 10))
""",
        'Simple Two-Module Example': """
# module1.py
def greet(name):
    return f"Hello, {name}!"

# module2.py
from module1 import greet

def main():
    print(greet("Alice"))

if __name__ == "__main__":
    main()
""",
        'Variations on the "import" Statement': """
# Different import styles
import math
from math import sqrt
from math import *
import math as m
from math import sqrt as square_root

print(math.pi)
print(sqrt(16))
print(pi)
print(m.e)
print(square_root(25))
""",
        'Using the "__all__" Symbol': """
# mymodule.py
__all__ = ['public_function']

def public_function():
    print("This is a public function")

def _private_function():
    print("This is a private function")

# main.py
from mymodule import *

public_function()  # This works
# _private_function()  # This would raise an error
""",
        'Public and Private Module Variables': """
# mymodule.py
public_var = "This is public"
_private_var = "This is meant to be private"

# main.py
import mymodule

print(mymodule.public_var)  # This is fine
# print(mymodule._private_var)  # This is discouraged
""",
        'The Main Module and "__main__"': """
# script.py
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()
""",
        'Gotcha! Problems with Mutual Importing': """
# Avoid circular imports like this:

# module1.py
from module2 import function2

def function1():
    print("Function 1")
    function2()

# module2.py
from module1 import function1

def function2():
    print("Function 2")
    function1()

# This will cause an ImportError
"""
    }
    return examples.get(topic, "No example available for this topic.")

def page_1():
    st.title("Python Code Snippets")

    statements = [
        'continue', 'def', 'del', 'elif', 'else', 'except', 'for', 'global', 'if', 'import',
        'nonlocal', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    ]

    selected_statement = st.selectbox("Choose a Python statement:", statements)

    st.code(get_code_snippet(selected_statement), language='python')

    st.write("This example demonstrates a basic usage of the selected statement.")

def page_2():
    st.title("Python Set and Dictionary Methods Examples")

    method_type = st.radio("Choose a method type:", ["Set Methods", "Dictionary Methods"])

    if method_type == "Set Methods":
        set_methods = [
            'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
            'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
            'symmetric_difference', 'symmetric_difference_update', 'union', 'union_update'
        ]
        selected_method = st.selectbox("Choose a Set method:", set_methods, key="set_method_selectbox")  # Unique key added
        st.code(get_set_example(selected_method), language='python')
    else:
        dict_methods = [
            'clear', 'copy', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'values', 'update'
        ]
        selected_method = st.selectbox("Choose a Dictionary method:", dict_methods, key="dict_method_selectbox")  # Unique key added
        st.code(get_dict_example(selected_method), language='python')

    st.write("This example demonstrates a basic usage of the selected method.")

def page_3():
    st.title("Python Built-in Functions Examples")

    functions = [
        'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list',
        'locals', 'map', 'max', 'min', 'oct', 'open', 'ord', 'pow', 'print', 'range', 'repr', 'reversed', 'round', 'set',
        'setattr', 'sorted', 'str', 'sum', 'super', 'tuple', 'type', 'zip'
    ]

    def get_example(func_name):
        examples = {
            'globals': "print(globals())",
            'hasattr': "class Person:\n name = 'John'\n\nprint(hasattr(Person, 'name'))",
            'hash': "print(hash('python'))",
            'help': "help(list)",
            'hex': "print(hex(255))",
            'id': "x = [1, 2, 3]\nprint(id(x))",
            'input': "name = input('Enter your name: ')\nprint(f'Hello, {name}!')",
            'int': "print(int('100', base=2))",
            'isinstance': "print(isinstance(5, int))",
            'issubclass': "class A: pass\nclass B(A): pass\nprint(issubclass(B, A))",
            'iter': "x = iter([1, 2, 3])\nprint(next(x))",
            'len': "print(len([1, 2, 3, 4, 5]))",
            'list': "print(list('python'))",
            'locals': "def func():\n x = 10\n print(locals())\nfunc()",
            'map': "numbers = [1, 2, 3, 4]\nprint(list(map(lambda x: x*2, numbers)))",
            'max': "print(max([1, 5, 3, 2, 4]))",
            'min': "print(min([1, 5, 3, 2, 4]))",
            'oct': "print(oct(8))",
            'open': "with open('example.txt', 'w') as f:\n f.write('Hello, World!')",
            'ord': "print(ord('A'))",
            'pow': "print(pow(2, 3))",
            'print': "print('Hello', 'World', sep='-', end='!')",
            'range': "print(list(range(0, 10, 2)))",
            'repr': "print(repr('Hello, World!'))",
            'reversed': "print(list(reversed([1, 2, 3])))",
            'round': "print(round(3.14159, 2))",
            'set': "print(set([1, 2, 2, 3, 3, 3]))",
            'setattr': "class Person: pass\nsetattr(Person, 'name', 'John')\nprint(Person.name)",
            'sorted': "print(sorted([3, 1, 4, 1, 5, 9, 2, 6, 5]))",
            'str': "print(str(123))",
            'sum': "print(sum([1, 2, 3, 4, 5]))",
            'super': "class Parent:\n def greet(self):\n print('Hello from Parent')\n\nclass Child(Parent):\n def greet(self):\n super().greet()\n print('Hello from Child')\n\nChild().greet()",
            'tuple': "print(tuple([1, 2, 3]))",
            'type': "print(type(42))",
            'zip': "x = [1, 2, 3]\ny = ['a', 'b', 'c']\nprint(list(zip(x, y)))"
        }
        return examples.get(func_name, "No example available for this function.")

    selected_function = st.selectbox("Choose a Python built-in function:", functions, key="builtin_function_selectbox")  # Unique key added
    st.code(get_example(selected_function), language='python')
    st.write("This example demonstrates a basic usage of the selected function.")

# New pages
def page_4():
    st.title("Python Built-in Functions Examples")

    functions = [
        'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytes', 'callable', 'chr', 'compile',
        'complex', 'delattr', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter',
        'float', 'format', 'frozenset', 'getattr'
    ]

    selected_function = st.selectbox("Choose a Python built-in function:", functions)

    st.code(get_example(selected_function), language='python')

    st.write("This example demonstrates a basic usage of the selected function.")

    if selected_function in ['compile', 'eval', 'exec']:
        st.warning("Note: Be cautious when using compile(), eval(), or exec() with untrusted input, as they can execute arbitrary code.")

def page_5():
    st.title("Python Module Examples")

    topics = [
        'Overview of Modules in Python',
        'Simple Two-Module Example',
        'Variations on the "import" Statement',
        'Using the "__all__" Symbol',
        'Public and Private Module Variables',
        'The Main Module and "__main__"',
        'Gotcha! Problems with Mutual Importing',
        'RPN Example: Breaking into Two Modules',
        'RPN Example: Adding I/O Directives',
        'Adding Line-Number Checking',
        'Adding Jump-If-Not-Zero'
    ]

    selected_topic = st.selectbox("Choose a Python module topic:", topics)
    st.code(get_example(selected_topic), language='python')
    st.write("This example demonstrates the selected topic related to Python modules.")


def page_6():
    st.title("Python Code Examples")

    topics = [
        'Adjusting Axes with "xticks" and "yticks"',
        '"numpy" Mixed-Data Records',
        'Reading and Writing "numpy" Data from Files',
        'Overview of Modules in Python',
        'Simple Two-Module Example',
        'Variations on the "import" Statement',
        'Using the "__all__" Symbol',
        'Public and Private Module Variables',
        'The Main Module and "__main__"',
        'Gotcha! Problems with Mutual Importing'
    ]

    selected_topic = st.selectbox("Choose a Python topic:", topics)
    st.code(get_example(selected_topic), language='python')
    st.write("This example demonstrates the selected topic.")

def page_7():
        st.title("Python Basics: Classes, Variables, Objects")

        st.header("Python Variables")
        st.write(
            "Variables in Python are used to store data values. They do not need explicit declaration to reserve memory space.")
        st.code("x = 5\ny = 'Hello, World!'")
        st.write("Python variables can store different types of data, and their type can change dynamically.")

        st.header("Python Classes and Objects")
        st.write("A class is a blueprint for creating objects (instances). An object is an instance of a class.")
        st.code("class MyClass:\n    def __init__(self, name):\n        self.name = name\n\nobj = MyClass('John')")
        st.write("In this example, `obj` is an instance of the `MyClass` class, initialized with a name 'John'.")

        st.header("Python Class Variables and Instance Variables")
        st.write(
            "Class variables are shared among all instances of a class. Instance variables are unique to each instance.")
        st.code(
            "class Car:\n    category = 'Vehicle'\n\n    def __init__(self, brand):\n        self.brand = brand\n\nbmw = Car('BMW')\ntoyota = Car('Toyota')")
        st.write("`category` is a class variable, and `brand` is an instance variable in this `Car` class example.")

        st.header("Python Methods")
        st.write(
            "Methods are functions defined inside the body of a class. They are used to perform operations with class attributes.")
        st.code(
            "class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        return 'Woof!'")
        st.write("In this `Dog` class, `bark()` is a method that returns 'Woof!' when called on an instance of `Dog`.")

        st.header("Encapsulation, Inheritance, Polymorphism")
        st.write(
            "Python supports object-oriented programming principles such as encapsulation, inheritance, and polymorphism.")
        st.write(
            "Encapsulation: Bundling of data (variables) and methods that operate on the data into a single unit (class).")
        st.write("Inheritance: Ability of a class to inherit properties and behavior from another class.")
        st.write("Polymorphism: Ability to present the same interface for different data types.")
        st.write("These concepts enhance code reusability and structure.")

        st.header("Conclusion")
        st.write(
            "Understanding classes, objects, and related concepts is fundamental to object-oriented programming in Python.")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page:", [
        "Page 1 - Code Snippets", "Page 2 - Set and Dictionary Methods", "Page 3 - Built-in Functions",
        "Page 4 - Built-in Functions Examples", "Page 5 - Python Module Examples", "Page 6 - Python Code Examples",
        "Page 7 - Python Basics"
    ])

    if page == "Page 1 - Code Snippets":
        page_1()
    elif page == "Page 2 - Set and Dictionary Methods":
        page_2()
    elif page == "Page 3 - Built-in Functions":
        page_3()
    elif page == "Page 4 - Built-in Functions Examples":
        page_4()
    elif page == "Page 5 - Python Module Examples":
        page_5()
    elif page == "Page 6 - Python Code Examples":
        page_6()
    elif page == "Page 7 - Python Basics":
        page_7()

if __name__ == "__main__":
    main()
