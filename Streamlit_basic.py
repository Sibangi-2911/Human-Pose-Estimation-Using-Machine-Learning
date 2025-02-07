import streamlit as st
st.title("Text Elements")
st.header("Header in Streamlit")
st.subheader("Subheadser in Streamlit")
st.markdown("**AskPython** is an awesomewebsite!")
st.markdown("Visit _askpython.com_ to learn from various ")
code = '''
def add(a,b):
print("a+b = ",a+b)
'''
st.code(code,language='python')
st.latex('''
(a+b)^2 = a^2 + b^2 + 2*a*b
''')
