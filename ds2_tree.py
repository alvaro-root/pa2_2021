class Node:
    """
    Inserting into a Tree

    To insert into a tree we use the same node class created above and add an insert method to it The insert method
    compares the value of the node to the parent node and decides to add it as a left node or a right node.

    Traversing a Tree
    The tree can be traversed by deciding on a sequence to visit each node. As we can clearly see we can start at a node
    then visit the left sub-tree first and right sub-tree next. Or we can also visit the right sub-tree first and left
    sub-tree next. Accordingly there are different names for these tree traversal methods.

    Traversal is a process to visit all the nodes of a tree and may print their values too. Because, all nodes are connected
    via edges (links) we always start from the root (head) node. That is, we cannot randomly access a node in a tree. There
    are three ways which we use to traverse a tree −

    In-order Traversal
    Pre-order Traversal
    Post-order Traversal

    In-order Traversal
    In this traversal method, the left subtree is visited first, then the root and later the right sub-tree. We should
    always remember that every node may represent a subtree itself.

    In the below python program, we use the Node class to create place holders for the root node as well as the left and
    right nodes. Then we create a insert function to add data to the tree. Finally the Inorder traversal logic is
    implemented by creating an empty list and adding the left node first followed by the root or parent node. At last
    the left node is added to complete the Inorder traversal. Please note that this process is repeated for each
    sub-tree until all the nodes are traversed.

    Pre-order Traversal
    In this traversal method, the root node is visited first, then the left subtree and finally the right subtree.

    In the below python program, we use the Node class to create place holders for the root node as well as the left and
    right nodes. Then we create a insert function to add data to the tree. Finally the Pre-order traversal logic is
    implemented by creating an empty list and adding the root node first followed by the left node. At last the right
    node is added to complete the Pre-order traversal. Please note that this process is repeated for each sub-tree until
    all the nodes are traversed.

    Post-order Traversal
    In this traversal method, the root node is visited last, hence the name. First we traverse the left subtree, then
    the right subtree and finally the root node.

    In the below python program, we use the Node class to create place holders for the root node as well as the left and
    right nodes. Then we create a insert function to add data to the tree. Finally the Post-order traversal logic is
    implemented by creating an empty list and adding the left node first followed by the right node. At last the root or
    parent node is added to complete the Post-order traversal. Please note that this process is repeated for each
    sub-tree until all the nodes are traversed.

    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root._data)
            res = res + self.inorder_traversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root._data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res
    # Postorder traversal
    # Left ->Right -> Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root._data)
        return res


if __name__ == "__main__":

    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.PrintTree()
    print(root.inorder_traversal(root))
    print(root.preorder_traversal(root))
    print(root.postorder_traversal(root))