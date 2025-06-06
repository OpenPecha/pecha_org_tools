
<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

<!-- Replace with 1-sentence description about what this tool is or does.-->

<h3 align="center">Pecha.org Categorizer</h3>

## Description
- A python package to get category for a particular pecha.
- Spreedsheet link [here](https://docs.google.com/spreadsheets/d/16pvNdKqGSb_CNZEkzS8B9fn_o9MMsoqA4vC5_X9G7bc/edit?usp=sharing).
- Kindly ask for permission from [@tenzin3](https://github.com/tenzin3) for write access to the spreadsheet.
- Input the  Pechas with unassigned categories in the Spreedsheet [here](https://docs.google.com/spreadsheets/d/16pvNdKqGSb_CNZEkzS8B9fn_o9MMsoqA4vC5_X9G7bc/edit?gid=1284579012#gid=1284579012).
- To know how to use the package, refer to `extract` folder from `tests` directory.

## How it Works?

![Category image](resources/category.png)

pecha.org organizes content in a tree-like structure, where a specific Pecha can belong to various nested categories or sections.

For example, in the image above:

* The primary category is **ཁ་འདོན།** (Recitation).
* Under it, there are subcategories like **སྨོན་ལམ།** (Aspiration Prayer), which further branches into **ཀུན་བཟང་སྨོན་ལམ།** (Samantabhadra Aspiration Prayer) and **བཟང་སྤྱོད་སྨོན་ལམ།** (Bodhicharyavatara Aspiration Prayer).

Each cell in the spreadsheet contains the following information:
སྨོན་ལམ།(སྨོན་ལམ་འགྲེལ་བཤད་)(སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་)

#### **Structure of a Cell**

1. **Title:** The first part is the title of the category (e.g., སྨོན་ལམ།).
2. **Description:** The text in the first set of parentheses provides a detailed description (e.g., སྨོན་ལམ་འགྲེལ་བཤད་ - Explanation of Aspiration Prayer).
3. **Short Description:** The text in the second set of parentheses gives a brief description (e.g., སྨོན་ལམ་འགྲེལ་བཤད་ཐུང་ཐུང་ - Brief Explanation of Aspiration Prayer).

The corresponding English cell might look like this:
Aspiration Prayer (Explanation of Aspiration Prayer) (Brief Explanation of Aspiration Prayer)

By using **pecha_org_tools**, users can ensure consistency in both Tibetan and English categorizations, making it easier to organize and navigate the texts on pecha.org.


## Project owner(s)

<!-- Link to the repo owners' github profiles -->

- [@tenzin3](https://github.com/tenzin3)

None
## Docs

<!-- Update the link to the docs -->

Read the docs [here](https://wiki.openpecha.org/#/dev/coding-guidelines).
