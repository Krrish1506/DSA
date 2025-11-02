'''
There are 4 people (A, B, C, and D) who want to cross a bridge at night.

A, B, C and D take 1, 2, 5 and 8 minutes respectively to cross the bridge.
There is only one torch with them, and the bridge cannot be crossed without the torch.
There cannot be more than two people on the bridge at any time, and when two people cross the bridge together, they must move at the slower person's pace.
Can they all cross the bridge in 15 minutes?
'''
people = {'A' : 1, 'B' : 2, 'C' : 5, 'D' : 8}
time_limit = 15

left = ['A', 'B', 'C', 'D']
right = []
total_time = 0

right.append('A')
right.append('B')
left.remove('A')
left.remove('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

left.append('A')
right.remove('A')
total_time+=people['A']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

left.remove('C')
left.remove('D')
total_time+=people['D']
right.append('C')
right.append('D')
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

right.remove('B')
left.append('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

right.append('A')
right.append('B')
left.remove('A')
left.remove('B')
total_time+=people['B']
print("Left side", left, "Right side", right, "time taken", total_time, "minutes")

if (total_time <= time_limit):
    print("All crossed bridge in", total_time, "minutes.")
else:
    print("Cannot be crossed in", time_limit, "took", total_time, "to cross the bridge.")