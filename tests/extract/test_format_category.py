from pecha_org_tools.extract import format_categories


def test_format_category():
    input = ["བཟང་སྤྱོད་སྨོན་ལམ།"]
    output = format_categories(input, "bo")
    assert output == [{"name": "བཟང་སྤྱོད་སྨོན་ལམ།", "heDesc": "", "heShortDesc": ""}]

    input = ["ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་)"]
    output = format_categories(input, "bo")
    assert output == [
        {
            "name": "ཁ་འདོན།",
            "heDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
            "heShortDesc": "ཁ་འདོན་འགྲེལ་བཤད་",
        }
    ]

    input = [
        "ཁ་འདོན།(ཁ་འདོན་འགྲེལ་བཤད་)(ཁ་འདོན་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "བཟང་སྤྱོད་སྨོན་ལམ།(བཟང་སྤྱོད་འགྲེལ་བཤད་)(བཟང་སྤྱོད་འགྲེལ་བཤད་ཐུང་ཐུང་)",
        "འགྲེལ་བ།",
        "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢",
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
        {"name": "བཟང་སྤྱོད་སྨོན་ལམ་འགྲེལ་བ་དེབ་། ༢", "heDesc": "", "heShortDesc": ""},
    ]

    input = ["Recitation (Explanation of Recitation)(Brief Explanation of Recitation)"]
    output = format_categories(input, "en")
    assert output == [
        {
            "name": "Recitation",
            "enDesc": "Explanation of Recitation",
            "enShortDesc": "Brief Explanation of Recitation",
        }
    ]

    input = [
        "Recitation (Explanation of Recitation)(Brief Explanation of Recitation)",
        "Aspiration Prayer (Explanation of Aspiration Prayer)(Brief Explanation of Aspiration Prayer)",
        "The Prayer of Good Actions",
        "Root Text",
        "The Prayer of Good Actions Root Text Book",
    ]
    output = format_categories(input, "en")
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
