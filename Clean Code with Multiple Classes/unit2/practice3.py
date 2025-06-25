'''

In this task, we'll harness the power of encapsulation and abstraction in Python by creating a practical exercise with abstract classes.

Your mission is to refactor the code, which currently relies heavily on specific implementations, into a more flexible structure utilizing an abstract class. The abstract class should encapsulate the sequence of commands open, process, and close within a concrete method. This approach will allow you to centralize common functionality and ensure that specific details are left to the implementing classes.

The current code processes different types of documents but is difficult to extend or maintain. Let's make it more maintainable and future-ready!

Good effort, but you missed one key part: the abstract class should have a method that runs open, process, and close in sequence, so you only call one method from the main block.

Want to give it another shot? Let me know if you need a hint!

How could you create a single method in your abstract class that calls open(), process(), and close() in order, so that subclasses only need to implement the specific process() logic?
Try sketching out what that method might look like in your abstract class!

Good effort, but your solution doesn't let each document type provide its own processing logic. The abstract class should require subclasses to implement their own process method.

Want to try making process abstract and customizing it in each subclass? Let me know if you need a hint!


In your abstract base class, define a method (e.g., process_document) that calls self.open(), self.process(), and self.close() in that order.

Use @abstractmethod to mark process as abstract, so each subclass must implement it.
Subclasses should only override process, not open or close.
Try writing just the abstract base class with this structure!

'''

from abc import ABC, abstractmethod

class Document(ABC) :
# {
    @abstractmethod
    def process(self) :
    # {
        # self.open()
        # self.process() 
        # self.close()
        None
    # }

    def process_document(self) :
    # {
        self.open()
        self.process()
        self.close()
    # }

    def open(self) :
    # {
        print("Opening document")
    # }

    def close(self) :
    # {
        print("Closing document")
    # }


# }

class TextDocument(Document) :
# {
    def process(self) :
    # {
        # print("Opening text document")
        print("Processing text document")
        # print("Closing text document")
    # }
         
# }

class SpreadsheetDocument(Document) :
# {
    def process(self) :
    # {
        # print("Opening spreadsheet document")
        print("Processing spreadsheet document")
        # print("Closing spreadsheet document")  
    # }

# }

if (__name__ == "__main__"):
# {
    text_document = TextDocument()
    spreadsheet_document = SpreadsheetDocument()
    text_document.process_document()
    spreadsheet_document.process_document()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

# TextDocument().process()
    # SpreadsheetDocument().process()
    # spreadsheet_document = SpreadsheetDocument()
    # document = Document()
    # document = Document(TextDocument)

text_document = TextDocument()
    spreadsheet_document = SpreadsheetDocument()

    text_document.open()
    text_document.process()
    text_document.close()

    spreadsheet_document.open()
    spreadsheet_document.process()
    spreadsheet_document.close()
    

    def open(self) :
    # {
        print("Opening document")
    # }

    def close(self) :
    # {
        print("Closing document")
    # }
    
    def open(self) :
    # {
        print("Opening document")
    # }

    def close(self) :
    # {
        print("Closing document")
    # }


'''