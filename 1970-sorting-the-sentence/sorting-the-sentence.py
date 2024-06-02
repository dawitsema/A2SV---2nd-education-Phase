class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = list(s.split())
        st = ['']*len(list1)
        for word in list1:
            ind = int(word[-1]) - 1
            word = word[:-1]
            st[ind] = word

        return " ".join(st)


        