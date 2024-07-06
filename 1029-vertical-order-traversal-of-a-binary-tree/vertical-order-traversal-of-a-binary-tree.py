from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # traverse the graph, use dict to group them by x
        group = defaultdict(list)
        queue = [(root, 0, 0)]
        for node in queue:
            if node[0]:
                point, x, y = node
                group[x].append((point.val, y))
                if point.left:
                    queue.append((point.left, x-1, y+1))
                if point.right:
                    queue.append((point.right, x+1, y+1))
        
        # group by vertical line
        res = []
        for x in sorted(group):
            res.append(group[x])
        
        # sort by value then by depth
        for i, item in enumerate(res):
            item.sort(key=lambda x: x[0])
            item.sort(key=lambda x: x[1])
            res[i] = [val for val, y in item]
                
        return res