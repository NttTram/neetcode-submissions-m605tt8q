class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            bucket[freq].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res[i].append(n)

            if len(res) == k:
                return res