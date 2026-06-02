from pathlib import Path
from st_aggrid import AgGrid, GridOptionsBuilder
from vuegen import table_utils
import pandas as pd
import streamlit as st
df_index = 1
section_dir = Path(__file__).resolve().parent.parent

st.markdown(
    '''
    <h3 style='text-align: center;
    color: #023558;'>
    Completeness
    </h3>
    ''',
    unsafe_allow_html=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Data Completeness Bar Plot
    </h4>
    ''',
    unsafe_allow_html=True)

plot_file_path = (section_dir / '../../report/1_data/completeness/data_completeness_bar_plot.png').resolve().as_posix()
st.image(plot_file_path, caption='', use_column_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Data Completeness Step Plot
    </h4>
    ''',
    unsafe_allow_html=True)

plot_file_path = (section_dir / '../../report/1_data/completeness/data_completeness_step_plot.png').resolve().as_posix()
st.image(plot_file_path, caption='', use_column_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Proteins
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/1_data/completeness/proteins.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Proteins Identifiers
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/1_data/completeness/proteins_identifiers.csv').resolve().as_posix()
df = pd.read_csv(file_path)


# Displays a DataFrame using AgGrid with configurable options.
grid_builder = GridOptionsBuilder.from_dataframe(df)
grid_builder.configure_default_column(editable=True,
                                      groupable=True,
                                      filter=True,
)
grid_builder.configure_side_bar(filters_panel=True,
                                columns_panel=True)
grid_builder.configure_selection(selection_mode="multiple")
grid_builder.configure_pagination(enabled=True,
                                paginationAutoPageSize=False,
                                paginationPageSize=20,
)
grid_options = grid_builder.build()

AgGrid(df, gridOptions=grid_options, enable_enterprise_modules=True)

# Button to download the df
df_csv = df.to_csv(sep=',', header=True, index=False
                  ).encode('utf-8')
st.download_button(
    label="Download dataframe as CSV",
    data=df_csv,
    file_name=f"dataframe_{df_index}.csv",
    mime='text/csv',
    key=f"download_button_{df_index}")
df_index += 1
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
