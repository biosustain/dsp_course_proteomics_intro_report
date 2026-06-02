# VueGen reports for proteomics intro course

## Install vuegen

```bash
pip install vuegen
```

## command line help

```bash
>>> vuegen --help

usage: VueGen [-h] [-c CONFIG] [-dir DIRECTORY] [-rt REPORT_TYPE] [-output_dir OUTPUT_DIRECTORY] [-st_autorun] [-qt_checks] [-mdep MAX_DEPTH]

options:
  -h, --help            show this help message and exit
  -c, --config CONFIG   Path to the YAML configuration file.
  -dir, --directory DIRECTORY
                        Path to the directory from which the YAML config will be inferred.
  -rt, --report_type REPORT_TYPE
                        Type of the report to generate: streamlit, html, pdf, docx, odt, revealjs, pptx, or jupyter.
  -output_dir, --output_directory OUTPUT_DIRECTORY
                        Path to the output directory for the generated report.
  -st_autorun, --streamlit_autorun
                        Automatically run the Streamlit app after report generation.
  -qt_checks, --quarto_checks
                        Check if Quarto is installed and available for report generation.
  -mdep, --max_depth MAX_DEPTH
                        Maximum depth for the recursive search of files in the input directory. Ignored if a config file is provided.
```

## Run vuegen based on the `result` folder

```bash
vuegen -dir report -st_autorun
```

## Customize the configfile

Based on the genericly created config file base on a directory using `-dir`, you can
customize a copy with descriptions.

```bash
# Streamlit report
vuegen -st_autorun --config report_config_manuel.yaml
# html report
vuegen -st_autorun --config report_config_manuel.yaml -rt html
```

