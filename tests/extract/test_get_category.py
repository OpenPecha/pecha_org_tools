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

    category_name = "ཀུན་བཟང་སྨོན་ལམ་རྩ་བ་དེབ་།"
    output = categorizer.get_category_by_lang(category_name, "bo")
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
        {"name": "ཀུན་བཟང་སྨོན་ལམ།", "heDesc": "", "heShortDesc": ""},
        {"name": "རྩ་བ།", "heDesc": "", "heShortDesc": ""},
        {"name": "ཀུན་བཟང་སྨོན་ལམ་རྩ་བ་དེབ་།", "heDesc": "", "heShortDesc": ""},
    ]

    category_name = "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢"
    output = categorizer.get_category_by_lang(category_name, "bo")
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
        {"name": "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢", "heDesc": "", "heShortDesc": ""},
    ]

    category_name = "The Prayer of Good Actions Root Text Book"
    output = categorizer.get_category_by_lang(category_name, "en")
    assert output == [
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
        {"name": "The Prayer of Good Actions", "enDesc": "", "enShortDesc": ""},
        {"name": "Root Text", "enDesc": "", "enShortDesc": ""},
        {
            "name": "The Prayer of Good Actions Root Text Book",
            "enDesc": "",
            "enShortDesc": "",
        },
    ]


def test_get_category():
    DATA_DIR = Path(__file__).parent / "data"
    input_xlsx = DATA_DIR / "input.xlsx"

    categorizer = CategoryExtractor(input_xlsx)

    category_name = "ཀུན་བཟང་སྨོན་ལམ་རྩ་བ་དེབ་།"
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
            {"name": "ཀུན་བཟང་སྨོན་ལམ།", "heDesc": "", "heShortDesc": ""},
            {"name": "རྩ་བ།", "heDesc": "", "heShortDesc": ""},
            {"name": "ཀུན་བཟང་སྨོན་ལམ་རྩ་བ་དེབ་།", "heDesc": "", "heShortDesc": ""},
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
            {"name": "The Prayer of Good Actions", "enDesc": "", "enShortDesc": ""},
            {"name": "Root Text", "enDesc": "", "enShortDesc": ""},
            {
                "name": "The Prayer of Good Actions Root Text Book",
                "enDesc": "",
                "enShortDesc": "",
            },
        ],
    }
    assert output == expected_output

    category_name = "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢"
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
            {"name": "འགྲེལ་བ།", "heDesc": "", "heShortDesc": ""},
            {
                "name": "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢",
                "heDesc": "",
                "heShortDesc": "",
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
            {"name": "Commentary Text", "enDesc": "", "enShortDesc": ""},
            {
                "name": "The Prayer of Good Conduct Commentary Text Book 2",
                "enDesc": "",
                "enShortDesc": "",
            },
        ],
    }
    assert output == expected_output
