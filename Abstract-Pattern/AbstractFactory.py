from abc import ABC, abstractmethod


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


factory_mapping = {
    "FastNotif": FastNotifFactory(),
    "SendBlue": SendBlueFactory(),
}


def select_notification_factory(provider):
    """Select and return the Notification Factory based on the provider"""
    factory = factory_mapping.get(provider)
    if factory is None:
        raise ValueError("Invalid provider")
    return factory


def send_notification(factory):
    """Create and send notifications using the selected factory"""
    email_notification = factory.create_email_notification()
    sms_notification = factory.create_sms_notification()
    push_notification = factory.create_push_notification()

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
