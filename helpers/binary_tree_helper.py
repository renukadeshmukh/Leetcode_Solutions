# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class BinaryTree:

    @staticmethod
    def build_binary_tree(values):
        nodes = [None if v is None else TreeNode(v) for v in values]

        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root
        
    @staticmethod
    def print_binary_tree(root):
        lines = BinaryTree._build_tree_string(root, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    @staticmethod
    def _build_tree_string(root, curr_index, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            BinaryTree._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BinaryTree._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end


    

#root = BinaryTree.build_binary_tree([1,3,2,5,3,None,9])
#tree = BinaryTree.print_binary_tree(root)
#print(tree)

root = BinaryTree.build_binary_tree([5,4,7,3,None,2,None, -1, None, 9])
tree = BinaryTree.print_binary_tree(root)
print(tree)

root = BinaryTree.build_binary_tree([0, None, 0, None, 0, None])
tree = BinaryTree.print_binary_tree(root)
print(tree)