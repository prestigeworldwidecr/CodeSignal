'''

In this exercise, we'll focus on the Liskov Substitution Principle (LSP). The current code represents a file processing system where the File class has a method to write data. The ReadOnlyFile, which inherits from File, throws an exception when trying to write data, violating LSP.

The solution involves creating a proper hierarchy with:

A base Storage class that defines the common behavior for all storage types
A WritableStorage class that extends Storage to add write capabilities
Concrete implementations (File and ReadOnlyFile) that inherit from the appropriate base classes
The process_file function demonstrates proper polymorphic behavior by:

Reading data from any storage type
Writing data only when the storage supports write operations (using isinstance check)
This approach ensures that objects of derived classes can be substituted for objects of their base classes without breaking the application's functionality.

Let's refactor this code to properly handle different file access types

'''

from abc import ABC, abstractmethod

class ReadOnlyFileError(Exception) :
# {
    def __init__(self, message) :
    # {
        super().__init__(message)
    # }

# }

class Storage(ABC) :
# {
    @abstractmethod
    def read_data(self) :
    # {
        None
    # }

    @abstractmethod
    def write_data(self, data) :
    # {
        None
    # }

# }

class File(Storage) :
# {
    def __init__(self, name) :
    # {
        self.name = name
    # }

    def read_data(self) :
    # {
        print("Reading data from", self.name)
    # }

    def write_data(self, data) :
    # {
        print("Writing to", self.name, ':', data)
    # }

# }

class ReadOnlyFile(Storage) :
# {
    def __init__(self, name) :
    # {
        self.name = name
    # }

    def read_data(self) :
    # {
        print("Reading data from", self.name)
    # }

    def write_data(self, data) :
    # {
        raise ReadOnlyFileError("Cannot write to read-only file")
    # }

# }

def process_file(storage) :
# {    
    storage.read_data()

    if (isinstance(storage, ReadOnlyFile)) :
    # {
        print("Cannot write to read-only file")
    # }

    else :
    # {
        # print("Writing data to file")
        storage.write_data("Some data")
    # }

# }

def main() :
# {
    regular_file = File("document.txt")
    read_only_file = ReadOnlyFile("read_only.txt")

    print("Processing regular file:")
    process_file(regular_file)

    print("\nProcessing readonly file:")
    process_file(read_only_file)
# }

if (__name__ == '__main__') :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****


    try :
    # {
        storage.write_data("Some data")
    # }

    except Exception as e :
    # {
        raise ReadOnlyFileError("Cannot write to read-only file") from e
    # }


'''