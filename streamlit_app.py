import streamlit as st

st.set_page_config(page_title="CGPA Calculator", page_icon="🎓")

st.title("CGPA Calculator")
st.write("A clean tool for students to calculate their results accurately.")

# 1. User Inputs for Scale and Number of Courses
col1, col2 = st.columns(2)
with col1:
    scale = st.selectbox("Select Institution Scale", [5, 4], help="5 for Universities, 4 for Polytechnics/Colleges")
with col2:
    num_courses = st.number_input("How many courses?", min_value=1, max_value=20, value=5)

total_points = 0.0
total_units = 0.0

st.divider()

# 2. Dynamic Inputs for Courses
st.subheader("Enter Course Details")
for i in range(int(num_courses)):
    c1, c2 = st.columns([2, 1])
    with c1:
        grade_point = st.number_input(f"Grade Point (Course {i+1})", min_value=0.0, max_value=float(scale), step=0.5, key=f"gp_{i}")
    with c2:
        unit = st.number_input(f"Units (Course {i+1})", min_value=1.0, max_value=6.0, step=1.0, key=f"unit_{i}")
    
    total_points += (unit * grade_point)
    total_units += unit

# 3. Calculation and Results
if st.button("Calculate CGPA", type="primary"):
    if total_units > 0:
        cgpa = total_points / total_units
        st.balloons()
        st.metric(label="Your Final CGPA", value=f"{cgpa:.2f} / {scale}.0")
        
        # Determine Classification
        if scale == 5:
            if cgpa >= 4.5: remark = "First Class"
            elif cgpa >= 3.5: remark = "Second Class (Upper)"
            elif cgpa >= 2.4: remark = "Second Class (Lower)"
            else: remark = "Pass"
        else:
            if cgpa >= 3.5: remark = "Distinction"
            elif cgpa >= 3.0: remark = "Upper Credit"
            else: remark = "Lower Credit/Pass"
            
        st.success(f"**Remark:** {remark}")
    else:
        st.error("Please ensure total units are greater than zero.")