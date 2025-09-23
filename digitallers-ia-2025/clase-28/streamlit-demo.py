import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "mes" : ["Enero", "Febrero", "Marzo", "Abril"],
    "ventas" : [100, 200, 300, 400]
})

st.line_chart(df.set_index("mes"))