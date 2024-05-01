import time
import streamlit as st

students = {
    "std1": {"name": "Arun", "image": "Frndz/images/arun.jpg", "votes": 0},
    "std2": {"name": "Alan", "image": "Frndz/images/alan.jpg", "votes": 0},
    "std3": {"name": "abel", "image": "Frndz/images/abel.jpg", "votes": 0},
    "std4": {"name": "baaes", "image": "Frndz/images/baaes.jpg", "votes": 0},
    "std5": {"name": "Aaron", "image": "Frndz/images/aaron.jpg", "votes": 0},
    "std6": {"name": "ajay", "image": "Frndz/images/ajay.jpg", "votes": 0},
}

valid_students = list(students.keys())


def get_two_unique_random_students():
    """
    This function ensures two randomly chosen students are unique using time-based pseudo-randomness.
    """
    current_time = time.time_ns()  # Get nanosecond timestamp
    student1_index = int(current_time % len(valid_students))
    student2_index = (student1_index + 1) % len(valid_students)  # Ensure different index

    return valid_students[student1_index], valid_students[student2_index]


student1, student2 = get_two_unique_random_students()
student1_data = students[student1]
student2_data = students[student2]


def voting(chosen_student):
    """
    Updates the vote count for the chosen student and displays a confirmation message.
    """
    students[chosen_student]["votes"] += 1
    st.success(f"You voted for {students[chosen_student]['name']}!")


tab1, tab2 = st.tabs(["Vote", " Rank"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.header(student1_data["name"])
        st.image(student1_data["image"], width=200)
        if st.button(f"Vote for {student1_data['name']}"):
            voting(student1)

    with col2:
        st.header(student2_data["name"])
        st.image(student2_data["image"], width=200)
        if st.button(f"Vote for {student2_data['name']}"):
            voting(student2)

with tab2:
    # Directly iterate through the original students dictionary for ranking display
    for student_name, student_data in students.items():
        st.write(f"{student_data['name']} {student_data['votes']}")
