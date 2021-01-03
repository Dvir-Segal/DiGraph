# import self as self


class NodeData:
    """ This abstract class represents a Node (a component of a graph) """
    key = 0
    counter = 0
    # Variables declared inside the class definition, but not inside a method are class or static variables
    weight = 0.0
    info = ""
    tag = 0
    parent = None  # nodeData parent. is it necessary?
    visited = "false"
    tagB = 0.0

    def __init__(self):
        self.key = self.counter
        NodeData.counter = NodeData.counter + 1
        """
          Constructor for NodeData. the key is defined by a general counter.
        """

    def setkey(self, key: int):  # replaces the constructor NodeData(int key) in previous project
        self.key = key

        """
             Sets the given NodeData key 
             @return
        """

    def copyNodeData(self, n):
        self.key = n.getKey()
        # self.geoLocation = n.getLocation()
        self.weight = n.getWeight()
        self.info = n.getInfo()
        self.tag = n.getTag()

    """
      Copy constructor. takes a NodeData named n and copies it into this self NodeData.
      @return
     """

    def getKey(self):
        return self.key

    """
      Returns the key (id) associated with this node.   
      @return
     """

    def getWeight(self):
        return self.weight

    """
    Returns the weight associated with this node.
    @return
    """

    def setWeight(self, w: float):
        self.weight = w

    """
    Allows changing this node's weight.
     @param w - the new weight
    """

    def getInfo(self):
        return self.info

    """
    Returns the remark (meta data) associated with this node.
        @return
    """

    def setInfo(self, s):
        self.info = s

    # the key of the father in this shortest path

    """
    Allows changing the remark (meta data) associated with this node.
     @param s
    """

    def getTag(self):
        return self.tag

    """
    Temporal data (aka color: e,g, white, gray, black)
    which can be used be algorithms
    @return
    """

    def setTag(self, t):
        self.tag = t

    # distance of weight, """"""whats the weight in the shortest path from the src up until this one (to dest)

    """
    Allows setting the "tag" value for temporal marking an node - common
    practice for marking by algorithms.

    @param t - the new value of the tag
    """

    def getTagB(self):
        return self.tagB

    """
    Allows getting the "tagB" value for temporal marking an node - common
    practice for marking by algorithms.
    @param t - the new value of the tag
    """

    def setTagB(self, t):
        self.tagB = t

    # distance of weight, """"""whats the weight in the shortest path from the src up until this one (to dest)

    """
    Allows setting the "tagB" value for temporal marking an node - common
    practice for marking by algorithms.
    @param t - the new value of the tag
    """

    def toString(self):
        return "NodeDatakey=" + self.key + ''

    """
    Tostring method
    """

    def setDub(self, e):
        self.dub = e

    """
    This function sets the dub value of this NodeData
    """

    def setCounter(self, count):
        self.counter = count

    """
    This function sets the conuter of this NodeData.
    """
