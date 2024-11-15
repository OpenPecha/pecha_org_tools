import re
from pathlib import Path
from typing import List, Union

from openpyxl import load_workbook


class CategoryExtractor:
    def __init__(self):
        self.rows_data = []

    @staticmethod
    def read_xlsx_file(file_path: Path):
        """
        Read the xlsx file and return its contents as a list of rows.
        """
        workbook = load_workbook(file_path)
        worksheet = workbook.active
        rows_data = []
        for row in worksheet.iter_rows(values_only=True):
            rows_data.append(row)
        return rows_data

    def extract_categories(self, file_path: Path):
        """
        Process the xlsx file and extract hierarchical categories from its contents.
        """
        self.rows_data = self.read_xlsx_file(file_path)
        extracted_categories = []
        current_category: List[Union[str, None]] = []

        extracted_en_categories = []
        current_en_category: List[Union[str, None]] = []

        for row in self.rows_data:
            # Find the first non-None value and its index
            flag = False
            for col_index, cell_value in enumerate(row):
                if cell_value is not None:
                    flag = True
                    break
            if not flag:
                continue

            current_category_len = len(current_category)
            cell_value = cell_value.strip()

            en_cell_value = row[col_index + 1].strip()

            # Update or extend the current category hierarchy
            if current_category_len == col_index:
                current_category.append(cell_value)
                current_en_category.append(en_cell_value)
            else:
                current_category[col_index] = cell_value
                current_en_category[col_index] = en_cell_value

            # Reset trailing elements to None
            current_category[col_index + 1 :] = [None] * (  # noqa
                current_category_len - col_index - 1
            )
            current_en_category[col_index + 1 :] = [None] * (  # noqa
                current_category_len - col_index - 1
            )

            # Add non-empty elements to the result
            active_category = [
                category for category in current_category if category is not None
            ]
            extracted_categories.append(active_category)

            active_en_category = [
                category for category in current_en_category if category is not None
            ]
            extracted_en_categories.append(active_en_category)

        return extracted_categories, extracted_en_categories

    def format_categories(self, category_hierarchy: List[str]):
        """
        Format each category hierarchy into a structured format with main text and descriptions.
        """
        formatted_hierarchy = []
        for category in category_hierarchy:
            name, description, short_description = extract_text_details(category)
            category_data = {
                "name": name,
                "desc": description,
                "short_desc": short_description,
            }
            formatted_hierarchy.append(category_data)

        return formatted_hierarchy

    def process_file(self, file_path: Path):
        """
        Extract and format categories from the provided xlsx file.
        """
        extracted_categories, extracted_en_categories = self.extract_categories(
            file_path
        )
        formatted_bo_categories = []
        for category_hierarchy in extracted_categories:
            formatted_category = self.format_categories(category_hierarchy)
            formatted_bo_categories.append(formatted_category)

        formatted_en_categories = []
        for category_hierarchy in extracted_en_categories:
            formatted_category = self.format_categories(category_hierarchy)
            formatted_en_categories.append(formatted_category)
        return formatted_bo_categories, formatted_en_categories


def extract_text_details(text: str):
    """
    Extract the main text and any descriptions (in parentheses) from a given string.
    """
    pattern = r"^(.*?)\s*(?:\((.*?)\))?(?:\((.*?)\))?$"
    match = re.search(pattern, text)

    if match:
        name = match.group(1).strip() if match.group(1) else ""
        description = match.group(2).strip() if match.group(2) else ""
        short_description = match.group(3).strip() if match.group(3) else ""
        return name, description, short_description
    else:
        return None, None, None
