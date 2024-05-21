class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] >= size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]

        parent = {}
        size = {}

        emails = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    size[email] = 1
                union(first_email, email)
                emails[email] = name

        email_groups = defaultdict(list)
        for email in parent:
            root_email = find(email)
            email_groups[root_email].append(email)

        result = []
        for root_email, email_list in email_groups.items():
            name = emails[root_email]
            result.append([name] + sorted(email_list))

        return result
