'''import streamlit as st
st.title("hello world")
st.write("this is my first streamlit app")
st.write("The current time is:", __import__("datetime").datetime.now())
st.write("This is a simple line of text.")
st.write("You can also write numbers:", 42)
st.title("Dashboard Title")           # Largest — use once per page
st.header("Section Header")           # Major section divider
st.subheader("Subsection")            # Minor section divider
st.text("Fixed-width plain text")     # Monospace, like terminal output
st.caption("Small grey caption text") # Small annotation below charts or images
st.markdown("**Bold**, *italic*, and `code` using standard Markdown syntax")
st.markdown("---")                    # Horizontal divider line
st.code("""
def hello():
   return "This renders as a code block with syntax highlighting"
""", language="python")
'''
import streamlit as st
import pandas as pd


# Create two equal-width columns


col1, col2 = st.columns(2)


with col1:
   st.subheader("Left Column")
   st.write("Any content placed inside this block appears on the left.")
   st.metric(label="Total Sales", value="$48,200", delta="+12%")
   # st.metric shows a number with an optional delta (change indicator)


with col2:
   st.subheader("Right Column")
   st.write("This content appears on the right, at the same vertical level.")
   st.metric(label="Active Users", value="1,284", delta="-3%")

import streamlit as st
import pandas as pd
import seaborn as sns


df = sns.load_dataset("tips")


# Method 1: st.write() — quick, automatic


st.subheader("Method 1: st.write()")
st.write(df.head(5))


# Method 2: st.dataframe() — interactive, sortable, scrollable


st.subheader("Method 2: st.dataframe() — Interactive Table")
st.dataframe(df.head(10), use_container_width=True)


# use_container_width=True stretches the table to fill the full page width


# Method 3: st.table() — static, compact, best for small summary tables


st.subheader("Method 3: st.table() — Static Table")
st.table(df.groupby("day")["total_bill"].mean().round(2))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")


# Matplotlib / Seaborn charts


st.subheader("Bill Distribution by Day")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x="day", y="total_bill", ax=ax, palette="muted")
ax.set_xlabel("Day of Week")
ax.set_ylabel("Total Bill ($)")
plt.tight_layout()
st.pyplot(fig)          # Pass the figure object directly
plt.close(fig)          # Always close after — prevents memory buildup in Streamlit





# The widget renders on the page AND returns the current value


user_name = st.text_input("Enter your name")


# Use the value immediately below


st.write(f"Hello, {user_name}!")

# inputs_demo.py


import streamlit as st
import pandas as pd
import seaborn as sns


st.title("Input Widgets Demo")


df = sns.load_dataset("tips")


# 1. Text input — free-form string


search_term = st.text_input("Search by day (Sun, Sat, Fri, Thur):", value="Sun")


# value= sets the default text shown on page load


# 2. Number input — constrained numeric entry


min_bill = st.number_input(
   "Minimum bill amount ($):",
   min_value=0.0,
   max_value=float(df["total_bill"].max()),
   value=10.0,
   step=1.0
)


# min_value and max_value prevent invalid entries


# step= controls the increment when clicking the +/- buttons


# 3. Selectbox — dropdown, one choice


meal_time = st.selectbox(
   "Filter by meal time:",
   options=["All", "Lunch", "Dinner"]


)


# 4. Multiselect — dropdown, multiple choices allowed


days_selected = st.multiselect(
   "Select days to include:",
   options=df["day"].unique().tolist(),
   default=df["day"].unique().tolist()   # All selected by default


)


# 5. Slider — range selection


tip_range = st.slider(
   "Filter by tip amount ($):",
   min_value=float(df["tip"].min()),
   max_value=float(df["tip"].max()),
   value=(1.0, 8.0)   # Tuple creates a range slider with two handles
)


# Apply all filters to the DataFrame


filtered = df[
   (df["total_bill"] >= min_bill) &
   (df["day"].isin(days_selected)) &
   (df["tip"] >= tip_range[0]) &
   (df["tip"] <= tip_range[1])
]


if meal_time != "All":
   filtered = filtered[filtered["time"] == meal_time]


# Display results


st.subheader(f"Filtered Results: {len(filtered)} rows")


st.dataframe(filtered, use_container_width=True)

import streamlit as st
import pandas as pd
import seaborn as sns


df = sns.load_dataset("tips")


# Checkbox — boolean toggle


show_raw_data = st.checkbox("Show raw data table", value=False)
if show_raw_data:
   st.dataframe(df)


# Radio — mutually exclusive choice, displayed as visible buttons


chart_type = st.radio(
   "Choose chart type:",
   options=["Bar Chart", "Box Plot", "Scatter Plot"],
   horizontal=True    # Display options side by side instead of stacked
)


st.write(f"You selected: {chart_type}")





import streamlit as st
import pandas as pd
import seaborn as sns


df = sns.load_dataset("tips")
st.subheader("Generate Report")


if st.button("Run Analysis"):
   # This block only executes the moment the button is clicked
   st.success("Analysis complete.")


  


   col1, col2 = st.columns(2)
   col1.metric("Average Bill", f"${df['total_bill'].mean():.2f}")
   col2.metric("Average Tip", f"${df['tip'].mean():.2f}")


   st.dataframe(df.describe().round(2), use_container_width=True)









