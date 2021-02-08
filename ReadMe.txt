Treap - Random Binary Search Tree(RBST):
A Treap or a Random Binary Search Tree(RBST) that stores data in a sorted order and offers efficient Search, insertion and deletion of data in the treap.

For each node n in the treap the following invariants hold:

Every node in the left subtree of n contains a key which is smaller than the key in the root node.
Every node in the right subtree of n contains a key which is larger than the key in the root node.
Assigns a random priority number to each node before it being inserted it into the RBST(Range given =1,100).
Make sure that each node in the treap has small priority than its children. (i.e. in priority order (highest first), 1 -> 2 -> 34 etc.)

Documentation:
The treap or RBST consists of 2 classes, Node and RBST with the following public methods/functions:

Search() -> returns the node of the given key, returns False if not in the RBST.
Insert() -> insert a node to the RBST, returns True if successful. 
Delete() -> Delete the node specified from the RBST, returns True if successful
Replace() -> repalce a node (key) in the RBST. 
FindMin() -> returns the minimum node in the RBST.
FindMax() -> returns the maximum node in the RBST.
Succesor() -> returns the successor node in the RBST w.r.t root.
Predessor() -> returns the predessor node in the RBST w.r.t root.