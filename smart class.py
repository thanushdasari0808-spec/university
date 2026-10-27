# Smart Classroom Timetable Allocation

courses = [
    ("Python", 40, "Monday", "9AM"),
    ("Maths", 30, "Monday", "9AM"),
    ("English", 25, "Monday", "10AM")
]

rooms = [
    ("Room A", 35),
    ("Room B", 50)
]

schedule = []
clashes = False

for course, students, day, period in courses:
    allocated = False

    for room, capacity in rooms:
        if capacity >= students:
            conflict = False

            for item in schedule:
                if item[1] == room and item[2] == day and item[3] == period:
                    conflict = True

            if not conflict:
                schedule.append((course, room, day, period))
                print(course, "allocated to", room, day, period)
                allocated = True
                break

    if not allocated:
        print("Cannot allocate:", course)
        clashes = True

print("\n--- Final Timetable ---")

for item in schedule:
    print(item)

if clashes:
    print("Some courses could not be accommodated.")
else:
    print("All courses accommodated successfully.")
