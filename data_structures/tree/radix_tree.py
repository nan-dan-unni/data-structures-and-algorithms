import os, json


def find_common_starting_substring(str1: str, str2: str):
    return os.path.commonprefix([str1, str2])

    common = ""
    for i in range(min(len(str1), len(str2))):
        if not str1[i] == str2[i]:
            break
        common += str1[i]
    return common


class Node:
    def __init__(self, value, data=None, children=None):
        self.value = value
        self.data = data
        self.children = [] if children is None else children


class RadixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, new_value: str, new_data=None, node=None):
        if node is None:
            node = self.root
        for child in node.children:
            common = find_common_starting_substring(child.value, new_value)
            if len(common) > 0:
                new_value = new_value[len(common) :]
                if len(new_value) == 0:
                    return
                if child.value == common:
                    self.insert(new_value, new_data, child)
                else:
                    old_value = child.value
                    old_data = child.data
                    old_children = child.children
                    child.value = common
                    child.children = []
                    child.data = None
                    child.children.append(
                        Node(old_value[len(common) :], old_data, old_children)
                    )
                    child.children.append(Node(new_value, new_data))

                return
        node.children.append(Node(new_value, new_data))

    def search(self, value: str, node=None):
        if node is None:
            for child in self.root.children:
                result = self.search(value, child)
                if result:
                    return result
            return None

        common = find_common_starting_substring(node.value, value)

        if len(common) == 0:
            return None
        elif common == value:
            return node.data

        for child in node.children:
            result = self.search(value[len(common) :], child)
            if result:
                return result

        return None

    def preview(self, node=None, level=0):
        if node is None:
            node = self.root

        datastr = ("-" + json.dumps(node.data)) if node.data else ""
        print(" " * (level * 2) + node.value + datastr)
        for child in node.children:
            self.preview(child, level + 1)


if __name__ == "__main__":
    tree = RadixTree()
    tree.insert("apple", "A fruit")
    tree.insert("apricot", "A fruit")
    tree.insert("april", "A month")
    tree.insert("banana", "A fruit")
    tree.insert("band", "An object")
    tree.insert("balloon", "A toy")
    tree.insert("bring", "An action")
    tree.insert("dragon", "An animal")
    tree.preview()
    print("\n\nSearch for balloon =", tree.search("balloon"))
    print("Search for basket =", tree.search("basket"))
    print("Search for apple =", tree.search("apple"))
    print("Search for dragon =", tree.search("dragon"))
