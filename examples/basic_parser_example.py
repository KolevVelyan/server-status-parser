from server_status_parser import extract_info_from_html

from example_data import HTML_SERVER_STATUS_1

parsed_content = extract_info_from_html(HTML_SERVER_STATUS_1)

print("Parsed content:")
for k, v in parsed_content.items():
    print(f" {k}: '{v}'")
