from pathlib import Path

from pecha_org_tools.extract import CategoryExtractor


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
