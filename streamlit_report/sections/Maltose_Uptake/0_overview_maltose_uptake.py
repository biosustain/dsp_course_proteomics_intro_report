from pathlib import Path
from st_aggrid import AgGrid, GridOptionsBuilder
from vuegen import table_utils
import json
import pandas as pd
import requests
import streamlit as st
df_index = 1
section_dir = Path(__file__).resolve().parent.parent

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Volcano Plot
    </h4>
    ''',
    unsafe_allow_html=True)


file_path = (section_dir / '../../report/3_maltose_uptake/0_volcano_plot.json').resolve().as_posix()
with open(file_path, 'r') as plot_file:
    plot_json = json.load(plot_file)

# Keep only 'data' and 'layout' sections
plot_json = {key: plot_json[key] for key in plot_json
                                 if key in ['data', 'layout']}

# Remove 'frame' section in 'data'
plot_json['data'] = [{k: v for k, v in entry.items() if k != 'frame'}
                                for entry in plot_json.get('data', [])]
st.plotly_chart(plot_json, use_container_width=True)

st.markdown(
    '''
    <h4 style='text-align: center;
    color: #2b8cbe;'>
    Differential Regulation
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/3_maltose_uptake/1_differential_regulation.csv').resolve().as_posix()
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
    Differently Regulated As In Paper
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/3_maltose_uptake/1_differently_regulated_as_in_paper.csv').resolve().as_posix()
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
    Highlighted Proteins In Figure3
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/3_maltose_uptake/2_highlighted_proteins_in_figure3.csv').resolve().as_posix()
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
    Highlighted Proteins In Figure3 Intensities
    </h4>
    ''',
    unsafe_allow_html=True)

file_path = (section_dir / '../../report/3_maltose_uptake/3_highlighted_proteins_in_figure3_intensities.csv').resolve().as_posix()
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