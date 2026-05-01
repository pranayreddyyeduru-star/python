# 1) Create input data (student_data):
#    a) A dictionary where each key is a student_id (id1, id2, ...).
#    b) Each value is another dictionary containing student details 
# (name, class, subject_integration).

# 2) Create result storage:
#    a) result = {} will store only unique student entries.
#    b) seen_keys = [] will store the unique identity 
# of each student already added.
#    - NOTE: A list is used here instead of a set, 
# so membership checking is slower.

# 3) Traverse each student entry:
#    a) Loop through student_data items (student_id, details).

# 4) Create a unique key for duplicate checking:
#    a) unique_key is a tuple of (name, class, subject_integration).
#    b) This tuple represents the “identity” of a student record.

# 5) Check for duplicates and store only unique entries:
#    a) If unique_key is not in seen_keys:
#       - append unique_key to seen_keys
#       - store this student in result using student_id as key.
#    b) If unique_key already exists, skip (duplicate record).

# 6) Print the final unique dictionary:
#    a) Loop through result items.
#    b) Print each student_id and its details line by line.
student_data = {

"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1

"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},

}
result={}
seen_keys = []
for student_id, details in student_data.items():
    unique_keys=(details["name"], details["class"], details["subject_integration"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id]=details
for k,v in result.items():
    print(k,":", v)