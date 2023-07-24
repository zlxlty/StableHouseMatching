import heapq

from student_agent import StudentAgent


class HouseAgent(object):

    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.member_heap = []

    def try_accept_member(self, student: StudentAgent):
        heap_item = (student.house_preference_dict[self.name], student)
        if len(self.member_heap) < self.max_size:
            heapq.heappush(self.member_heap, heap_item)
            return None
        else:
            item = heapq.heappushpop(self.member_heap, heap_item)[1]
            return item