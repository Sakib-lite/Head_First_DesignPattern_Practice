## Step 1: Define the Product (FormField)

### Class: `FormField`

This class represents a form field with attributes for:

- `label`: the label for the field.
- `input_type`: the type of input for the field (e.g., text, password, etc.).

#### Methods:

- `__init__(self, label, input_type)`: Initializes the `FormField` object with a label and an input type.
- `__str__(self)`: Returns a string that represents the form field in HTML format.

When an instance of `FormField` is printed, it will return an HTML string representing the form field in the format:

```python

class FormField:
    def __init__(self, label, input_type):
        self.label = label
        self.input_type = input_type

    def __str__(self):
        return f"{self.label}: <input type='{self.input_type}'>"
```


## Step 2: Define the Builder (Abstract Builder)

### Class: `Builder` (Abstract Base Class)

This is an abstract base class (ABC) that defines the blueprint for constructing forms. It outlines the structure for form creation using multiple methods, but leaves their implementation to the concrete subclasses.

#### Methods (Abstract):

- `add_name_field(self)`: Adds a name input field to the form. This method must be implemented in subclasses.
- `add_email_field(self)`: Adds an email input field to the form. This method must be implemented in subclasses.
- `add_subscribe_field(self)`: Adds a subscribe checkbox field to the form. This method must be implemented in subclasses.
- `build(self)`: Builds and returns the final form. This method must be implemented in subclasses.

The `abstractmethod` decorator ensures that these methods must be implemented by any subclass that inherits from the `Builder` class.

### Python Code:

```python
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def add_name_field(self):
        pass

    @abstractmethod
    def add_email_field(self):
        pass

    @abstractmethod
    def add_subscribe_field(self):
        pass

    @abstractmethod
    def build(self):
        pass
```


## Step 3: Implement the Concrete Builder (FormBuilder)

### Class: `FormBuilder`

This is a concrete implementation of the `Builder` class. It maintains an internal list, `self.form`, which stores the form fields as they are added. It implements all the abstract methods defined in the `Builder` class.

#### Methods:

- `__init__(self)`: Initializes the `FormBuilder` with an empty list to store form fields.
- `add_name_field(self)`: Adds a text input for "Name" to the form.
- `add_email_field(self)`: Adds an email input for "Email" to the form.
- `add_subscribe_field(self)`: Adds a checkbox for "Subscribe" to the form.
- `build(self)`: Combines all form fields into a final HTML form and returns it as a string.

When the `build` method is called, it returns the form in the following HTML format:



```python

class FormBuilder(Builder):
    def __init__(self):
        self.form = []

    def add_name_field(self):
        self.form.append(FormField("Name", "text"))
        return self

    def add_email_field(self):
        self.form.append(FormField("Email", "email"))
        return self

    def add_subscribe_field(self):
        self.form.append(FormField("Subscribe", "checkbox"))
        return self

    def build(self):
        form = "\n".join(str(field) for field in self.form)
        return f"<form>\n{form}\n</form>"


```


## Step 4: Implement the Director (FormBuilderDirector)

### Class: `FormBuilderDirector`

This class acts as the Director in the Builder pattern. It orchestrates the construction of a form using a given `Builder` instance. The `FormBuilderDirector` is responsible for coordinating the order in which form fields are added.

#### Methods:

- `__init__(self, builder)`: Initializes the `FormBuilderDirector` with an instance of a builder (e.g., `FormBuilder`).
- `construct_form(self)`: Sequentially calls the builder's methods to add the fields:
  - Adds a name field.
  - Adds an email field.
  - Adds a subscribe checkbox.

This ensures that the form is constructed in a step-by-step manner, delegating the actual field construction to the builder.

### Python Code:

```python
class FormBuilderDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_form(self):
        self.builder.add_name_field().add_email_field().add_subscribe_field()
```