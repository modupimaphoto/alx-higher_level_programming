# 0x0A. Python - Inheritance

### 1. What is a superclass, base class, or parent class:

A superclass, base class, or parent class is a class that is extended or inherited by another class, called the subclass. It provides a blueprint for common attributes and methods that the subclass can use.

### 2. What is a subclass:

A subclass is a class that inherits attributes and methods from a superclass or base class. It can also have its own additional attributes and methods.

### 3. How to list all attributes and methods of a class or instance:

You can use the dir() function to get a list of attributes and methods of a class or instance.

### 4. When can an instance have new attributes:

An instance can have new attributes at any time by assigning values to new attribute names. Python is dynamically typed, allowing you to add attributes to instances on the fly.

### 5. What is the default class every class inherits from:

The default class that every class inherits from in Python is object.

### 6. How to override a method or attribute inherited from the base class:

Simply define a method or attribute with the same name in the subclass. This overrides the inherited method or attribute.

### 7. Which attributes or methods are available by heritage to subclasses:

Subclasses have access to all public attributes and methods of their superclass. Private attributes (those starting with a double underscore __) are not directly accessible in the subclass.

### 8. What is the purpose of inheritance:

Inheritance promotes code reusability, as it allows you to create a new class by building upon an existing class. It helps in organizing and structuring code.

### 9. What are, when and how to use isinstance, issubclass, type, and super built-in functions:

- `isinstance(obj, class_or_tuple)`: Checks if an object is an instance of a class or a tuple of classes.
- `issubclass(class, classinfo)`: Checks if a class is a subclass of another class or a tuple of classes.
- `type(obj)`: Returns the type of an object.
- `super()`: Returns a temporary object of the superclass, allowing you to call its methods.
