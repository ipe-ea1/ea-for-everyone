import os
import xml.etree.ElementTree as ET

def remove_factSheet_attr(select_attr: str, directory: str, input_filename: str, output_filename: str):
    """
    Removes the select_attr attribute from all <object> elements in an XML file.

    Args:
        select_attr (str): The attribute to be removed
        directory (str): Path to the directory containing the XML file.
        input_filename (str): Name of the input XML file.
        output_filename (str): Name of the output XML file (will be created/overwritten).
    """
    # Build full file paths
    input_path = os.path.join(directory, input_filename)
    output_path = os.path.join(directory, output_filename)

    # Parse the XML
    tree = ET.parse(input_path)
    root = tree.getroot()

    # Remove factSheetId attribute from all <object> elements
    for obj in root.findall(".//object"):
        if select_attr in obj.attrib:
            del obj.attrib[select_attr]

    # Write the modified XML to the output file
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

    print(f"Processed '{input_filename}' → '{output_filename}' ('{select_attr}' removed).")

# Example usage:
# remove_factSheet_attr("factSheetId", "/path/to/xml/files", "input.xml", "output.xml")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Remove the supplied factSheet attribute from <object> elements in an XML file."
    )
    parser.add_argument("select_attr", help="The attribute you want to remove from the Objects within the file")
    parser.add_argument("directory", help="Path to the directory containing the XML file")
    parser.add_argument("input_filename", help="Name of the input XML file")
    parser.add_argument("output_filename", help="Name of the output XML file")

    args = parser.parse_args()

    remove_factSheet_attr(args.select_attr, args.directory, args.input_filename, args.output_filename)
