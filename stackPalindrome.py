# create a palindome program that atakes the input of
# a word and determines if it is a palidrome or not using stacks\
class Stack:

    def __init__( self ):
        self.items = []

    def is_empty( self ):
        return self.items == []

    def push( self, item ):
        self.items.append( item )

    def pop( self ):
        return self.items.pop()

    def peek( self ):
        return self.items[len( self.items ) - 1 ]

    def size( self ):
        return len( self.items )



def main():
    # prompt the user for a string, set reverse string
    userString = input( "Enter string: " )
    reverse_string = ""

    # create stack object
    palindrome = Stack()

    # add each letter to stack 
    for letter in userString:
        palindrome.push( letter )

    # pop string from palindrome, add to reverse string
    while len( reverse_string ) < len( userString ):
        reverse_string += palindrome.pop()  

    # if equal, print True, else False
    if userString == reverse_string:
        print( "Is a palindrome." )
    else:
        print( "Not a palindrome." )  

# call the main function 
if __name__ == '__main__':
    main()
