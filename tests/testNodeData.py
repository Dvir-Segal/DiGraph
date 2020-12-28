import unittest
from src.NodeData import NodeData

#from : https://stackoverflow.com/questions/35964848/pycharm-no-tests-were-found
#NOTE: in order to recognize test functions they must be named test_
# in your case rename xyCheck to test_xyCheck :)

class MyTestCase(unittest.TestCase):

    def test_creatingNewNodeAndGetKey(self):
        """
        Test that we can create a new NodeData. and get it's key (in the beginning should be 0).
        """
        # creating a new node
        newNode = NodeData()
        print("key of node is", newNode.getKey())
        self.assertEqual(0, newNode.getKey())


    def test_setAndGetKeysAndInfos(self):
        """
        Test that we can create Node Datas, set and get their infos,
         and get their keys(in the beginning should be 0).
         Then, to CHANGE their keys and infos, and get them changed:
         *create Node Datas
         *get their keys
         *set and get their infos
         *set (change) and get their keys
         *set (change) and get their infos
        """
        # creating a new node
        node1 = NodeData()
        node2 = NodeData()
        node1.setInfo("first")
        node2.setInfo("second")
        print("key of node1 is", node1.getKey())
        self.assertEqual(1, node1.getKey())
        print("key of node2 is", node2.getKey())
        self.assertEqual(2, node2.getKey())
        print("info of node1 is", node1.getInfo())
        self.assertEqual("first", node1.getInfo())
        print("key of node2 is", node2.getInfo())
        self.assertEqual("second", node2.getInfo())
        print("set the info of node1 to be change1", node1.setInfo("change1"))
        self.assertEqual("change1", node1.getInfo())
        print("change the key of node2 to be 3", node2.setkey(3))
        self.assertEqual(3, node2.getKey())


if __name__ == '__main__':
    unittest.main()
