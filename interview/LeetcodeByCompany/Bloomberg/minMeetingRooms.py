class Solution:
    def minMeetingRooms(self, intervals):
        """
        compute the max number of overlaps in intervals
        intervals are not sorted
        cant bucket sort

        Approach 1
            sort and check overlaps -> nlogn time, constant space
        """

        intervals = sorted(intervals, key= )

