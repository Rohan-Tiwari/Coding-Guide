# undirected graph code
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0':set(['1','2']),
         '1':set(['0','3','4']),
         '2':set(['0']),
         '3':set(['1']),
         '4':set(['2','3'])}

dfs(graph,'0')


# Traversal : inorder- binary tree
class TreeNode:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def addNode(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = addNode(root.right, key)
        else:
            root.left = addNode(root.left, key)
    return root

def inorderTraversal(root):
    result = []
    stack = []
    node = root

    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if not stack:
                break
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
    return result
    
def utility():
    root = TreeNode(50)
    root = addNode(root, 30)
    root = addNode(root, 20)
    root = addNode(root, 40)
    root = addNode(root, 70)
    root = addNode(root, 60)
    root = addNode(root, 80)

    print(inorderTraversal(root))
utility()
    
