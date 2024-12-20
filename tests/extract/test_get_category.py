from pathlib import Path

from pecha_org_tools.extract import CategoryExtractor


def test_get_category_by_lang():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཁ་འདོན།"
    output = categorizer.get_category_by_lang(category_name, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་",
        }
    ]

    category_name = "Recitation"
    output = categorizer.get_category_by_lang(category_name, "en")
    assert output == [
        {
            "name": "Recitation",
            "enDesc": "Explanation of Recitation",
            "enShortDesc": "Brief Explanation of Recitation",
        }
    ]


def test_get_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "བཟང་སྤྱོད་སྨོན་ལམ།"
    output = categorizer.get_category(category_name)
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
        ],
    }
    assert output == expected_output
