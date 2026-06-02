from pathlib import Path
import json
import requests
import streamlit as st
section_dir = Path(__file__).resolve().parent.parent

st.markdown(
    '''
    <h3 style='text-align: center;
    color: #023558;'>
    Clustermap
    </h3>
    ''',
    unsafe_allow_html=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Boxplot Log2 Unnormalized
    </h4>
    ''',
    unsafe_allow_html=True)

plot_file_path = (section_dir / '../../report/1_data/clustermap/boxplot_log2_unnormalized.png').resolve().as_posix()
st.image(plot_file_path, caption='', use_column_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Clustermap Ward
    </h4>
    ''',
    unsafe_allow_html=True)

plot_file_path = (section_dir / '../../report/1_data/clustermap/clustermap_ward.png').resolve().as_posix()
st.image(plot_file_path, caption='', use_column_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Clustermap Ward Median
    </h4>
    ''',
    unsafe_allow_html=True)

plot_file_path = (section_dir / '../../report/1_data/clustermap/clustermap_ward_median.png').resolve().as_posix()
st.image(plot_file_path, caption='', use_column_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Cv Vs Mean
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../report/1_data/clustermap/cv_vs_mean.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

footer = '''
<style type="text/css">
.footer {
    position: relative;
    left: 0;
    width: 100%;
    text-align: center;
}
</style>
<footer class="footer">
    This report was generated with
    <a href="https://github.com/Multiomics-Analytics-Group/vuegen" target="_blank">
        <img src="https://raw.githubusercontent.com/Multiomics-Analytics-Group/vuegen/HEAD/docs/images/logo/vuegen_logo.svg" alt="VueGen" width="65px">
    </a>
    | Copyright 2025 <a href="https://github.com/Multiomics-Analytics-Group" target="_blank">
        Multiomics Network Analytics Group (MoNA)
    </a>
</footer>
'''

st.markdown(footer, unsafe_allow_html=True)
