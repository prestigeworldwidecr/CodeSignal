'''

Imagine that you're designing a text editor. The users would undoubtedly need an undo and redo feature. We have sketched out a simple model of a text editor, which has these features modeled around the concept of Stacks. The undo corresponds to the pop operation, and whenever we append text, it corresponds to the push operation within the Stack.

Go ahead and press the Run button. Analyze and comprehend how this marvel of Stacks works.

'''

class Editor :
# {
    def __init__(self) :
    # {
        self.text = ""
        self.history_stack = []
        self.redo_stack = []
    # }

    def append_text(self, text) :
    # {
        self.history_stack.append(self.text)
        # self.text += text
        self.text = self.text + text
    # }

    def undo(self) :
    # {
        if (self.history_stack) :
        # {
            self.redo_stack.append(self.text)
            self.text = self.history_stack.pop()
        # }

        else :
        # {
            print("Undo operation not possible. No history available.")
        # }

    # }

    def redo(self) :
    # {
        if (self.redo_stack) :
        # {
            self.history_stack.append(self.text)
            self.text = self.redo_stack.pop()
        # }

        else :
        # {
            print("Redo operation not possible. No redo history available.")
        # }
    
    # }

    def display_text(self) :
    # {
        print(self.text)
    # }

# }

editor = Editor()

editor.append_text("Hello, ")
editor.append_text("CodeSignal!")
editor.display_text()
editor.undo()
editor.display_text()
editor.undo()
editor.display_text()
editor.redo()
editor.display_text()
editor.redo()
editor.display_text()
editor.redo()
editor.undo()

'''

***** BONEYARD *****

'''