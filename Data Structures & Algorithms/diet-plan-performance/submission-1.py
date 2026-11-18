class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left = 0
        score = 0
        total = 0

        for r in range(len(calories)):
            if r - left + 1 > k:
                left += 1
            
            total += calories[r]

            if r - left + 1 == k:
                if total > upper:
                    score += 1
                elif total < lower:
                    score -= 1
            
                total -= calories[left]

        return score
