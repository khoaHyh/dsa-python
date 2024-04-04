from typing import List, Optional


class TreeNode:
    def __init__(self, value):
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.value = value

class BinarySearchTree:        
    def __init__(self):
        self.root: Optional[TreeNode] = None
        self.size: int = 0

    def insert(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
        else:
            self._insert_recursive(self.root, value)
            self.size += 1

    def _insert_recursive(self, node: TreeNode, value: int):
        if value < node.value:
            # If the given value is less than the current node, insert at the left branch if it empty.
            # Otherwise, keep traversing left.
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            # If the given value is equal or greater than the current node, insert at the right branch if it empty.
            # Otherwise, keep traversing right.
            if node.right is None:
                node.right = TreeNode(value)
            else: 
                self._insert_recursive(node.right, value)

    def get(self, value: int):
        not_found_message = f"No nodes found with value '{value}'"
        if self.root is None:
            return not_found_message
        else:

            node: Optional[TreeNode] = self._get_recursive(self.root, value) 
            return not_found_message if node is None  else node

    def _get_recursive(self, node: TreeNode, value: int) -> Optional[TreeNode]:
        if value == node.value:
            return node
        elif value < node.value:
            # If the given value is less than the current node's value, return None if the left branch is None.
            # Otherwise, keep traversing left.
            if node.left is None:
                return None
            else:
                self._get_recursive(node.left, value)
        else:
            # If the given value is greater than the current node's value, return None if the right branch is None.
            # Otherwise, keep traversing left.
            if node.right is None:
                return None
            else:
                self._get_recursive(node.right, value)

    def inorder_traversal(self) -> Optional[List[str]]:
        if self.root is None:
            return None
        else:
            return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node: TreeNode) -> List[str]:
        queue: List[str] = []

        if node.left is not None:
            queue.extend(self._inorder_traversal_recursive(node.left))

        queue.append(node.value)

        if node.right is not None:
            queue.extend(self._inorder_traversal_recursive(node.right))

        return queue

    # both branches are empty => simple deletion
    # left branch is empty  => right node replaces
    # right branch is empty  => left node replaces
    # both branches have nodes => largest node in left tree OR smallest nodein right tree replaces
    def delete(self, value: int):
        if self.root is None:
            return None
        else:
            # find the node and its parent
                # we will something like prev_node to track
            # determine the node's branch situation
            # traverse to find the appropriate node to replace
                # replace the node
            found_node = self._get_recursive(self.root, value)

            if found_node is None:
                return None

def main():
    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)
    bst.insert(13)

    print("bst:", bst.size) 
    print("bst inorder traversal:", bst.inorder_traversal()) 

if __name__ == "__main__":
    main()
