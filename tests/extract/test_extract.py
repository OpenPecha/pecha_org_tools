from pathlib import Path

from pecha_org_categorizer.extract import Extractor, extract_description_from_text


def test_extract_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    extractor = Extractor()
    extracted_info = extractor.extract(input_xlsx)
    assert extracted_info == [
        ["ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)"],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་)(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་)(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "རྩ་བ།",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་)(ཀུན་བཟང་སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "འགྲེལ་བ།",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "རྩ་བ།",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "འགྲེལ་བ།",
        ],
    ]


def parse_category():
    text = "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)"
    main, desc, short_desc = extract_description_from_text(text)

    assert main == "ཁ་འདོན།"
    assert desc == "ཁ་འདོན་འགྲེལ་བཤད་"
    assert short_desc == "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་"

    text = "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)"
    main, desc, short_desc = extract_description_from_text(text)
    assert main == "སྨོན་ལམ།"
    assert desc == "སྨོན་ལམ་འགྲེལ་བཤད་"
    assert short_desc == ""

    text = "བཟང་སྤྱོད་སྨོན་ལམ།"
    main, desc, short_desc = extract_description_from_text(text)
    assert main == "བཟང་སྤྱོད་སྨོན་ལམ།"
    assert desc == ""
    assert short_desc == ""