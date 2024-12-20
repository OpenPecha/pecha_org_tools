from pathlib import Path

from pecha_org_tools.enums import TextType
from pecha_org_tools.extract import CategoryExtractor


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


def test_get_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "བཟང་སྤྱོད་སྨོན་ལམ།"
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
    output = categorizer.get_category(category_name, pecha_metadata, TextType.ROOT)
    expected_output = {
        "bo": [
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
            {"name": "རྩ་བ།", "heDesc": "", "heShortDesc": ""},
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
                "name": "Aspiration Prayer",
                "enDesc": "Explanation of Aspiration Prayer",
                "enShortDesc": "Brief Explanation of Aspiration Prayer",
            },
            {
                "name": "The Prayer of Good Conduct",
                "enDesc": "Explanation of Good Conduct",
                "enShortDesc": "Brief Explanation of Good Conduct",
            },
            {"name": "Root text", "enDesc": "", "enShortDesc": ""},
            {
                "name": "School Recitation",
                "enDesc": "School Recitation heDescription",
                "enShortDesc": "School Recitation Short heDescription",
            },
        ],
    }
    assert output == expected_output
