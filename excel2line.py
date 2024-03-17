import streamlit as st
import pandas as pd

st.title('数据分析')

upf = st.file_uploader('导入excel文件',type=['xlsx','xls'])

if not upf:
    st.stop()
    
dfs = pd.read_excel(upf,None)

names = list(dfs.keys())

tabs = st.tabs(names)

for tab,name in zip(tabs,names):
    with tab:
        df = dfs[name]
        st.line_chart(df)

