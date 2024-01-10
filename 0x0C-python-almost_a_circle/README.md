# 0x0C. Python - Almost a circle

1. **Import:**
   - **Definition:** `import` is used in Python to include external modules or libraries in your code.
   - **Example:**

     ```python

     import math
     print(math.sqrt(16))
     ```

2. **Exceptions:**
   - **Definition:** Exceptions are events that occur during the execution of a program that disrupts the normal flow of the program.
   - **Example:**

     ```python

     try:
         result = 10 / 0
     except ZeroDivisionError as e:
         print(f"Error: {e}")
     ```

3. **Class:**
   - **Definition:** A class is a blueprint for creating objects, providing initial values for state and implementations of behavior (methods).
   - **Example:**

     ```python

     class Dog:
         def __init__(self, name):
             self.name = name

         def bark(self):
             print(f"{self.name} says Woof!")

     my_dog = Dog("Buddy")
     my_dog.bark()
     ```

4. **Private Attribute:**
   - **Definition:** Private attributes are attributes that are not accessible directly from outside the class.
   - **Example:**

     ```python
     class Car:
         def __init__(self):
             self.__speed = 0

     my_car = Car()
     # This will result in an error
     # print(my_car.__speed)
     ```

5. **Getter/Setter:**
   - **Definition:** Getter and setter methods are used to control access to the attributes of a class.
   - **Example:**

     ```python
     class Circle:
         def __init__(self, radius):
             self.__radius = radius

         def get_radius(self):
             return self.__radius

         def set_radius(self, radius):
             if radius > 0:
                 self.__radius = radius

     my_circle = Circle(5)
     print(my_circle.get_radius())
     my_circle.set_radius(8)
     ```

6. **Class Method:**
   - **Definition:** A class method is a method that is bound to the class and not the instance of the class.
   - **Example:**

     ```python
     class MyClass:
         @classmethod
         def class_method(cls):
             print("This is a class method.")

     MyClass.class_method()
     ```

7. **Static Method:**
   - **Definition:** A static method is a method that is bound to the class and not the instance, and doesn't have access to the instance or class.
   - **Example:**

     ```python
     class MathOperations:
         @staticmethod
         def add(x, y):
             return x + y

     result = MathOperations.add(3, 5)
     ```

8. **Inheritance:**
   - **Definition:** Inheritance is a way to create a new class using the properties and methods of an existing class.
   - **Example:**

     ```python
     class Animal:
         def speak(self):
             pass

     class Dog(Animal):
         def speak(self):
             print("Woof!")

     my_dog = Dog()
     my_dog.speak()
     ```

9. **Unittest:**
   - **Definition:** `unittest` is a built-in Python module for writing and running tests.
   - **Example:**

     ```python
     import unittest

     def add(x, y):
         return x + y

     class TestAddFunction(unittest.TestCase):
         def test_add(self):
             self.assertEqual(add(3, 5), 8)

     if __name__ == '__main__':
         unittest.main()
     ```

10. **Read/Write File:**
    - **Definition:** Reading and writing files is a common operation in Python to interact with external data.
    - **Example:**

      ```python
      # Writing to a file
      with open('example.txt', 'w') as file:
          file.write("Hello, world!")

      # Reading from a file
      with open('example.txt', 'r') as file:
          content = file.read()
          print(content)
      ```

11. **args and kwargs:**
    - **Definition:** `*args` and `**kwargs` allow a function to accept any number of positional and keyword arguments, respectively.
    - **Example:**

      ```python
      def example_function(*args, **kwargs):
          print(args)
          print(kwargs)

      example_function(1, 2, 3, name='John', age=25)
      ```

12. **Serialization/Deserialization:**
    - **Definition:** Serialization is the process of converting an object into a format that can be easily stored or transmitted, and deserialization is the reverse process.
    - **Example:**

      ```python
      import pickle

      data = {'name': 'Alice', 'age': 30}

      # Serialization
      serialized_data = pickle.dumps(data)

      # Deserialization
      deserialized_data = pickle.loads(serialized_data)
      ```

13. **JSON:**
    - **Definition:** JSON (JavaScript Object Notation) is a lightweight data interchange format.
    - **Example:**

      ```python
      import json

      data = {'name': 'Bob', 'age': 28}

      # Serialization to JSON
      json_data = json.dumps(data)

      # Deserialization from JSON
      deserialized_data = json.loads(json_data)
      ```
