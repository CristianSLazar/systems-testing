from tree import Tree

class TestTree:
    def setup_method(self):
        self.tree1 = Tree();
        for i in range(10):
            self.tree1.add(i)

        self.tree2 = Tree();
        z = ord('z')
        for i in range(25):
            self.tree2.add(chr(z - i))

    def test_find_1(self):
        node = self.tree1.find(7)
        assert node.data == 7

    def test_find_2(self):
        node = self.tree2.find('l')
        assert node.data == 'l'
