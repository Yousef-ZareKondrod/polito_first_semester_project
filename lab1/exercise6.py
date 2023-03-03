# In a scheduling program, we want to check whether two appointments overlap. For
# simplicity, appointments start at a full hour, and we use hours in the format 0-23h. The
# following pseudocode describes an algorithm that determines whether the appointment
# with start time start1 and end time end1 overlaps with the appointment with start time
# start2 and end time end2.
# If start1 > start2
#  s = start1
# Else
#  s = start2
# If end1 < end223
#  e = end1
# Else
#  e = end2
# If s < e
#  The appointments overlap.
# Else
#  The appointments don’t overlap.
# 1. Trace this algorithm with an appointment from 10–12 and one from 11–13, then
# with an appointment from 10–11 and one from 12–13.
# 2. Draw a flowchart for the algorithm.
# 3. Explain the algorithm functionality and verify if it is correct [R3.12]

start1 = input('please enter the first appointment start time:')
end1 = input('please enter the first appointment end time:')
start2 = input('please enter the second appointment start time:')
end2 = input('please enter the second appointment end time:')

if start1 > start2:
    s = start1
else:
    s = start2
if end1 < end2:
    e = end1
else:
    e = end2
if s < e:
    print('The appointments overlap.')
else:
    print('The appointments don’t overlap.')

# if the time enters around 0 it doesn't work correctly

# modified code


