from pathlib import Path

from pecha_org_tools.extract import CategoryExtractor
from pecha_org_tools.utils import read_json


def test_extract_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    extractor = CategoryExtractor(input_xlsx)
    extractor.extract_categories()

    expected_bo_categories = read_json(DATA_DIR / "expected_bo_categories.json")
    expected_en_categories = read_json(DATA_DIR / "expected_en_categories.json")

    assert extractor.bo_extracted_categories == expected_bo_categories
    assert extractor.en_extracted_categories == expected_en_categories


test_extract_category()
