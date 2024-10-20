# Implementing the Abstract Factory in Python

### Step 0: Create Factory Interface

In this step, we create the abstract factory interface `NotificationFactory`. This interface serves as a blueprint for
all concrete factory classes. It defines three essential abstract methods:

- `create_email_notification()`: Creates an email notification object.
- `create_sms_notification()`: Creates an SMS notification object.
- `create_push_notification()`: Creates a push notification object.

Below is the code for the abstract factory interface:

```python
from abc import ABC, abstractmethod


# 0. Abstract Factory Interface
class NotificationFactory(ABC):
    """Abstract Factory Interface"""

    @abstractmethod
    def create_email_notification(self):
        pass

    @abstractmethod
    def create_sms_notification(self):
        pass

    @abstractmethod
    def create_push_notification(self):
        pass
```

This interface enforces a consistent structure for factories, ensuring that they can create various types of
notifications, whether it’s for email, SMS, or push notifications. Concrete factories, such as FastNotifFactory and
SendBlueFactory, must implement these methods to fulfill the contract defined by the NotificationFactory interface.

### Step 1: Define Concrete Factory Classes

In this step, we define the factory classes responsible for creating different types of notification objects. In our
example, we have two concrete factories: `FastNotifFactory` and `SendBlueFactory`. Each factory is responsible for
creating a family of related notification objects for a specific provider.

Below is the code for the concrete factory classes:

```python
# 1. Concrete Factories
class FastNotifFactory(NotificationFactory):
    """Concrete Factory for FastNotif"""

    def create_email_notification(self):
        return FastNotifEmailNotification()

    def create_sms_notification(self):
        return FastNotifSMSNotification()

    def create_push_notification(self):
        return FastNotifPushNotification()


class SendBlueFactory(NotificationFactory):
    """Concrete Factory for SendBlue"""

    def create_email_notification(self):
        return SendBlueEmailNotification()

    def create_sms_notification(self):
        return SendBlueSMSNotification()

    def create_push_notification(self):
        return SendBluePushNotification()

```

Step 2: Define Abstract Product Classes
Next, we define the abstract product classes, which serve as interfaces for different types of notification objects.
These abstract classes declare the methods that concrete product classes must implement. In our example, we have three
abstract product classes: AbstractEmailNotification, AbstractSMSNotification, and AbstractPushNotification.



### Step 2: Define Abstract Product Classes

Next, we define the abstract product classes, which serve as interfaces for different types of notification objects. These abstract classes declare the methods that concrete product classes must implement. In our example, we have three abstract product classes: `AbstractEmailNotification`, `AbstractSMSNotification`, and `AbstractPushNotification`.

Below is the code for the abstract product classes:

```python
# 2. Abstract Products
class AbstractEmailNotification(ABC):
    """Abstract Product for Email Notifications"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass

class AbstractSMSNotification(ABC):
    """Abstract Product for SMS Notifications"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def encode_message(self):
        pass

class AbstractPushNotification(ABC):
    """Abstract Product for Push Notifications"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_payload(self):
        pass
```



### Step 3: Define Concrete Product Classes

In this step, we define concrete product classes that implement the methods declared in the abstract product classes. These classes represent the actual notification objects. In our example, we have concrete product classes for both `FastNotif` and `SendBlue` providers, covering email, SMS, and push notifications.

### Concrete Product Classes that `FastNotifFactory` Creates:

```python
# 3. Concrete Products
class FastNotifEmailNotification(AbstractEmailNotification):
    """Concrete Product for Email Notifications via FastNotif"""

    def send(self):
        print("Sending Email via FastNotif")

    def format_content(self):
        print("Formatting Email content")

class FastNotifSMSNotification(AbstractSMSNotification):
    """Concrete Product for SMS Notifications via FastNotif"""

    def send(self):
        print("Sending SMS via FastNotif")

    def encode_message(self):
        print("Encoding SMS message")

class FastNotifPushNotification(AbstractPushNotification):
    """Concrete Product for Push Notifications via FastNotif"""

    def send(self):
        print("Sending Push Notification via FastNotif")

    def format_payload(self):
        print("Formatting Push Notification payload")
```

Concrete Product Classes that SendBlueFactory Creates:

```python


class SendBlueEmailNotification(AbstractEmailNotification):
    """Concrete Product for Email Notifications via SendBlue"""

    def send(self):
        print("Sending Email via SendBlue")

    def format_content(self):
        print("Formatting Email content")

class SendBlueSMSNotification(AbstractSMSNotification):
    """Concrete Product for SMS Notifications via SendBlue"""

    def send(self):
        print("Sending SMS via SendBlue")

    def encode_message(self):
        print("Encoding SMS message")

class SendBluePushNotification(AbstractPushNotification):
    """Concrete Product for Push Notifications via SendBlue"""

    def send(self):
        print("Sending Push Notification via SendBlue")

    def format_payload(self):
        print("Formatting Push Notification payload")

```

### Step 4: Create Factory Mapping Dictionary

In this step, we create a dictionary (`factory_mapping`) that maps provider names (e.g., `"FastNotif"` or `"SendBlue"`) to their respective factory classes. This mapping allows us to dynamically select the factory based on the provider's name.

Below is the code for the factory mapping dictionary:

```python
# Dictionary to map provider names to factory classes
factory_mapping = {
    "FastNotif": FastNotifFactory(),
    "SendBlue": SendBlueFactory(),
}
```


### Step 5: Select Notification Factory

In this step, we define the `select_notification_factory` function, which takes the provider name as input and returns the corresponding factory object from the `factory_mapping` dictionary. If the provided provider name is not found in the dictionary, a `ValueError` is raised to indicate an invalid provider.

Below is the code for the function:

```python
# Main Function to select Notification Factory
def select_notification_factory(provider):
    """Select and return the Notification Factory based on the provider"""
    factory = factory_mapping.get(provider)
    if factory is None:
        raise ValueError("Invalid provider")
    return factory
```

### Step 6: Example Usage

In this step, we demonstrate how to use the `select_notification_factory` function in a complete example. The user is prompted to input a provider (e.g., `"FastNotif"` or `"SendBlue"`), and based on the selection, the corresponding factory is used to create and send notifications.

### Example Code:

```python
# Example Usage
def send_notification(factory):
    """Create and send notifications using the selected factory"""
    email_notification = factory.create_email_notification()
    sms_notification = factory.create_sms_notification()
    push_notification = factory.create_push_notification()

    # Sending notifications
    email_notification.send()
    sms_notification.send()
    push_notification.send()

if __name__ == "__main__":
    provider = input("Enter the provider (FastNotif or SendBlue): ")
    try:
        notification_factory = select_notification_factory(provider)
        send_notification(notification_factory)
    except ValueError as e:
        print(e)
```