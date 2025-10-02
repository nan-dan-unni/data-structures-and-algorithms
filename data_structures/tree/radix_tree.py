import os


def find_common_starting_substring(str1: str, str2: str):
    return os.path.commonprefix([str1, str2])

    common = ""
    for i in range(min(len(str1), len(str2))):
        if not str1[i] == str2[i]:
            break
        common += str1[i]
    return common


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children


class RadixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, value: str, node=None):
        if node is None:
            node = self.root
        for child in node.children:
            common = find_common_starting_substring(child.value, value)
            if len(common) > 0:
                value = value[len(common) :]
                if len(value) == 0:
                    return
                if child.value == common:
                    self.insert(value, child)
                else:
                    old_value = child.value
                    old_children = child.children
                    child.value = common
                    child.children = []
                    child.children.append(Node(old_value[len(common) :], old_children))
                    child.children.append(Node(value))

                return
        node.children.append(Node(value))

    def preview(self, node=None, level=0):
        if node is None:
            node = self.root

        print(" " * (level * 2) + node.value)
        for child in node.children:
            self.preview(child, level + 1)


if __name__ == "__main__":
    tree = RadixTree()
    tree.insert("apple")
    tree.insert("apricot")
    tree.insert("april")
    tree.insert("april")
    tree.insert("april")
    tree.insert("april")
    tree.insert("april")
    tree.insert("april")
    tree.insert("banana")
    tree.insert("band")
    tree.insert("balloon")
    tree.insert("bring")
    tree.preview()
