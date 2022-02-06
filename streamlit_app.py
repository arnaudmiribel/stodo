import streamlit as st

from stodo import to_do

st.title("☑️ Meet `stodo`, your Streamlit to-do")
"""Introducing `stodo` so you can create to do items in Streamlit!"""

"""## My to-do today"""
to_do(
    [(st.write, "☕ Take my coffee")],
    "coffee",
)
to_do(
    [(st.write, "🥞 Have a nice breakfast")],
    "pancakes",
)
to_do(
    [(st.write, ":train: Go to work!")],
    "work",
)

"""## How to use it?

Here's how you can create a Streamlit to-do"""


with st.echo():
    from stodo import to_do

    to_do([(st.write, "Here's a first item")], "first_to_do")

"""Checking the to-do will strike all the text that can be found! Try it out below:"""
with st.echo():
    to_do(
        [
            (st.write, "Check that box..."),
            (st.write, "And you will see how everything..."),
            (st.write, "Gets striked! ⚡"),
        ],
        "second_to_do",
    )

"""You can also make more complex to-dos with other Streamlit commands hidden inside! 

See how Streamlit widgets also gets disabled? """

with st.echo():
    to_do(
        [
            (st.write, "Here's a second, more complex item"),
            (st.slider, "Choose a value", 0, 50),
            (st.text_area, "Something else to say?"),
        ],
        "third_to_do",
    )
