import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Ashwath's Portfolio",
                   layout="wide", page_icon="👨🏾‍🍳")

# ---- HEADER ----
# st.markdown("<h1 style='text-align: center;'>Welcome to Ashwath's Portfolio 👋</h1>", unsafe_allow_html=True)
# st.write("---")

# ---- SUMMARY ----
st.subheader("✔️ Summary")
st.write("""
A Computer Science graduate with five years of experience as a **Software Engineer**.  

I am particularly drawn to roles involving impactful projects in Software Engineering, Full-stack Development, Backend Development, 
Security Analytics & AI research, and Application Security.
""")

# ---- SKILLS ----
st.subheader("👨🏾‍🍳 Skills")
st.markdown("""
- **Languages**: Java, Python, Golang, Bash  
- **Databases**: PostgreSQL, Redis, Apache Hadoop  
- **Graphics/Math**: OpenGL, MATLAB (Computer Vision)  
- **Deep Learning**: Keras, TensorFlow  
- **Security Tools**: Nmap, Nessus, Wireshark, Metasploit, Snyk, Invicti, Nikto, SQLMap  
- **Cloud & DevOps**: GCP, Docker, CircleCI, Git, Splunk, API Security  
""")

# ---- EDUCATION ----
st.subheader("🎓 Education")
st.write("**MS in Computer Science**, minor in Big Data from Rochester Institute of Technology, May 2024")

# ---- EXPERIENCE ----
st.subheader("🎻 Work Experience")
with st.expander("Security Engineer Intern @ Infinitus AI (Silicon Valley AI Startup, 2022 & 2023)"):
    st.write("Worked on Application Security, Vulnerability Management, and AI Security-related projects in San Francisco.")

with st.expander("Senior Software Engineer, Security @ CGI Global, Bangalore (2017-2021)"):
    st.write("Worked on Penetration Testing, Vulnerability Assessments, Secure Code Reviews, and Cloud Security.")

# ---- LINKS ----
st.subheader("🖇️ Links to My Work")
st.markdown("""
- [GitHub](https://github.com/ashwathhalemane)  
- [PentesterLab](https://pentesterlab.com/profile/)  
- [Leetcode](https://leetcode.com/u/ash_wattha)  
- [CodeChef](https://www.codechef.com/users/ashwathhalemane)  
- [Email](mailto:ah7387@rit.edu)  
- [LinkedIn](https://www.linkedin.com/in/ashwath-s-halemane/)  
""")

# ---- PROJECTS ----
st.subheader("📽️ Projects")

tab1, tab2 = st.tabs(["Academic Projects", "Personal Projects"])

with tab1:
    with st.expander("Web Services and Service Oriented Architecture"):
        st.write("Built a MongoDB-based query system for APIs and Mashups.")
        st.markdown(
            "[GitHub Repo](https://github.com/ashwathhalemane/CSCI-724-PA3)")
    with st.expander("Computer Graphics"):
        st.markdown("""
        - Rasterization: [Link](https://ashwathhalemane.github.io/CSCI610-Assignment2)  
        - Barycentric Interpolation: [Link](https://ashwathhalemane.github.io/CSCI610-Assignment3)  
        - Tessellation: [Link](https://ashwathhalemane.github.io/CSCI610-Assignment4/assn4-tessellation.html)  
        - Textures: [Link](https://ashwathhalemane.github.io/csci610-assn7/assn7-textures.html)  
        """)
    with st.expander("Computer Vision"):
        st.write("Worked on image manipulation, segmentation, convolution, and a DL-based cotton field irrigation classifier.")
        st.markdown(
            "[Repos](https://github.com/ashwathhalemane/CSCI-631-Computer-Vision)")

with tab2:
    with st.expander("MEAN Stack Blog Application"):
        st.markdown("[Frontend Angular App](https://github.com/ashwathhalemane/Angular-7-Blog-App-) | [Backend API](https://github.com/ashwathhalemane/REST-API-Blog-app)")
        st.write(
            "Includes security fixes for XSS and SQL Injection using Snyk + SonarCloud.")
    with st.expander("Cybersecurity Projects"):
        st.markdown(
            "[CTFs & Security Tools](https://github.com/ashwathhalemane/hacking-exercise)")
    with st.expander("Android Catalog App"):
        st.markdown(
            "[Explore here](https://phoneky.com/android/?id=d1d169677)")

# ---- COURSES ----
st.subheader("✔️ Relevant Courses")
with st.expander("Data Structures and Algorithms"):
    st.write("""
    - Divide & Conquer, Greedy, Dynamic Programming  
    - Graph Algorithms (MST, Shortest Paths, Network Flow)  
    - Theory of Computation, OOP, Computational Problem Solving  
    """)

with st.expander("Data Science"):
    st.write("""
    - Big Data (IMDB dataset, COVID crime analysis)  
    - Web Services (classification + clustering of services)  
    - Database System Implementation (H2 feature development)  
    - Foundations of Computer Vision  
    """)

with st.expander("Cybersecurity & Distributed Systems"):
    st.write("""
    - Cryptography, Foundations of Cybersecurity (RBAC for healthcare, fuzzing, OSS security, XS-leaks)  
    - Distributed Systems  
    """)

with st.expander("Computer Graphics"):
    st.write(
        "Foundations of Graphics, Rasterization, Interpolation, Tessellation, Textures.")

st.write("---")
st.success("🚀 Thanks for visiting my portfolio!")
