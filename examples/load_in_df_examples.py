from server_status_parser import extract_info_from_html
from example_data import (
    HTML_SERVER_STATUS_1,
    HTML_SERVER_STATUS_2,
    SIMPLE_SERVER_STATUS_1,
    SIMPLE_SERVER_STATUS_2,
    SIMPLE_SERVER_STATUS_3,
)
import pandas as pd

results = []
for example_content in [
    HTML_SERVER_STATUS_1,
    HTML_SERVER_STATUS_2,
    SIMPLE_SERVER_STATUS_1,
    SIMPLE_SERVER_STATUS_2,
    SIMPLE_SERVER_STATUS_3,
]:
    info = extract_info_from_html(example_content)
    results.append(info)

df = pd.DataFrame(results)
print(df)
