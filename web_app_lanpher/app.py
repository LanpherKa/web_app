#This is a starting template please change the comments
import streamlit as st
import backend


st.set_page_config(page_title="Illegal Dumping in Philadelphia", layout="wide")

#link views on other python scripts
overview = st.Page("views/overview.py", title="Overview", icon="🙂", default=True)
analytics = st.Page("views/analytics.py", title="Data Analytics", icon="🙂")
resources = st.Page("views/resources.py", title="Resources", icon="🙂")

#navigation bar
pg = st.navigation([overview, analytics, resources])

#run the pages
pg.run()