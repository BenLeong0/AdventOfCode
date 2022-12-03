from collections import defaultdict
from typing import DefaultDict, Dict, List, Set, Tuple

Name = str
HappinessMatrix = Dict[Name, Dict[Name, str]]


def get_happiness_matrix(filename: str) -> HappinessMatrix:
     with open(filename, "r", newline="") as readfile:
          full_statements: List[Tuple[Set[str, str], int]] = [
               ({statement[0], statement[-1][:-1]}, int(statement[3]) * {"gain": 1, "lose": -1}[statement[2]])
               for statement in [x.split() for x in readfile.readlines()]
          ]
          happiness_matrix: DefaultDict[Name, DefaultDict[Name, str]] = defaultdict(lambda : defaultdict(int))
          for statement in full_statements:
               happiness_matrix[sorted(statement[0])[0]][sorted(statement[0])[1]] += statement[1]
               happiness_matrix[sorted(statement[0])[1]][sorted(statement[0])[0]] += statement[1]
          return {k:dict(v) for k,v in happiness_matrix.items()}

test_matrix = get_happiness_matrix("inputs/day13_test.in")
full_matrix = get_happiness_matrix("inputs/day13.in")

full_matrix_with_self = {k:{**v, "self":0} for (k,v) in full_matrix.items()}
full_matrix_with_self['self'] = {k:0 for k in full_matrix_with_self.keys()}


# Shared

def get_maximum_happiness(happiness_matrix: HappinessMatrix) -> int:
     start_name = list(happiness_matrix.keys())[0]
     seen: set[Name] = []
     def dfs(name: Name) -> int:
          seen.append(name)
          max_happiness = max([
               happiness_matrix[name][target_name] + dfs(target_name)
               for target_name in happiness_matrix[name]
               if target_name not in seen
          ], default=happiness_matrix[start_name][name] if start_name != name else 0)
          seen.pop()
          return max_happiness
     return dfs(start_name)

assert get_maximum_happiness(test_matrix) == 330
print(get_maximum_happiness(full_matrix))
print(get_maximum_happiness(full_matrix_with_self))
