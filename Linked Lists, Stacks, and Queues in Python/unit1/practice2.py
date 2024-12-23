'''

Nice work on the advanced text editor task! Now, let's dive into some real-life action.

After you briefed your manager about the editor, they appreciated the functionality but immediately requested an additional feature: an alert that will trigger when an undo operation is attempted on an empty history stack.

Your task is to enable your code to provide a user-friendly message, "Nothing to undo. Initialize a new action first.", for such attempts.

'''

class History :
# {
    def __init__(self) :
    # {
        self.history_stack = []
        self.future_stack = []
    # }

    def execute_action(self, action) :
    # {
        self.history_stack.append(action)
        print("Executing:", action)
    # }

    def undo_action(self) :
    # {
        if (self.history_stack is True) :
        # {
            self.future_stack.append(self.history_stack.pop())
            
            # self.history_stack[: : -1] if self.history_stack else "nothing"
            action = False
            
            if (self.history_stack[: : -1] is True) :
            # {
                action = True
            # }

            else :
            # {
                None
            # }
            
            print("Undid, now on action:", action)

        # }

        else :
        # {
            print("Nothing to undo. Initialize a new action first")
        # }
    
    # }

    def redo_action(self) :
    # {
        if (self.future_stack) :
        # {
            action = self.future_stack.pop()
            self.history_stack.append(action)
            print("Redid, now on action:", action)
        # }

        else :
        # {
            print("Nothing to redo")
        # }

    # }

# }

history = History()
history.undo_action()

'''

***** BONEYARD *****

'''