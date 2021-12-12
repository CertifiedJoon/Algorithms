class Solution:
    def minMeetingRooms(self, intervals):
        """
        compute the max number of overlaps in intervals
        intervals are not sorted
        cant bucket sort

        Approach 1
            sort and check overlaps -> nlogn time, constant space
        """        

        if not intervals:
            return []

        free_rooms = []

        intervals.sort(key= lambda x: x[0])

        heaq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if i[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.push(i[1])
        
        return len(free_rooms)   