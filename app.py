import streamlit as st
import pandas as pd
import os

# Filepath to store feedback
FEEDBACK_FILE = "feedback.csv"
def main():
    st.title("Deepak Prasad Shah's Portfolio")
    st.subheader("An Interactive Portfolio")
    st.write("Welcome to my portfolio! Here you can find information about my projects, skills, and how to contact me.")
    st.sidebar.title("Navigation")
    
    # Dictionary mapping page names to their respective functions
    pages = {
        "Home": home,
        "About Me": about_me,
        "Education": education,
        "Skills": skills,
        "Experience": experience,
        "Certifications": certifications,
        "Achievements": achievements,
        "Publications": publications,
        "Projects": projects,
        "Contact": contact
    }
    
    # Sidebar navigation
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()  # Call the selected page function

# Define the individual page functions
def home():
    st.write("This is the home page of my interactive portfolio. Explore my work and get to know me!")
    st.write("I'm a Computer Science student at Chandigarh University with a passion for innovation and problem-solving. I’m currently working on four upcoming patents in the fields of IoT and smart systems, showcasing my drive to create meaningful tech solutions. With hands-on experience in Python, C/C++, HTML, and CSS, I love building interactive applications — from IoT-based automation to web-powered portfolios. I’m also diving deeper into AI, machine learning, and data visualization using tools like Streamlit. Welcome to my digital space — feel free to explore my work!")

def about_me():
    st.header("About Me")
    st.write("""
## 💼 About Me

Hello! I'm **Deepak Prasad Shah**, currently pursuing my Bachelor's in Computer Science and Engineering at **Chandigarh University**. Beyond just academics and technical skills, I believe in the power of leadership, communication, and teamwork — values that have shaped me into who I am today.

### 🏆 Leadership Journey

My leadership journey took off during my **12th grade**, when I was honored to serve as the **House Leader**. With determination, team spirit, and clear communication, I led my house to become the **Best House of the Year** — an achievement that still fills me with pride. That experience taught me how to **motivate a team**, set shared goals, and adapt under pressure — lessons I carry with me even today.

At Chandigarh University, I’ve continued to grow as a leader. As an active member of **CUNSS (Chandigarh University Nepali Students Society)**, I successfully **organized two major events**, coordinating with multiple teams and managing everything from planning to execution. These opportunities have deepened my sense of **responsibility** and **social commitment**.

### 🤝 People & Team Skills

I'm someone who **connects easily with people**, no matter their background. Whether I’m collaborating on a group project, managing an event, or just helping a peer, I value clear communication, mutual respect, and genuine engagement.

I’m often told I’m the kind of person who **brings people together** and keeps the energy positive. It’s one of the reasons I enjoy **teamwork and coordination** — because when a group works in sync, great things happen.

## 🌱 Looking Ahead

I'm excited to continue growing as a responsible leader and a tech enthusiast. Whether it's through developing innovative tech solutions or organizing impactful social events, I strive to make a meaningful contribution — both in my community and in the world of technology.
""")


def education():
    st.header("Education")
    st.write("""
## 🎓 Education

### 📘 Class 10 — Modern Indian School, Chovar, Kathmandu  
I completed my Class 10 from **Modern Indian School**, Chovar, Kathmandu, with a score of **90.6%**. This phase built a solid academic base for me and nurtured my interest in science and technology. It was during these years that I developed a structured way of thinking and a deep curiosity about how things work.

### 📗 Class 11 & 12 — Kendriya Vidyalaya, Embassy of India, Kathmandu  
I pursued my higher secondary education at **Kendriya Vidyalaya, Embassy of India, Kathmandu**, and secured **85%** in Class 12. These years were transformative — I was selected as the **House Leader** and led my house to win the **Best House Award**. I also had the opportunity to organize **two major events under CUNSS**, which helped me gain real experience in planning, communication, and teamwork.

However, this phase also came with challenges. Despite **Chemistry** being one of my favorite subjects, I struggled with it in 11th grade. Until then, I had rarely faced failure — so this was a moment of personal growth. It taught me how to **deal with setbacks**, **bounce back**, and develop resilience. That experience made me stronger and more self-aware, both academically and emotionally.

### 🎓 Bachelor's — Chandigarh University  
Currently, I’m pursuing my **Bachelor’s in Computer Science and Engineering** at **Chandigarh University**. My time here has been dynamic and full of exploration — I've made valuable connections, worked on exciting projects, and discovered new areas of interest.

I've applied for **four patents** as part of my innovation journey:
- A **fully automated anti-drone system** operating in the 2.4GHz band  
- A **MOSFET-type suggestion mechanism**  
- A **solar panel cleaning device**  
- A **mechanical lifting mechanism**

These projects reflect my strong grip over **electronics, electrical systems**, and even **mechanical concepts**. I love bridging hardware with software to solve real-world problems creatively and efficiently.
""")



def skills():
    st.header("Skills")
    st.write("""
- **Python**: Proficient in Python with hands-on experience developing complete backend systems like a Hotel Management System and a Matrix Manipulation System. Contributed to various IT-Hardware-AI integration projects involving data visualization, automation, and AI logic implementation. Comfortable with both scripting and modular programming.

- **MySQL**: Applied MySQL databases in real-world applications such as Hotel Management Systems (HMS), Matrix Manipulation Systems (MMS), and School Management Systems. Skilled in designing relational databases, writing optimized queries, and integrating MySQL with backend services.

- **C/C++**: Strong foundation in C and C++ from academic coursework, with a focus on Object-Oriented Programming (OOP), Data Structures and Algorithms (DSA). Regularly solve algorithmic problems on platforms like LeetCode, building analytical and logical thinking skills.

- **IoT (Internet of Things)**: Expert in IoT systems design and hardware-software integration. Skilled in working with sensors, microcontrollers (like ESP32), and real-time data monitoring. Successfully built and deployed IoT-based solutions for home automation and system control.

- **FEDE & Semiconductor Physics**: Advanced understanding of Fundamental Electronics and Device Engineering (FEDE) and Semiconductor Physics. Able to bridge theoretical concepts with practical circuit design and behavior analysis.

- **HTML & CSS**: Strong grasp of web fundamentals. Capable of building responsive static websites with clean design principles and well-structured HTML/CSS code. Familiar with front-end basics used in prototyping and UI design.

- **Leadership**: Proven leadership capabilities through project work and event organization. Known for motivating teams, delegating responsibilities smartly, and ensuring goals are achieved even with less active team members.

- **Communication**: A+ grade in college communication assessments. An experienced public speaker and anchor at major institutional events. Excellent at presenting ideas clearly, hosting programs, and representing groups confidently.

- **Team Management**: Demonstrated ability to manage teams under tight deadlines. Adaptable, approachable, and results-driven. Helped diverse groups stay coordinated and productive even under pressure.

- **Maturity**: Recognized for mature decision-making and calm demeanor. Handle responsibilities with seriousness and empathy, balancing personal growth with team development.
""")


def experience():
    st.header("Experience")
    st.write("Information about my professional experience.")

def certifications():
    st.header("Certifications")
    st.write("Certifications I have earned.")

def achievements():
    st.header("Achievements")
    st.write("Highlights of my achievements.")

def publications():
    st.header("Publications")
    st.write("Details about my published work.")

def projects():
    st.header("Projects")
    st.write("""

- **Hotel Management System (HMS) – Full Backend in Python & MySQL**  
  A robust command-line based hotel management system that handles room bookings, check-ins/outs, billing, and guest records. Implemented full CRUD operations, user authentication, and database integration using MySQL. Designed to be modular and scalable with reusable Python modules.

- **Matrix Manipulation System (MMS) – Python with GUI/CLI**  
  Developed a Python-based system for performing various matrix operations like addition, subtraction, multiplication, transposition, and determinant calculation. Emphasized data structure design and algorithm efficiency. Included options for both GUI (Tkinter) and command-line interfaces.

- **School Management System – Python + MySQL**  
  Built a centralized database-driven system for managing students, teachers, classes, and fee records. Includes features like attendance tracking, grading, and role-based access. MySQL used as the backend to store and retrieve structured data with optimized query performance.

- **IoT Home Automation System – ESP32 + Sensors + Python Dashboard**  
  Designed and deployed a complete home automation solution using ESP32 microcontrollers. Integrated sensors (temperature, motion, light), actuators (relays, motors), and real-time data monitoring through a custom Python dashboard. Supported mobile and web alerts using APIs and MQTT.

- **AI Data Visualization Toolkit – Python (Matplotlib, Seaborn, Plotly)**  
  Developed a set of reusable Python scripts and modules to visualize complex datasets used in AI/ML projects. Included support for regression visualization, classification boundary plots, correlation heatmaps, and time-series trends. Focused on clarity, interactivity, and performance.

- **FEDE/SC Physics Simulation Models – Python + Mathematical Libraries**  
  Created simulation tools for visualizing semiconductor behaviors and basic electronic circuits. These models helped in understanding carrier movement, depletion regions, PN junction behavior, and device switching using NumPy and Matplotlib.

- **IT-HW-AI Integration Experiments**  
  Series of projects integrating hardware and AI such as gesture recognition using sensors, real-time monitoring using ML-powered cameras, and alert-based automation systems. Explored interaction between hardware triggers and AI logic.

- **Mini Web Front-End Designs – HTML & CSS**  
  Developed several static web templates showcasing basic UI components, responsive layouts, and styling elements. Used to demonstrate understanding of layout design, element positioning, and aesthetic consistency.

- **College Event Anchoring & Leadership Campaigns**  
  While not a tech project, planned and hosted various institutional events and campaigns, involving scripting, managing schedules, and leading teams under pressure. These strengthened soft skills and showcased real-world application of leadership and communication.
""")

def contact():
    st.header("Contact")
    st.write("""
## 📞 Contact

### 📧 Email : \ndeepakprasadshah@yahoo.com, 24bcs12705@cuchd.in

### 📱 Phone
+091 828899759\n
+977 9761704176

### 📍 Location
Kathmandu, Nepal \n
Chandigarh, India

### 🕒 Availability
Open to work on new projects or collaborations. Feel free to reach out anytime!
""")
# Run the app
if __name__ == "__main__":
    main()