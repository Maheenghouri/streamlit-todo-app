import streamlit as st


def add_bg():
    bg_img = "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(20, 20, 20, 0.75), rgba(20, 20, 20, 0.75)), 
                        url({bg_img}) no-repeat center center fixed;
            background-size: cover;
        }}
        .task-container {{
            background: rgba(255, 255, 255, 0.10);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
            margin-bottom: 15px;
        }}
        .sidebar .sidebar-content {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 1.2rem;
            border-radius: 12px;
            color: white;
        }}
        .stButton>button {{
            background-color: #444;
            color: white;
            border-radius: 8px;
            border: 1px solid #666;
            padding: 10px;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #666;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

st.title("📝 TO-DO LIST ")


if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None 

st.sidebar.header("💼 WorkSpace")
new_task = st.sidebar.text_input("➕ Add Task:", placeholder="Type your task here...")

if st.sidebar.button("✔ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.sidebar.success("Task added successfully!")
    else:
        st.sidebar.warning("Task cannot be empty!")

st.markdown("<div class='task-container'>", unsafe_allow_html=True)
st.subheader("🗂 Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks added yet! Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

      
        completed = col1.checkbox(f" {task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

     
        if col2.button("✏ Edit", key=f"edit_{index}"):
            st.session_state.edit_index = index
            st.rerun() 
        
        if col3.button("🗑 Remove", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.rerun()  
if st.session_state.edit_index is not None:
    edit_index = st.session_state.edit_index
    edited_task = st.text_input("Edit Task", st.session_state.tasks[edit_index]["task"], key="edit_task_input")

    save_col, cancel_col = st.columns([0.5, 0.5])
    
    if save_col.button("💾 Save", key="save_task"):
        if edited_task.strip():
            st.session_state.tasks[edit_index]["task"] = edited_task  
            st.session_state.edit_index = None   
            st.rerun()  
    if cancel_col.button("❌ Cancel", key="cancel_edit"):
        st.session_state.edit_index = None   
        st.rerun() 
if st.button("🚮 Clear All Tasks"):
    st.session_state.tasks = []
    st.session_state.edit_index = None   
    st.success("All tasks deleted successfully!")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("🎯 Stay focused & achieve more with this elegant To-Do App! 🚀")
