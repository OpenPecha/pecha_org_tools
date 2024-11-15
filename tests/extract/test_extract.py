from pathlib import Path

from pecha_org_categorizer.extract import (
    CategoryExtractor,
    extract_text_details,
    format_categories,
)


def test_extract_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    extractor = CategoryExtractor(input_xlsx)
    extractor.extract_categories()
    assert extractor.bo_extracted_categories == [
        ["ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)"],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།",
            "རྩ་བ།",
        ],
        [
            "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
            "ཀུན་བཟང་སྨོན་ལམ།",
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
    assert extractor.en_extracted_categories == [
        ["Recitation (Explanation of Recitation)(Brief Explanation of Recitation)"],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Actions",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Actions",
            "Root Text",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Actions",
            "Commentary Text",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Conduct (Explanation of Good Conduct)(Brief Explanation of Good Conduct)",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Conduct (Explanation of Good Conduct)(Brief Explanation of Good Conduct)",
            "Root Text",
        ],
        [
            "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
            "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
            "The Prayer of Good Conduct (Explanation of Good Conduct)(Brief Explanation of Good Conduct)",
            "Commentary Text",
        ],
    ]


def parse_category():
    text = "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)"
    name, desc, short_desc = extract_text_details(text)

    assert name == "ཁ་འདོན།"
    assert desc == "ཁ་འདོན་འགྲེལ་བཤད་"
    assert short_desc == "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་"

    text = "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)"
    name, desc, short_desc = extract_text_details(text)
    assert name == "སྨོན་ལམ།"
    assert desc == "སྨོན་ལམ་འགྲེལ་བཤད་"
    assert short_desc == ""

    text = "བཟང་སྤྱོད་སྨོན་ལམ།"
    name, desc, short_desc = extract_text_details(text)
    assert name == "བཟང་སྤྱོད་སྨོན་ལམ།"
    assert desc == ""
    assert short_desc == ""


def test_format_category():

    input = ["ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་)"]
    output = format_categories(input)
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "desc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "short_desc": "ཁ་འདོན་འགྲེལ་བཤད་",
        }
    ]

    input = ["སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)"]
    output = format_categories(input)
    assert output == [
        {"name": "སྨོན་ལམ།", "desc": "སྨོན་ལམ་འགྲེལ་བཤད་", "short_desc": ""}
    ]

    input = ["བཟང་སྤྱོད་སྨོན་ལམ།"]
    output = format_categories(input)
    assert output == [{"name": "བཟང་སྤྱོད་སྨོན་ལམ།", "desc": "", "short_desc": ""}]

    input = [
        "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "འགྲེལ་བ།",
    ]
    output = format_categories(input)
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "desc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "short_desc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "སྨོན་ལམ།",
            "desc": "སྨོན་ལམ་འགྲེལ་བཤད་",
            "short_desc": "སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "བཟང་སྤྱོད་སྨོན་ལམ།",
            "desc": "བཟང་སྤྱོད་འགྲེལ་བཤད་",
            "short_desc": "བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {"name": "འགྲེལ་བ།", "desc": "", "short_desc": ""},
    ]


def test_get_category_hierarchy():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཁ་འདོན།"
    pecha_metadata = {
        "title": "སློབ་གྲྭ་ཁ་འདོན།",
        "desc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
        "short_desc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
    }
    output = categorizer.get_category_hierarchy(category_name, pecha_metadata, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "desc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "short_desc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "སློབ་གྲྭ་ཁ་འདོན།",
            "desc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
            "short_desc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
    ]

    category_name = "Recitation"
    pecha_metadata = {
        "title": "School Recitation",
        "desc": "School Recitation description",
        "short_desc": "School Recitation Short description",
    }

    output = categorizer.get_category_hierarchy(category_name, pecha_metadata, "en")
    assert output == [
        {
            "name": "Recitation",
            "desc": "Explanation of Recitation",
            "short_desc": "Brief Explanation of Recitation",
        },
        {
            "name": "School Recitation",
            "desc": "School Recitation description",
            "short_desc": "School Recitation Short description",
        },
    ]


test_get_category_hierarchy()
