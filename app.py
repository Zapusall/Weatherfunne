
import streamlit as st
from datetime import date
from plotly import graph_objs as go
import requests
import json
import itertools

ls = []

@st.cache
def load_data(city):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f4f19cae7d4100d1cceb1599f25c750e&units=imperial").json()

data = [x for y in list(json.load(open('cities.json')).values()) for x in y]

selected_city = st.selectbox("Select a city", data)

st.write(load_data(selected_city)['main'])
ls.append(selected_city)
st.write(ls)
