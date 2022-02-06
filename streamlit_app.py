import streamlit as st


def to_do(st_commands, checkbox_id):
    cols = st.columns((1, 20))
    done = cols[0].checkbox(" ", key=checkbox_id)
    if done:
        for (cmd, *args) in st_commands:
            with cols[1]:
                if cmd == st.write:
                    text = args[0]
                    cols[1].write(
                        f"<s style='color: #888'> {text} </s>",
                        unsafe_allow_html=True,
                    )
                else:
                    if cmd in (
                        st.slider,
                        st.button,
                        st.checkbox,
                        st.time_input,
                        st.color_picker,
                        st.selectbox,
                        st.camera_input,
                        st.radio,
                        st.date_input,
                        st.multiselect,
                        st.text_area,
                        st.text_input,
                    ):
                        cmd(*args, disabled=True)
                    else:
                        cmd(*args)

    else:
        for (cmd, *args) in st_commands:
            with cols[1]:
                if cmd == st.write:
                    st.write(*args, unsafe_allow_html=True)
                else:

                    cmd(*args)
    st.write("")
    return done


st.title("☑️ Meet `stodo`, your Streamlit to-do")
"""Introducing `stodo` so you can create to do items in Streamlit! Here's how it looks like:"""

with st.echo():
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
