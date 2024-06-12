class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pt = 0
        i = 0

        while i < len(name):
            count_name = 1
            count_typed = 1

            while i + 1 < len(name) and name[i] == name[i + 1]:
                i += 1
                count_name += 1

            while pt + 1 < len(typed) and typed[pt] == typed[pt + 1]:
                pt += 1
                count_typed += 1

            if i < len(name) and pt < len(typed) and (name[i] != typed[pt] or count_typed < count_name):
                return False

            i += 1
            pt += 1

        return pt == len(typed)
