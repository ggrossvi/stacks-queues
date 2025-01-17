from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    '''
    https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        print('calling str')
        if self.message:
            return 'StackEmptyException, {0}'.format(self.message)
        else:
            return 'StackEmptyException has been raised'
    '''
    raise StackEmptyException # MyCustom Error is being raised without any arguments, so None will be sent to the message attribute in the object. The str method will be called and will print the message 'MyCustomEror message has been raised'
    raise StackEmptyException('We have a problem')       
    '''



class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        self.store.add_first(element)


    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        try:
            return self.store.remove_first()
        
        except LinkedList.EmptyListError():
            raise StackEmptyException("The Stack is empty")
            


        

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.empty():
            return True
        return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        pass
