# http://openbookproject.net/thinkcs/python/english2e/ch21.html
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
    if tree == None: return
    print(tree.cargo,end='')
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo,end='')

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.cargo,end='')
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print('  ' * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

# Check if a character is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse_expression(exp):
    exp = exp.replace(' ','')
    exp = list(exp)
    for i in range(len(exp)):
        if RepresentsInt(exp[i]):
            exp[i] = int(exp[i])
    exp.append('end')
    # print(exp)
    return exp

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    x = token_list[0]
    if type(x) != type(0): return None
    del token_list[0]
    return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*',a,b)
    else:
        return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list,'+'):
        b = get_sum(token_list)
        return Tree('+',a,b)
    else:
        return a


# left = Tree(2)
# right = Tree(3)
# tree = Tree(1, left, right)
#
# print(total(tree))

# tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
# print_tree(tree)
# print('')
# print_tree_postorder(tree)
# print('')
# print_tree_inorder(tree)
# print('')
# print_tree_indented(tree)

# expression = '(3 + 7) * 9'
# token_list = parse_expression(expression)
# print(token_list)
# token_list = [9, 11, 'end']
# x = get_number(token_list)
# print_tree_postorder(x)
# print('')
# print(token_list)

# token_list = [9,'*',11,'end']
# tree = get_product(token_list)
# print_tree_postorder(tree)

# token_list = [9,'+',11,'end']
# tree = get_product(token_list)
# print_tree_postorder(tree)

# token_list = [2,'*',3,'*',5,'*',7,'end']
# tree = get_product(token_list)
# print_tree_postorder(tree)

token_list = [9, '*', 11, '+', 5, '*', 7, 'end']
tree = get_sum(token_list)
print_tree_postorder(tree)

