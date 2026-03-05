project = "VibeCoding Docs"
author = "VibeCoding"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_static_path = ["_static"]
html_css_files = [
    'custom.css',
]

root_doc = "index"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# LaTeX settings
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'geometry': r'\usepackage[margin=1.5cm,top=2cm,bottom=2cm]{geometry}',
    'preamble': r'''
% 禁止章节强制从奇数页开始（消除大量空白页）
\let\cleardoublepage\clearpage
\usepackage{xeCJK}
\setCJKmainfont[
    BoldFont=HarmonyOS Sans SC,
    ItalicFont=HarmonyOS Sans SC
]{HarmonyOS Sans SC}
\setCJKmonofont{HarmonyOS Sans SC}
\setmainfont{FreeSerif}
\setsansfont{FreeSans}
\setmonofont{FreeMono}
% 将常见西文标点声明为 Default 字符，由主字体(FreeSerif)渲染
\xeCJKDeclareCharClass{Default}{
  "2018, "2019,   % ' '  单引号
  "201C, "201D,   % " "  双引号
  "2013, "2014,   % – —  连接号/破折号
  "2026,          % …    省略号
  "00B7,          % ·    间隔号
  "2022,          % •    圆点
  "00B0,          % °    度号
  "00A9, "00AE,   % © ®  版权/注册
  "2122           % ™    商标
}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
% 防止表格列内容溢出
\usepackage{array}
\usepackage{etoolbox}
% 缩小列间距，给内容更多空间
\setlength{\tabcolsep}{3pt}
% 表格内使用小字号，避免宽表撑出页面
\AtBeginEnvironment{longtable}{\small}
\AtBeginEnvironment{tabulary}{\small}
% 允许长单词/URL 自动断行
\usepackage{xurl}
% tabular 自动缩放到页面宽度和高度（防止横向大表溢出页面）
\usepackage{adjustbox}
\BeforeBeginEnvironment{tabular}{\begin{adjustbox}{max totalsize={\linewidth}{0.92\textheight},keepaspectratio,center}}
\AfterEndEnvironment{tabular}{\end{adjustbox}}
% 横向页面支持（仅局部区域）
\usepackage{pdflscape}
''',
}

latex_documents = [
    (root_doc, 'VibeCodingDocs.tex', project, author, 'manual'),
]
