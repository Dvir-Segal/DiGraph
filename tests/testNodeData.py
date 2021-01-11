import unittest
from src.NodeData import NodeData


# from : https://stackoverflow.com/questions/35964848/pycharm-no-tests-were-found
# NOTE: in order to recognize test functions they must be named test_
# in your case rename xyCheck to test_xyCheck :)

class MyTestCase(unittest.TestCase):

    def setUp(self): #initalizes the nodes counter before each test to be 0.
        NodeData.counter = 0

    def test_creatingNewNodeAndGetKey(self):
        """
        Test that we can create a new NodeData. and get it's key (in the beginning should be 0).
        """
        # creating a new node
        newNode = NodeData()
        print("key of node is", newNode.getKey())
        self.assertEqual(0, newNode.getKey())

    def test_setAndGetKeysAndInfosAndCopyNodeData(self):
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
        self.assertEqual(0, node1.getKey())
        print("key of node2 is", node2.getKey())
        self.assertEqual(1, node2.getKey())
        print("info of node1 is", node1.getInfo())
        self.assertEqual("first", node1.getInfo())
        print("key of node2 is", node2.getInfo())
        self.assertEqual("second", node2.getInfo())
        print("set the info of node1 to be change1", node1.setInfo("change1"))
        self.assertEqual("change1", node1.getInfo())
        print("change the key of node2 to be 3", node2.setkey(3))
        self.assertEqual(3, node2.getKey())
        print("copying node1 to copyNode")
        copyNode = NodeData()
        copyNode.copyNodeData(node1)
        print("key of node1 is", node1.getInfo())
        print("info of node1 is", node1.getInfo())
        print("key of copyNode is", copyNode.getInfo())
        print("info of copyNode is", copyNode.getInfo())

    # def testCopyNodeData(self, n):
    #
    #     self.key = n.getKey()
    #     # self.geoLocation = n.getLocation()
    #     self.weight = n.getWeight()
    #     self.info = n.getInfo()
    #     self.tag = n.getTag()
    #
    # """
    #   Tests copy constructor. takes a NodeData named n and copies it into this self NodeData.
    #   @return
    #  """

    def testSetAndGetWeight(self):
        node1 = NodeData()
        node1.setWeight(8)
        self.assertEqual(8, node1.getWeight())

    """
    Testing set&gets methods of NodeData's weight
    """

    def testSetAndGetTag(self):
        node1 = NodeData()
        node1.setTag(10)
        self.assertEqual(10, node1.getTag())

    """
    Testing set&gets methods of NodeData's tag
    """

    def testSetAndGetTagB(self):
        node1 = NodeData()
        node1.setTagB(10)
        self.assertEqual(10, node1.getTagB())

    """
    Testing set&gets methods of NodeData's tag
    """

    # distance of weight, """"""whats the weight in the shortest path from the src up until this one (to dest)

    """
    Testing set&gets methods of NodeData's tagB
    """

    # def testToString(self):
    #     node1 = NodeData()
    #     self.assertEqual("NodeDatakey=", node1.key, '', node1.toString())

    """
    testing Tostring method
    """

    def testSetDub(self):
        node1 = NodeData()
        node1.setDub(3)
        self.assertEqual(3, node1.dub)

    """
    This function tests the setDub function in NodeData
    """

    def setCounter(self):
        node1 = NodeData()
        node1.setCounter(300)
        self.assertEqual(node1.counter, 300)

    """
    This function tests the setConuter function in NodeData.
    """


if __name__ == '__main__':
    unittest.main()
