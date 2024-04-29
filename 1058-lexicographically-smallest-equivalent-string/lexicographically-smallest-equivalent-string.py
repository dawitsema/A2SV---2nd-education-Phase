class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            xval = find(x)
            yval = find(y)
            if xval != yval:
                if xval < yval:
                    parent[yval] = xval
                else:
                    parent[xval] = yval
        
        # def connected(x, y):
        #     return find(x) == find(y)

        parent = {}
        for i in range(len(s1)):
            if s1[i] not in parent and s2[i] not in parent:
                if s1[i] < s2[i]:
                    parent[s1[i]] = s1[i]
                    parent[s2[i]] = s1[i]
                else:
                    parent[s1[i]] = s2[i]
                    parent[s2[i]] = s2[i]
            elif s1[i] not in parent:
                y = find(s2[i])
                if s1[i] < y:
                    parent[y] = s1[i]
                    parent[s1[i]] = s1[i]
                else:
                    parent[y] = y
                    parent[s1[i]] = y
            elif s2[i] not in parent:
                x = find(s1[i])
                if s2[i] < x:
                    parent[x] = s2[i]
                    parent[s2[i]] = s2[i]
                else:
                    parent[x] = x
                    parent[s2[i]] = x
            else:
                y = find(s2[i])
                x = find(s1[i])
                if y != x:
                    if y < x:
                        parent[x] = y
                        parent[y] = y
                    else:
                        parent[x] = x
                        parent[y] = x

        ans = []
        for i in range(len(baseStr)):
            if baseStr[i] in parent:
                ans.append(find(baseStr[i]))
            else:
                ans.append(baseStr[i])
        
        return "".join(ans)

                    