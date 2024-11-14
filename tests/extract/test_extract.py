from pathlib import Path

from pecha_org_categorizer.extract import Extractor


def test_extract():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    extractor = Extractor()
    extracted_info = extractor.extract(input_xlsx)
    print(extracted_info)


test_extract()
