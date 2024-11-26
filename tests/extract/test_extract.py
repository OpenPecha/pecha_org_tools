from pathlib import Path

from pecha_org_categorizer.enums import TextType
from pecha_org_categorizer.extract import (
    CategoryExtractor,
    format_categories,
    parse_category_text,
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
    name, heDesc, heShortDesc = parse_category_text(text)

    assert name == "ཁ་འདོན།"
    assert heDesc == "ཁ་འདོན་འགྲེལ་བཤད་"
    assert heShortDesc == "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་"

    text = "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)"
    name, heDesc, heShortDesc = parse_category_text(text)
    assert name == "སྨོན་ལམ།"
    assert heDesc == "སྨོན་ལམ་འགྲེལ་བཤད་"
    assert heShortDesc == ""

    text = "བཟང་སྤྱོད་སྨོན་ལམ།"
    name, heDesc, heShortDesc = parse_category_text(text)
    assert name == "བཟང་སྤྱོད་སྨོན་ལམ།"
    assert heDesc == ""
    assert heShortDesc == ""


def test_format_category():

    input = ["ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་)"]
    output = format_categories(input, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
        }
    ]

    input = ["སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)"]
    output = format_categories(input, "bo")
    assert output == [
        {"name": "སྨོན་ལམ།", "heDesc": "སྨོན་ལམ་འགྲེལ་བཤད་", "heShortDesc": ""}
    ]

    input = ["བཟང་སྤྱོད་སྨོན་ལམ།"]
    output = format_categories(input, "bo")
    assert output == [{"name": "བཟང་སྤྱོད་སྨོན་ལམ།", "heDesc": "", "heShortDesc": ""}]

    input = [
        "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "འགྲེལ་བ།",
    ]
    output = format_categories(input, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "སྨོན་ལམ།",
            "heDesc": "སྨོན་ལམ་འགྲེལ་བཤད་",
            "heShortDesc": "སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "བཟང་སྤྱོད་སྨོན་ལམ།",
            "heDesc": "བཟང་སྤྱོད་འགྲེལ་བཤད་",
            "heShortDesc": "བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {"name": "འགྲེལ་བ།", "heDesc": "", "heShortDesc": ""},
    ]


def test_get_category_by_lang():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཁ་འདོན།"
    pecha_metadata = {
        "title": "སློབ་གྲྭ་ཁ་འདོན།",
        "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
        "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
    }
    output = categorizer.get_category_by_lang(category_name, pecha_metadata, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {
            "name": "སློབ་གྲྭ་ཁ་འདོན།",
            "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
    ]

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཁ་འདོན།"
    pecha_metadata = {
        "title": "སློབ་གྲྭ་ཁ་འདོན།",
        "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
        "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
    }
    output = categorizer.get_category_by_lang(
        category_name, pecha_metadata, "bo", TextType.ROOT
    )
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        {"name": "རྩ་བ།", "heDesc": "", "heShortDesc": ""},
        {
            "name": "སློབ་གྲྭ་ཁ་འདོན།",
            "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
    ]

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "Recitation"
    pecha_metadata = {
        "title": "School Recitation",
        "enDesc": "School Recitation heDescription",
        "enShortDesc": "School Recitation Short heDescription",
    }

    output = categorizer.get_category_by_lang(category_name, pecha_metadata, "en")
    assert output == [
        {
            "name": "Recitation",
            "enDesc": "Explanation of Recitation",
            "enShortDesc": "Brief Explanation of Recitation",
        },
        {
            "name": "School Recitation",
            "enDesc": "School Recitation heDescription",
            "enShortDesc": "School Recitation Short heDescription",
        },
    ]

    categorizer = CategoryExtractor(input_xlsx)
    category_name = "Recitation"
    pecha_metadata = {
        "title": "School Recitation",
        "enDesc": "School Recitation heDescription",
        "enShortDesc": "School Recitation Short heDescription",
    }

    output = categorizer.get_category_by_lang(
        category_name, pecha_metadata, "en", TextType.COMMENTARY
    )
    assert output == [
        {
            "name": "Recitation",
            "enDesc": "Explanation of Recitation",
            "enShortDesc": "Brief Explanation of Recitation",
        },
        {"name": "Commentaries", "enDesc": "", "enShortDesc": ""},
        {
            "name": "School Recitation",
            "enDesc": "School Recitation heDescription",
            "enShortDesc": "School Recitation Short heDescription",
        },
    ]


def test_get_category_hierarchy():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཁ་འདོན།"
    pecha_metadata = {
        "bo": {
            "title": "སློབ་གྲྭ་ཁ་འདོན།",
            "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        },
        "en": {
            "title": "School Recitation",
            "enDesc": "School Recitation heDescription",
            "enShortDesc": "School Recitation Short heDescription",
        },
    }
    output = categorizer.get_category_hierarchy(category_name, pecha_metadata)
    expected_output = {
        "bo": [
            {
                "name": "ཁ་འདོན།",
                "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
                "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
            },
            {
                "name": "སློབ་གྲྭ་ཁ་འདོན།",
                "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
                "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
            },
            {
                "name": "སློབ་གྲྭ་ཁ་འདོན།",
                "heDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་",
                "heShortDesc": "སློབ་གྲྭ་ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
            },
        ],
        "en": [
            {
                "name": "Recitation",
                "enDesc": "Explanation of Recitation",
                "enShortDesc": "Brief Explanation of Recitation",
            },
            {
                "name": "School Recitation",
                "enDesc": "School Recitation heDescription",
                "enShortDesc": "School Recitation Short heDescription",
            },
        ],
    }
    assert output == expected_output


test_get_category_hierarchy()
