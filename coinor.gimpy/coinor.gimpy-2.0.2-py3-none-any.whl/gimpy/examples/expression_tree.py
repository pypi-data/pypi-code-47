from __future__ import print_function
try:
    from src.gimpy import BinaryTree
except ImportError:
    from coinor.gimpy import BinaryTree
    
T = BinaryTree(display = 'pygame')
T.add_root('*', label='*')
T.add_left_child('+', '*', label='+')
T.add_left_child('4', '+', label='4')
T.add_right_child('5', '+', label='5')
T.add_right_child('7', '*', label='7')
T.set_display_mode('file')
T.display(basename='expression')
T.printexp()
print()
T.postordereval()
