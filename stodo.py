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
                        f"<s style='color: rgba(49, 51, 63, 0.4)'> {text} </s>",
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
