# Object Adapter Pattern

The **Object Adapter Pattern** is a structural design pattern that enables incompatible interfaces to work together. It uses composition to adapt one class to another, allowing the client class to interact with an interface it normally wouldn’t support.

## Key Concepts

- **Adapter**: The adapter object acts as a bridge, translating requests from the client to a format understood by the adaptee.
- **Adaptee**: The existing class with an interface that’s incompatible with the client’s expected interface.
- **Client**: The class that uses the target interface and interacts with the adapter.

## How It Works

In the Object Adapter Pattern, the adapter contains an instance of the adaptee class and delegates calls to this instance. This approach enables adapting the adaptee's interface without modifying its structure.

## Example

Imagine a program that works with a `MediaPlayer` interface, which only supports playing MP3 files. To add support for other formats (like MP4 and VLC) without modifying the original `MediaPlayer` class, we use an **Object Adapter** to make the necessary conversions.

### Explanation

- **MediaPlayer**: The target interface, which the client expects.
- **Mp4Player** and **VlcPlayer**: Adaptees, which are existing classes with incompatible interfaces.
- **MediaAdapter**: The adapter class that makes `Mp4Player` and `VlcPlayer` compatible with `MediaPlayer` by containing instances of these classes and delegating method calls.
- **AudioPlayer**: The client that interacts with `MediaAdapter` to play various media formats.

## Benefits of the Object Adapter Pattern

- **Flexibility**: Allows an object to be adapted without modifying its source code.
- **Composition Over Inheritance**: The Object Adapter Pattern promotes composition over inheritance, making the adapter more flexible.

Using the Object Adapter Pattern here allows the `AudioPlayer` to handle new file formats seamlessly by integrating the `MediaAdapter`, which bridges between the incompatible interfaces.



*******
*******
*******
*******
*******


# Class Adapter Pattern

The **Class Adapter Pattern** is a structural design pattern that enables incompatible interfaces to work together by using inheritance to adapt one class to another. Unlike the **Object Adapter Pattern** (which uses composition), the Class Adapter Pattern directly extends both the target interface and adaptee class, combining their behaviors.

## Key Concepts

- **Adapter**: Inherits from both the target interface and the adaptee class to directly bridge their interfaces.
- **Adaptee**: The existing class with an interface that is incompatible with the target interface.
- **Client**: The class that uses the target interface and interacts with the adapter.

## How It Works

The Class Adapter Pattern works by inheriting the adaptee’s methods and directly implementing the target interface’s methods. This approach is possible in languages that support multiple inheritance (like C++ or Python), allowing a single class to inherit from both the target interface and the adaptee class.

## Example

Imagine we have a `MediaPlayer` interface for an audio player that only supports playing MP3 files. We also have classes to handle other file formats like MP4 and VLC. The **Class Adapter Pattern** allows us to adapt these additional formats to the `MediaPlayer` interface by inheriting from both `MediaPlayer` and the incompatible media player classes (`Mp4Player` and `VlcPlayer`).

### Explanation

- **MediaPlayer**: The target interface expected by the client.
- **Mp4Player** and **VlcPlayer**: Adaptees with interfaces incompatible with `MediaPlayer`.
- **Mp4Adapter** and **VlcAdapter**: Adapter classes that inherit from both `MediaPlayer` and their respective adaptee classes. Each adapter:
  - Inherits the target `MediaPlayer` interface.
  - Inherits the adaptee methods (e.g., `play_mp4` in `Mp4Player`).
  - Adapts `play()` to call the appropriate method in the adaptee.
- **AudioPlayer**: The client class that uses adapters to play various media types.

## Benefits of the Class Adapter Pattern

- **Direct Access**: Since the adapter directly inherits from the adaptee, it can override or extend adaptee behavior easily.
- **Better Performance**: Reduces the need for delegating calls since the adapter has direct access to the adaptee's methods.

### Limitations

- **Multiple Inheritance**: Limited to languages that support multiple inheritance (like Python and C++).
- **Rigid Design**: Less flexible than the Object Adapter Pattern, as the adapter is tightly coupled with the adaptee.

In this example, `AudioPlayer` can now handle multiple media formats by using specific adapters that bridge the gap between the client’s expected interface (`MediaPlayer`) and the formats available through `Mp4Player` and `VlcPlayer`.


******

# Class Adapter Pattern vs Object Adapter Pattern

| Feature                        | **Class Adapter Pattern**                             | **Object Adapter Pattern**                          |
|---------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| **Inheritance**                 | Uses inheritance to adapt one class to another.      | Uses composition to adapt one class to another.     |
| **Adapter Type**                | The adapter directly inherits from both the target interface and adaptee class. | The adapter contains an instance of the adaptee class and delegates calls. |
| **Flexibility**                 | Less flexible, as the adapter is tightly coupled with the adaptee. | More flexible, as it uses composition over inheritance. |
| **Language Dependency**         | Limited to languages that support multiple inheritance (like C++ or Python). | Works in all languages regardless of inheritance model. |
| **Access to Adaptee Methods**   | Direct access to the adaptee methods, making it easier to override or extend behavior. | Requires delegating calls to the adaptee, which can add overhead. |
| **Performance**                 | Better performance due to direct inheritance and method overriding. | May have lower performance due to delegation. |
| **Design Complexity**           | More rigid design due to inheritance.                | More flexible and modular design due to composition. |
