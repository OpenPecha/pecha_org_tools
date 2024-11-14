from pathlib import Path

from pecha_org_categorizer.extract import Extractor


def test_extract():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    extractor = Extractor()
    extracted_info = extractor.extract(input_xlsx)
    assert extracted_info == [
        ["ཁ་འདོན།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "ཀུན་བཟང་སྨོན་ལམ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "ཀུན་བཟང་སྨོན་ལམ།", "རྩ་བ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "ཀུན་བཟང་སྨོན་ལམ།", "འགྲེལ་བ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "བཟང་སྤྱོད་སྨོན་ལམ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "བཟང་སྤྱོད་སྨོན་ལམ།", "རྩ་བ།"],
        ["ཁ་འདོན།", "སྨོན་ལམ།", "བཟང་སྤྱོད་སྨོན་ལམ།", "འགྲེལ་བ།"],
    ]
