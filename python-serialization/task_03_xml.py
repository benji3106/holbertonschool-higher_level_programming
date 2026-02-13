#!/usr/bin/python3
"""
XML serialization/deserialization utilities.
"""

import xml.etree.ElementTree as ET


def _python_type_to_str(value):
    """Return a (type_name, text_value) pair for XML storage."""
    if value is None:
        return ("none", "")
    if isinstance(value, bool):
        return ("bool", "true" if value else "false")
    if isinstance(value, int):
        return ("int", str(value))
    if isinstance(value, float):
        return ("float", str(value))
    return ("str", str(value))


def _str_to_python_type(type_name, text_value):
    """Convert XML stored type+text back to a Python value."""
    if type_name == "none":
        return None
    if type_name == "bool":
        return (text_value or "").strip().lower() == "true"
    if type_name == "int":
        return int((text_value or "").strip())
    if type_name == "float":
        return float((text_value or "").strip())
    # default: string
    return text_value if text_value is not None else ""


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to filename.
    Returns True if successful, False otherwise.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            item = ET.SubElement(root, "item")

            k = ET.SubElement(item, "key")
            k.text = str(key)

            v = ET.SubElement(item, "value")
            type_name, text_value = _python_type_to_str(value)
            v.set("type", type_name)
            v.text = text_value

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True

    except (OSError, TypeError, ValueError):
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML from filename into a Python dictionary.
    Returns a dict if successful, None otherwise.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        if root.tag != "data":
            return None

        result = {}
        for item in root.findall("item"):
            key_elem = item.find("key")
            val_elem = item.find("value")

            if key_elem is None or val_elem is None:
                continue

            key = key_elem.text if key_elem.text is not None else ""
            type_name = val_elem.get("type", "str")
            value = _str_to_python_type(type_name, val_elem.text)

            result[key] = value

        return result

    except (FileNotFoundError, OSError, ET.ParseError, ValueError, TypeError):
        return None
