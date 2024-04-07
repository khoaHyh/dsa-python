from typing import List, Optional
import json


class TreeNode:
    # TODO: consider adding a height property to nodes to reduce computation when trying to rebalance
    def __init__(self, value: int):
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.value = value

    def _to_dict(self) -> dict:
        return {
            "left": None if self.left is None else self.left.value,
            "right": None if self.right is None else self.right.value,
            "value": self.value
        }

    def __str__(self):
        return json.dumps(self._to_dict(), indent=4)


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
            return not_found_message if node is None else node

    def _get_recursive(self, node: TreeNode, value: int) -> Optional[TreeNode]:
        if value == node.value:
            return node
        elif value < node.value:
            # If the given value is less than the current node's value, return None if the left branch is None.
            # Otherwise, keep traversing left.
            if node.left is None:
                return None
            else:
                return self._get_recursive(node.left, value)
        else:
            # If the given value is greater than the current node's value, return None if the right branch is None.
            # Otherwise, keep traversing left.
            if node.right is None:
                return None
            else:
                return self._get_recursive(node.right, value)

    def inorder_traversal(self) -> Optional[List[str]]:
        if self.root is None:
            return None
        else:
            return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node: TreeNode) -> List[str]:
        queue: List[str] = []

        # Accumulate values when recursive traversing the left subtree
        if node.left is not None:
            queue.extend(self._inorder_traversal_recursive(node.left))

        # Only insert the node's value after the subtree has been traversed
        queue.append(str(node.value))

        # Accumulate values when recursively traversing the right subtree
        if node.right is not None:
            queue.extend(self._inorder_traversal_recursive(node.right))

        return queue

    # TODO: remaining methods
    # def preorder_traversal(self):
    #
    # def postorder_traversal(self):
    #
    # def balance():

    # both branches of node to delete are empty => simple deletion
    # left branch of node to delete is empty  => right node replaces
    # right branch of node to delete is empty  => left node replaces
    # both branches of node to delete have nodes => largest node in left tree OR smallest node in right tree replaces
    def delete(self, value: int):
        if self.root is None:
            return None
        else:
            parent_node = self._get_parent(self.root, value)

            if parent_node is None:
                return "Value to be deleted has no parent."

            sub_tree = "left" if parent_node.left is not None and parent_node.left.value == value else "right"
            node_to_delete = parent_node.left if parent_node.left is not None and parent_node.left.value == value else parent_node.right

            if node_to_delete is None:
                raise Exception("Node to be deleted's parent was found but the node itself wasn't found.")

            if node_to_delete.left is None and node_to_delete.right is None:
                if sub_tree == "left":
                    parent_node.left = None
                else: 
                    parent_node.right = None

                self.size -= 1 
            elif node_to_delete.left is None and node_to_delete.right is not None:
                replacing_node = node_to_delete.right                

                if sub_tree == "left":
                    parent_node.left = replacing_node
                else: 
                    parent_node.right = replacing_node

                self.size -= 1 
            elif node_to_delete.left is not None and node_to_delete.right is None:
                replacing_node = node_to_delete.left

                if sub_tree == "left":
                    parent_node.left = replacing_node
                else:
                    parent_node.right = replacing_node

                self.size -= 1 
            else:
                # TODO: for now we will default to the largest node in left subtree to replace but a more robust solution would be to use the 
                # balance factor of the node being deleted to decide which node will take its place
                if node_to_delete.left is None:
                    raise Exception("This else branch should mean that the node to delete has both subtrees.")

                # Go to left subtreeof the node to be deleted, find biggest node
                replacing_node = self.get_max_node(node_to_delete.left)
                parent_replacing_node = self._get_parent(node_to_delete.left, replacing_node.value)

                if parent_replacing_node is None or parent_replacing_node.right is None:
                    raise Exception("The max node in the left subtree must have a parent.")

                # Set the replacing node's parent to not to point to it anymore
                parent_replacing_node.right = None

                # Set the node to be deleted's parent to point to the replacing node
                if sub_tree == "left":
                    parent_node.left = replacing_node
                else: 
                    parent_node.right = replacing_node

                self.size -= 1 

            return self.inorder_traversal()
            

    def _get_parent(self, node:TreeNode, value: int):
        if (node.left is not None and node.left.value == value) or (node.right is not None and node.right.value == value):
            return node
        elif value < node.value:
            if node.left is None:
                return None
            else:
                return self._get_parent(node.left, value)
        else:
            if node.right is None:
                return None
            else:
                return self._get_parent(node.right, value)

    def get_min_node(self, node: TreeNode):
        if node.left is None:
            return node
        else:
            return self.get_min_node(node.left)

    def get_max_node(self, node: TreeNode):
        if node.right is None:
            return node
        else:
            return self.get_max_node(node.right)


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

    print("bst size:", bst.size) 
    print("bst inorder traversal:", bst.inorder_traversal()) 
    print("get (5):", bst.get(5)) 
    print("get (13):", bst.get(13)) 
    print("get (6):", bst.get(6)) 
    print("bst inorder traversal:", bst.inorder_traversal()) 
    print("bst size:", bst.size)
    print("delete(4)", bst.delete(4))
    print("bst size:", bst.size)

if __name__ == "__main__":
    main()
