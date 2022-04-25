
import streamlit as st
from datetime import date
from plotly import graph_objs as go
import requests
import json
import itertools

if 'ls' not in st.session_state:
	st.session_state.ls = {}

	
@st.cache
def load_data(city):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c5b4fbf9aaaa4bac56566ff54253c658&units=imperial").json()

data = [x for y in list(json.load(open('cities.json')).values()) for x in y]

selected_city = st.selectbox("Select a city", data)
loaded = load_data(selected_city)['main']
st.session_state.ls[selected_city] = loaded
st.table(loaded)
