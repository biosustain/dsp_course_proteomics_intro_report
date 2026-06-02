import os
import time

import psutil
import streamlit as st

st.set_page_config(layout="wide",
                   page_title="Report")

st.markdown(
    '''
    <h1 style='text-align: center;
    color: #023858;'>
    Report
    </h1>
    ''',
    unsafe_allow_html=True)


sections_pages = {}
homepage = st.Page('Home/Homepage.py', title='Homepage')
sections_pages['Home'] = [homepage]

Clustermap = st.Page('Data/Clustermap.py', title='Clustermap')
Completeness = st.Page('Data/Completeness.py', title='Completeness')
sections_pages['Data'] = [Clustermap, Completeness]

Differential_Regulation_overview = st.Page('Differential_Regulation/0_overview_differential_regulation.py', title='Overview Differential Regulation')
sections_pages['Differential Regulation'] = [Differential_Regulation_overview]

Maltose_Uptake_overview = st.Page('Maltose_Uptake/0_overview_maltose_uptake.py', title='Overview Maltose Uptake')
sections_pages['Maltose Uptake'] = [Maltose_Uptake_overview]

Uniprot_Annotations_overview = st.Page('Uniprot_Annotations/0_overview_uniprot_annotations.py', title='Overview Uniprot Annotations')
sections_pages['Uniprot Annotations'] = [Uniprot_Annotations_overview]

report_nav = st.navigation(sections_pages)

# Following https://discuss.streamlit.io/t/close-streamlit-app-with-button-click/35132/5
exit_app = st.sidebar.button("Shut Down App",
                             icon=":material/power_off:",
                             use_container_width=True)
if exit_app:
    st.toast("Shutting down the app...")
    time.sleep(1)
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()


report_nav.run()
