# coding: utf-8
#
# Copyright 2021 The Technical University of Denmark
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations
import sys
import itertools
import numpy as np
from utils import pos_add, pos_sub, APPROX_INFINITY
from collections import deque, defaultdict

import domains.hospital.state as h_state
import domains.hospital.goal_description as h_goal_description
import domains.hospital.level as h_level


class HospitalZeroHeuristic:
    def __init__(self):
        pass

    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior 
        # to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
        pass

    def h(self, state: h_state.HospitalState, 
                goal_description: h_goal_description.HospitalGoalDescription) -> int:
        return 0
    

class HospitalGoalCountHeuristics:

    def __init__(self):
        pass


    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior 
        # to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
       pass
    
    def h(self, state: h_state.HospitalState, 
                goal_description: h_goal_description.HospitalGoalDescription) -> int:
        # your code here...
        hCount = 0
        for (goal_position, goal_char, is_positive_literal) in goal_description.goals:
            char = state.object_at(goal_position)
            if is_positive_literal and goal_char != char:
                hCount += 1
            elif not is_positive_literal and goal_char == char:
                hCount += 1
        return hCount

class HospitalAdvancedHeuristics:

    def __init__(self):
        pass

    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
        pass

    def h(self, state: h_state.HospitalState, goal_description: h_goal_description.HospitalGoalDescription) -> int:
        # Custom heuristic to calculate the manhatten distance between an agent and it's goal     
        maxDist = 0
        for goal_position, goal_char, _ in goal_description.agent_goals:
            for agent_pos, agent_char in state.agent_positions:
                if goal_char == agent_char:
                    dist = pos_sub(goal_position, agent_pos)
                    distSum =abs(dist[0]) + abs(dist[1])
                if distSum > maxDist:
                    maxDist = distSum
        # for x in goal_description.box_goals:
        #    dist = pos_sub(state.box_goal_positions[x], state.box_positions[x])
        #    distSum = dist[0] + dist[1]
        #    if distSum > maxDist:
        #        maxDist = distSum
        return maxDist