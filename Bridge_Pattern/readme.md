# Abstraction and Implementation

In the context of the **Bridge Design Pattern**, the terms **Abstraction** and **Implementation** refer to fundamental concepts that facilitate the separation of concerns and promote code maintainability.

- **Abstraction** serves as the high-level control layer, delegating work to the **Implementation** layer.  
  For example, a graphical user interface (GUI) interacts with the underlying operating system code (API).
- **Implementation**, or the platform, contains platform-specific code and is declared through a common interface.  
  This allows interchangeable implementations to be linked to the abstraction object.

By splitting classes into **Abstraction** and **Implementation** hierarchies, the **Bridge Pattern** simplifies code maintenance and promotes flexibility.

For instance:
- GUI changes won’t affect API-related classes.
- Adding support for new operating systems in the API requires minimal modifications.

---

## Terminology and Key Components

Here are the fundamental components involved in the Bridge Design Pattern:

1. **Abstraction**  
   Provides high-level control logic and relies on the implementation object for low-level work.

2. **Implementation**  
   Declares the interface common to all concrete implementations, allowing communication with the abstraction through declared methods.

3. **Concrete Implementations**  
   Contain platform-specific code and provide implementations for the methods declared in the implementation interface.

4. **Refined Abstractions**  
   Variants of control logic that work with different implementations via the general implementation interface.

5. **Client**  
   Primarily interacts with the abstraction and is responsible for linking the abstraction object with one of the implementation objects.

---

Understanding how these components interact is crucial for effectively utilizing the **Bridge Pattern** in software design.



# Practical Example: File Storage

## Step 1: Define Abstraction
Define an abstract class representing the file storage abstraction. This class will declare methods for saving files.

```python
from abc import ABC, abstractmethod

# Step 1: Define Abstraction (Abstract class)
class FileStorage(ABC):
    """Abstract class representing the file storage abstraction."""
    
    @abstractmethod
    def save_file(self, file_name):
        """Abstract method to save a file."""
        pass
```

## Step 2: Define Implementation
Define an abstract class representing the storage implementation. This class will declare methods for saving files specific to each storage location.

```python
# Step 2: Define Implementation (Abstract class)
from abc import ABC, abstractmethod

class StorageImplementation(ABC):
    """Abstract class representing the storage implementation."""
    
    @abstractmethod
    def save(self, file_name):
        """Abstract method to save a file."""
        pass
```

## Step 3: Create Concrete Implementations
Implement concrete classes for local storage, cloud storage, and network storage. Each class will provide a specific implementation for saving files.

```python
# Step 3: Create Concrete Implementations
class LocalStorage(StorageImplementation):
    """Concrete implementation for local file storage."""
    
    def save(self, file_name):
        """Save a file locally."""
        return f"File '{file_name}' saved locally"

class CloudStorage(StorageImplementation):
    """Concrete implementation for cloud file storage."""
    
    def save(self, file_name):
        """Save a file to the cloud."""
        return f"File '{file_name}' saved to the cloud"

class NetworkStorage(StorageImplementation):
    """Concrete implementation for network file storage."""
    
    def save(self, file_name):
        """Save a file to a network location."""
        return f"File '{file_name}' saved to a network location"
```

## Step 4: Create Refined Abstractions
Create a refined abstraction class that extends the file storage abstraction. This class will delegate file storage operations to the appropriate storage implementation based on runtime configurations.

```python
# Step 4: Create Refined Abstraction
class AdvancedFileStorage(FileStorage):
    """Refined abstraction for advanced file storage."""
    
    def __init__(self, storage_impl):
        """Initialize with a specific storage implementation."""
        self._storage_impl = storage_impl
    
    def save_file(self, file_name):
        """Save a file using the specified storage implementation."""
        return self._storage_impl.save(file_name)
```


## Step 5: Main Client Code
Demonstrate the usage of the file storage system using the refined abstractions and concrete implementations.

```python
# Step 5: Main Client Code
if __name__ == "__main__":
    # Create concrete implementations
    local_storage = LocalStorage()
    cloud_storage = CloudStorage()
    network_storage = NetworkStorage()

    # Create refined abstractions and link them with concrete implementations
    advanced_local_storage = AdvancedFileStorage(local_storage)
    advanced_cloud_storage = AdvancedFileStorage(cloud_storage)
    advanced_network_storage = AdvancedFileStorage(network_storage)

    # Use refined abstractions to save files
    print(advanced_local_storage.save_file("example.txt"))    # Output: File 'example.txt' saved locally
    print(advanced_cloud_storage.save_file("example.txt"))    # Output: File 'example.txt' saved to the cloud
    print(advanced_network_storage.save_file("example.txt"))  # Output: File 'example.txt' saved to a network location
```