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
        Test that we can create a new NodeData. and get it's key (in the beginning should be 0).
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


if __name__ == '__main__':
    unittest.main()
