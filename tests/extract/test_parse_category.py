from pecha_org_tools.extract import parse_category_text


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
