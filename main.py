import math
import tinydb

from define import *
from house_agent import HouseAgent
from student_agent import StudentAgent, PreferenceItem


def main():
    db = tinydb.TinyDB("data/db.json", ensure_ascii=False)

    unmatched_student_agents = []
    house_agents = {}

    for student in db:
        house_preference = sorted([
            PreferenceItem(house_name=house_name, score=student[house_name]) for house_name in HOUSE_NAMES
        ], key=lambda x: x.score, reverse=True)
        
        unmatched_student_agents.append(StudentAgent(student[STR_USER_ID], student[STR_USERNAME], house_preference))
    
    house_max_size = math.ceil(len(unmatched_student_agents) / len(HOUSE_NAMES))
    print("house_max_size:", house_max_size)
    for house_name in HOUSE_NAMES:
        house_agents[house_name] = HouseAgent(house_name, house_max_size)
        
    
    while len(unmatched_student_agents) > 0:
        current_student_agent = unmatched_student_agents.pop(0)
        match_candidate = current_student_agent.get_next_candidate()
        abandoned_student = house_agents[match_candidate.house_name].try_accept_member(current_student_agent)
        abandoned_student and unmatched_student_agents.append(abandoned_student)
        
    for house_name, house_agent in house_agents.items():
        print(house_name, [student.name for _, student in house_agent.member_heap])

if __name__ == "__main__":
    main()
