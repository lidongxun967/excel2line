import streamlit as st
import pandas as pd

st.set_page_config("Excel转折线图",layout="wide",page_icon="♾️")
st.title('Excel转折线图')


upf = st.file_uploader('导入excel文件',type=['xlsx','xls'])

if not upf:
    st.stop()

try:
    dfs = pd.read_excel(upf,None)
except :
    st.toast("文件格式错误！",icon="❗")
    st.stop()

names = list(dfs.keys())

tabs = st.tabs(names)



for tab,name in zip(tabs,names):
    with tab:
        df = dfs[name]
        st.line_chart(df)

