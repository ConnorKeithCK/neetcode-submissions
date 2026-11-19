class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        recolor = k + 1
        currColor = 0

        for r in range(len(blocks)):
            if blocks[r] == "W":
                currColor += 1

            if r - left + 1 == k:
                recolor = min(recolor, currColor)
                if blocks[left] == "W":
                    currColor -= 1

                left += 1


        return recolor