
#===============================================
# AUTHOR: John Spataro
# DESCRIPTION:
#       Terminal formatting utilities.
#===============================================

## Globals

TERMINAL_CHARS = 72

## Functions

def section(sect_name, width=TERMINAL_CHARS):
    
    """ Prints a section header.
    
        ARGS:
            sect_name: section name (str)
            width: section width (int)
            
    """

    true_length = width - len(sect_name) - 1
    print("\n_%s" % (sect_name.upper() + "_" * true_length))
    
def tprint(msg, indent=0):

    """ Prints an indented tree item.
    
        ARGS:
            msg: item string (str)
            indent: indentation level (int)            
    """

    print("    " * indent + 
          " " * (indent+1) + 
          "'-- " + msg)

def blockprint(content, width=TERMINAL_CHARS):

    """ Prints a block of text from a block quote string.
    
        ARGS:
            content: block text (str)
            length: block width
            
    """

    lines = content.split('\n')
    print('_'*width)
    print('')
    for line in lines:
        p = line.strip()
        print("| " + p)
    print('_'*width)

def errprint(msg):
    
    """ Prints an error message.
    
        ARGS:
            msg: error message (str)
    """

    print('!! *** ERROR: %s' % msg)
    
def warnprint(msg):
    
    """ Prints a warning message.
    
        ARGS:
            msg: warning message (str)
    """

    print('!! *** WARNING: %s' % msg)
    
def critprint(msg):
    
    """ Prints a critical message.
    
        ARGS:
            msg: critical message (str)
    """
    
    print('!! *** CRITICAL: %s' % msg)
    
def newline():

    """ Prints a new line. """

    print('')
    


