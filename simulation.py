students = ["S1","S2","S3","S4","S5","S6","S7","S8"]
arrival_times = [0,2,4,5,9,12,14,18]
# service_times = [4,3,5,2,4,3,2,4]
service_times = [5,4,6,3,5,4,3,5]

service_start = []
completion_time = []
waiting_time = []
time_in_system = []

previous_completion = 0

for i in range(len(students)):
    start = max(arrival_times[i], previous_completion)
    completion = start + service_times[i]
    wait = start - arrival_times[i]
    system_time = completion - arrival_times[i]

    service_start.append(start)
    completion_time.append(completion)
    waiting_time.append(wait)
    time_in_system.append(system_time)
    previous_completion = completion

    print("Student:", students[i])
    print("Arrival Time:", arrival_times[i])
    print("Service Start:", start)
    print("Completion Time:", completion)
    print("Waiting Time:", wait)
    print("Time in System:", system_time)
    print("-" * 30)

average_wait = sum(waiting_time) / len(waiting_time)
maximum_wait = max(waiting_time)
average_system_time = sum(time_in_system) / len(time_in_system)
number_waited = sum(1 for w in waiting_time if w > 0)
percentage_waited = (number_waited / len(waiting_time)) * 100
print("Average Waiting Time:", average_wait)
print("Maximum Waiting Time:", maximum_wait)
print("Average Time in System:", average_system_time)
print("Number of Students Who Waited:", number_waited)
print("Percentage of Students Who Waited:", percentage_waited)