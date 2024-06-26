class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(v) for v in version1.split(".")]
        version2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(version1), len(version2))):
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
            