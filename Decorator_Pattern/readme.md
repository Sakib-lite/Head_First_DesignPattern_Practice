# Understanding the Decorator Pattern

The **Decorator design pattern** is a structural pattern that adds behavior to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.

In other words, it enables you to "decorate" or enhance objects by adding new functionalities without modifying their structure.

This pattern is handy when you want to extend the capabilities of objects in a flexible and reusable way.

## When to Use the Decorator Pattern

- **Add Responsibilities Dynamically**: When you want to add behavior or features to objects dynamically at runtime without modifying their code.
- **Avoid a Complex Inheritance Hierarchy**: To avoid creating a deep and complex class hierarchy through subclassing, which can be challenging to maintain.

# Practical Example: Game Character Abilities

Consider a scenario in game design where different characters possess a unique set of abilities. As the game evolves, we need to add new abilities.

We’ll use game character abilities, such as the `DoubleDamageDecorator`, `FireballDecorator`, and `InvisibilityDecorator`, as examples. Characters can have different combinations of these abilities at any given moment.

Handling all subclass combinations with inheritance leads to complex code. The **Decorator Pattern** simplifies this by allowing abilities to be added to characters dynamically, keeping the code clean and flexible.

# Key Components of the Decorator Pattern

The **Decorator pattern** lets you add behavior to objects without affecting others. To implement it correctly, you need to understand its essential components:

- **Component**:  
  The base interface or abstract class that both concrete components and decorators share. It defines the core functions that can be extended.

- **Concrete Component**:  
  The basic objects to which extra behaviors are added. Decorators wrap around these components.

- **Decorator**:  
  An abstract class that adheres to the Component interface. It holds a reference to a Component and allows specific functions to be added to the core.

- **Concrete Decorator**:  
  Classes that extend the Decorator abstract class, implementing specific behaviors. These decorators can be stacked to create chains, allowing multiple functionalities to be applied dynamically.


# Step 1: Component

The **Component** is the base interface that defines the core behavior that can be enhanced. In our example, it represents the game character with a basic attack method.

```python
from abc import ABC, abstractmethod

# Step 1: Component - The base game character
class Character(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass
```
# Step 2: Concrete Component

**Concrete Components** are the basic game characters to which we can add special abilities. In this step, we create the basic character class.

```python
# Step 2: Concrete Component - Basic game character
class BasicCharacter(Character):
    def get_description(self):
        return "Basic Character"

    def get_damage(self):
        return 10
```


Step 3: Decorator
The Decorator is an abstract class that also implements the Component interface. It has a reference to a Component object and adds its specific behavior to the component’s core. In this step, we create the abstract decorator class.

# Step 3: Decorator - Abstract decorator class

```python
class CharacterDecorator(Character, ABC):
    def __init__(self, character):
        self._character = character

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass
```

# Step 4: Concrete Decorator

**Concrete Decorators** are classes that extend the Decorator abstract class, implementing specific behaviors. In this step, we create concrete decorator classes for special character abilities, such as Double Damage.

```python
# Step 4: Concrete Decorator
class DoubleDamageDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Double Damage"

    def get_damage(self):
        return self._character.get_damage() * 2

class FireballDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Fireball"

    def get_damage(self):
        return self._character.get_damage() + 20

class InvisibilityDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Invisibility"

    def get_damage(self):
        return self._character.get_damage()
```

# Step 5: Client Code

The **Client** is responsible for creating and configuring the decorators and using them with the core character. In this step, we demonstrate how to create a character with various abilities.

```python
# Step 5: Client Code - Creating a character with abilities

if __name__ == "__main__":
    character = BasicCharacter()
    print(character.get_description())  # Output: "Basic Character"
    print(character.get_damage())       # Output: 10

    # Create different decorators
    double_damage_decorator = DoubleDamageDecorator(character)
    fireball_decorator = FireballDecorator(character)
    invisibility_decorator = InvisibilityDecorator(character)

    # Apply decorators individually
    print(double_damage_decorator.get_description())  # Output: "Basic Character with Double Damage"
    print(double_damage_decorator.get_damage())       # Output: 20

    print(fireball_decorator.get_description())  # Output: "Basic Character with Fireball"
    print(fireball_decorator.get_damage())       # Output: 30

    print(invisibility_decorator.get_description())  # Output: "Basic Character with Invisibility"
    print(invisibility_decorator.get_damage())       # Output: 10

    # Combine decorators
    double_fireball_character = DoubleDamageDecorator(FireballDecorator(character))
    print(double_fireball_character.get_description())  # Output: "Basic Character with Double Damage with Fireball"
    print(double_fireball_character.get_damage())       # Output: 60

    invisibility_double_fireball_character = InvisibilityDecorator(double_fireball_character)
    print(invisibility_double_fireball_character.get_description())  # Output: "Basic Character with Invisibility with Double Damage with Fireball"
    print(invisibility_double_fireball_character.get_damage())       # Output: 60
```
