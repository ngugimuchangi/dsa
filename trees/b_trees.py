"""
B Trees
- BTrees are a generalization of BSTs where each node can have more than 2 children.
- BTrees are used when the data is too large to fit in the main memory.
- BTrees are also used in databases and file systems.
- BTrees are balanced trees.
"""

from typing import Optional


class BTreeNode:
    """
    B Tree Node
    """

    def __init__(self, is_leaf: bool = False) -> None:
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.count = 0


class BTree:
    def __init__(self, min_order: int) -> None:
        self.min_order = min_order
        self.root = BTreeNode(is_leaf=True)

    def insert(self, val: int) -> None:
        """
        - Insert a value into the B Tree
        - Args:
            - val: value to be inserted
        - Approach:
            1. If the root is full, create a new node and make it the root
                - Split the child
                - Call insert_non_full on the new root
            2. If the root is not full, call insert_non_full on the root
        """
        if self.root.count == (2 * self.min_order) - 1:
            temp = BTreeNode()
            temp.children.insert(0, self.root)
            self.root = temp
            self.split_node(temp, 0)
        self.insert_non_full(self.root, val)

    def insert_non_full(self, node: BTreeNode, val: int) -> None:
        """
        - Insert a value into a non-full node
        - Args:
            - `node`: node to insert the value into
            - `val`: value to be inserted
        - Approach:
            1. If the node is a leaf, insert the value into the node
            2. If the node is not a leaf, find the child to insert the value into
                - If the child is full, split the child
                - If the value from the split is greater than the value to be inserted, insert into the left child
                - Else insert into the right child - i.e i += 1
                - Call insert_non_full on the child
                - Continues until a leaf node is reached
                - Note that nodes that are already full are split even before the value is inserted
        """
        i, keys = node.count - 1, node.keys
        if node.is_leaf:
            keys.append(None)
            while i >= 0 and keys[i] > val:
                keys[i + 1] = keys[i]
                i -= 1
            keys[i + 1] = val
            node.count += 1
        else:
            while i >= 0 and keys[i] > val:
                i -= 1
            i += 1
            if node.children[i].count == (2 * self.min_order) - 1:
                self.split_node(node, i)
                if val > keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], val)

    def split_node(self, parent: BTreeNode, child_index: int) -> None:
        """
        - Preemptively split a full node
        - Args:
            - `parent`: parent node
            - `child_index`: index of the child to be split
        Approach:
            1. Create a new node and make it a child of the parent
            2. Move the median key to the parent and the right half of the keys to the new node
            3. Update the counts of the parent and the new node
        """
        child = parent.children[child_index]
        sibling = BTreeNode(is_leaf=child.is_leaf)

        # move median key to parent and sibling to parent's children
        parent.children.insert(child_index + 1, sibling)
        parent.count += 1
        parent.keys.insert(child_index, child.keys[self.min_order - 1])

        # split the keys
        sibling.keys = child.keys[self.min_order:]
        child.keys = child.keys[:self.min_order - 1]

        # update the counts of keys
        child.count = self.min_order - 1
        sibling.count = self.min_order - 1

        if not child.is_leaf:
            sibling.children = child.children[self.min_order:]
            child.children = child.children[:self.min_order]

    def search(self, val: int, node: Optional[BTreeNode] = None) -> Optional[BTreeNode]:
        """
        - Search for a value in the B Tree
        - Args:
            - `node`: node to start the search from
            - `val`: value to be searched for
        - Approach:
            1. If the node is None or the value is in the node, return the node and index
            2. If the node is a leaf, return None
            3. Else, search for the value in the appropriate child
        """
        node = self.root if node is None else node
        i = 0
        while i < node.count and val > node.keys[i]:
            i += 1
        if i < node.count and val == node.keys[i]:
            return node, i
        elif node.is_leaf:
            return None, -1
        else:
            return self.search(val, node.children[i])

    # TODO: Implement delete
    def delete(self, val: int, node: Optional[BTreeNode] = None):
        """
        Delete a value from the B Tree
        """
        NotImplemented

    def print_tree(self, root: BTreeNode, l: int = 0):
        """
        Print the B Tree pre-orderly
        """
        print("Level ", l, " ", root.count, end=" : ")
        for i in root.keys:
            print(i, end=" ")
        print()
        l += 1
        if root.children:
            for child in root.children:
                self.print_tree(child, l)


def main():
    B = BTree(3)

    for i in range(20):
        B.insert(i)

    B.print_tree(B.root)

    res, index = B.search(20)
    print('Search for 19:', res and res.keys[index])


if __name__ == "__main__":
    main()
