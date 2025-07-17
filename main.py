import streamlit as st
st.title("Hii I am Adhi!")
st.header("B.Tech")
st.subheader("AI&DS")
st.text("I am from PDKT i am python developer")
st.markdown("**Hiii** *frds*")
st.markdown("---")
st.caption("4th year student")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
js={"a":"1,2,3","b":"4,5,6"}
st.json(js)
st.markdown("---")
cd="""
print("Hellow world")
def fun():
    return 0;
"""
st.code(cd, language = "python")
