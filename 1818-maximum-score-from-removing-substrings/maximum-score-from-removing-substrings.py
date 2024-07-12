class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pts = 0
        s = list(s)

        if x > y:
            pts += self.remove_pair(s, "ab", x)
            pts += self.remove_pair(s, "ba", y)
        else:
            pts += self.remove_pair(s, "ba", y)
            pts += self.remove_pair(s, "ab", x)

        return pts

    def remove_pair(self, s, pair, pts_per_rem):
        pts = 0
        w_idx = 0

        for r_idx in range(0, len(s)):
            s[w_idx] = s[r_idx]
            w_idx += 1
            if (
                w_idx > 1
                and s[w_idx - 2] == pair[0]
                and s[w_idx - 1] == pair[1]
            ):
                w_idx -= 2
                pts += pts_per_rem

        del s[w_idx:]

        return pts
