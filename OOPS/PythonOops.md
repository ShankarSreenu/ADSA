

## Python OOPS:
  
### OOPS
- An object-oriented paradigm is to design the program using classes and objects

### Why OOPS?
- 

### class:
- A class is a user-defined blueprint ,template or prototype from which objects are created.

### Object:
- Object is an instance of class 
- object has state and behaviour i.e attrib,methods

### __init__:
- The __init__ method is similar to constructors 
- This method lets the class initialize the object's attributes 

#### __self__:
- self parameter is a reference to the current instance of the class
  
### Inheritance:
- Inheritance is the capability of one class to derive or inherit the properties from another class.
### Types:
#### Single inheritance: 
  - When a child class inherits from only one parent class
#### Multiple inheritance:
  - When a child class inherits from more than one parent class
  ``` python
  #Multiple Inheritance

      class X:
          def __init__(self,x):
              self.x=x

      class Y:
          def __init__(self,y):
              self.y=y

      class Box(X,Y):
          def __init__(self,x,y):
              X.__init__(self,x)
              Y.__init__(self,y)

          def area(self):
              print(self.x*self.y)

      Box(4,3).area()

  ```
#### Multilevel inheritance:
  - When we have a child and grandchild relationship
#### Hierarchical inheritance:
  - More than one derived class are created from a single base.
  ``` python
    #Hierarchical inheritance

    class Card:
        def __init__(self,cardno):
            self.cardno=cardno
    class Debit(Card):
        def __init__(self,cardno):
            Card.__init__(self,cardno)
            self.name=None

        def show(self):
            print('Debit card')

    class Credit(Card):
        def __init__(self,cardno):
            Card.__init__(self,cardno)

        def show(self):
            print('Credit card')

    obj1=Debit(5000)
    obj2=Credit(5001)
    obj1.show()
    obj2.show()
    print(obj1.cardno,obj2.cardno)

  ```
#### Hybrid Inheritance:
  - When combines more than one form of inheritance.


#### uses:
   - Code reuseblity.
   - Can represent relationships between classes
   - we can add new methods and attributes to new child class along with inheriting parent class properties.
  

### Encapsulation
   - It describes the idea of wrapping data and the methods that work on data within one unit
  
  #### Protected Members
  - Protected members  are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses.
  - presented by underscore '_'.
  #### Private Members
  - Declared private should neither be accessed outside the class nor by any child class
  ``` python
    class Bank:
      def __init__(self):
          self.__Accno ='580' # private
      def returnDetails(self):
          print('showing unrestricted details')

    class client:
      def __init__(self):
          Bank.__init__(self)
          self._name='xyz' #potected
      def returnDetails(self):
          print(self.name)

  ```
  #### uses:
  -  This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
  - To prevent accidental change, an object’s variable can only be changed by an object’s method


### Polymorphism:
 - polymorphism means the same function name (but different signatures) being used for different types
 - 
  
  #### Method overloading
  - In which we can have two or more methods (functions) that have the same name but the parameters that they   take as input values are different
  - python dosent support method overloading as other classes.

  #### Method overriding
  ```python
    # method overriding
    class Parent:
        def method(self):
            print("Iam inside Parent")

    class child:
        def method(self):
            print("Inside child")

    c=child()
    c.method()
  ```

### Abstraction
- A class that consists of one or more abstract method is called the abstract class.
- A abstract class donot contain their implementation.
- Abstraction classes are meant to be the blueprint of the other class.
- An abstract class is also helpful to provide the standard interface for different implementations 
  of components
- We cannot create instances from abstract class.
  

``` python
  # method overriding
  from abc import ABC, abstractmethod
  class Employee(ABC):
      def __init__(self, first_name, last_name):
          self.first_name = first_name
          self.last_name = last_name

      @property
      def full_name(self):
          return f"{self.first_name} {self.last_name}"

      @abstractmethod
      def get_salary(self):
          pass
      

  class FulltimeEmployee(Employee):
      def __init__(self, first_name, last_name, salary):
          super().__init__(first_name, last_name)
          self.salary = salary

      def get_salary(self):
          return self.salary

  class HourlyEmployee(Employee):
      def __init__(self, first_name, last_name, worked_hours, rate):
          super().__init__(first_name, last_name)
          self.worked_hours = worked_hours
          self.rate = rate

      def get_salary(self):
          return self.worked_hours * self.rate


```
