import pandas as pd
import streamlit as st

students = {
    "std1": {"name": "Arun", "image": "Frndz/images/arun.jpg", "votes": 0},
    "std2": {"name": "Alan", "image": "Frndz/images/alan.jpg", "votes": 0},
    "std3": {"name": "abel", "image": "Frndz/images/abel.jpg", "votes": 0},
    "std4": {"name": "baaes", "image": "Frndz/images/baaes.jpg", "votes": 0},
    "std5": {"name": "Aaron", "image": "Frndz/images/aaron.jpg", "votes": 0},
    "std6": {"name": "ajay", "image": "Frndz/images/ajay.jpg", "votes": 0},
}

# Convert students dict to a Pandas DataFrame
df_students = pd.DataFrame.from_dict(students, orient='index')

def get_two_unique_random_students():
  """
  This function ensures two randomly chosen students are unique using Pandas sample function.
  """
  return df_students.sample(2).index.tolist()

# Get two random students
student1, student2 = get_two_unique_random_students()
student1_data = students[student1]
student2_data = students[student2]

def voting(chosen_student):
    """
    Updates the vote count for the chosen student and displays a confirmation message.
    """
    df_students.loc[chosen_student, "votes"] += 1
    students[chosen_student] = df_students.loc[chosen_student].to_dict()  # Update original dict
    st.success(f"You voted for {students[chosen_student]['name']}!")

# Rest of the code remains the same using st.tabs, st.columns etc.

with tab2:
    # Sort DataFrame by vote count (descending order)
    sorted_students = df_students.sort_values(by='votes', ascending=False)

    for student_name in sorted_students.index:
        student_data = sorted_students.loc[student_name].to_dict()
        st.write(f"{student_data['name']}: {student_data['votes']}")
