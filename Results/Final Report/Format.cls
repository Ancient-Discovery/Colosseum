\ProvidesClass{Format}
\def\thesisID{1}
%\def\dissertationID{2}
\def\theDocumentType#1{\gdef\@theDocumentType{#1}}
\def\documentID#1{\gdef\@documentID{#1}}
% DocumentID is either 1 (for thesis) or 2 (for dissertation).
\DeclareOption{thesis}
{
	\def\@theDocumentType{thesis}
	\def\@documentID{\thesisID}
}
%\DeclareOption{dissertation}
%{
%	\def\@theDocumentType{dissertation}
%	\def\@documentID{\dissertationID}
%}
\DeclareOption{linespacing}{\@lnspacing}
\DeclareOption*{\PassOptionsToPackage{\CurrentOption}{color}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ExecuteOptions{thesis, a4paper, 12pt} % Execute default options.
\ProcessOptions
\LoadClass{report} % Single-sided.

\def\graduationYear#1{\gdef\@graduationYear{#1}}
\def\graduationMonth#1{\gdef\@graduationMonth{#1}}
\def\supervisor#1{\gdef\@supervisor{#1}}
\def\keywords#1{\gdef\@keywords{#1}}
\def\headSchool#1{\gdef\@headSchool{#1}}
\def\major#1{\gdef\@major{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\college#1{\gdef\@college{#1}}
\def\dept#1{\gdef\@dept{#1}}
\def\university#1{\gdef\@university{#1}}

% Initialise macros.
\def\@title{Ancient Discovery: AI for Oracle Bone Script Recognition}
\def\@author{Yongzhen Ren}
\def\@keywords{oracle bone scripts, bronze scripts, deep learning, CycleGAN, conditional GAN, pix2pix}
\def\@graduationYear{2018}
\def\@graduationMonth{May}
\def\@supervisor{Ruihai Dong}
\def\@degree{BSc. (Hons.) in Computer Science}
\def\@college{Science}
\def\@dept{Computer Science}
\def\@headSchool{Prof. P{\'a}draig Cunningham}
\def\@major{Computer Science}
\def\@university{University College Dublin}

\RequirePackage{amsmath,amsthm,amssymb}	 			% AMS math, AMS theorem, AMS fonts.
\RequirePackage{mathrsfs}				   			% Additional math scripts.
\RequirePackage{setspace}				   			% Line spacing.
\RequirePackage[vcentering, dvips, a4paper]{geometry}		% Help with margins.
\RequirePackage{color}									% Allows for changing text color.
\RequirePackage[numbers]{natbib}						% This package allows you to link your references.
\RequirePackage{graphicx}								% Graphics package.
\RequirePackage{float}					  			% Figure floats.
\RequirePackage[config, labelfont={bf}]{caption,subfig} % Nice sub figures.
\RequirePackage[Bjarne]{fncychap}						% Create fancier chapter titles.
\RequirePackage{url}									% Nicely format url breaks.
\RequirePackage[inactive]{srcltx}		 				% Necessary to use forward and inverse searching in DVI.
\RequirePackage{relsize}								% Font sizing hierarchy.
\RequirePackage{booktabs}				   			% Professional looking tables.
\RequirePackage[pdftex,plainpages=false,pdfpagelabels=true,breaklinks=true,pagebackref]{hyperref} % For pdf bookmarks.

\renewcommand{\bibname}{References} % Rename Bibliography to Refrences.

% Allow empty pages before chapters (i.e. no page numbers).
\let\origdoublepage\cleardoublepage
\newcommand{\clearemptydoublepage}
{
	\clearpage
	{\pagestyle{empty}\origdoublepage}
}
\let\cleardoublepage\clearemptydoublepage

\hypersetup
{
	bookmarksnumbered = true,
	pdftitle={\@title},
	pdfauthor = {\@author},
	pdfsubject = {\@dept},
	pdfkeywords = {\@keywords},
	pdfpagelayout = SinglePage,
	bookmarksopen = False,
	%pdfview = FitV,
	pdfborder = 0 0 0, 		% make all links invisible, so the pdf looks good when printed	
	pdffitwindow = true,	  % window fit to page when opened
	%pdfstartview = {FitV},   % fits the width of the page to the window
	pdfcreator = {\@author},  % creator of the document
	pdfnewwindow = true,	  % links in new window
	colorlinks = true,		% false: boxed links; true: colored links
	linkcolor = blue,		 % color of internal links
	citecolor = magenta,	  % color of links to bibliography
	filecolor = magenta,	  % color of file links
	urlcolor = cyan		   % color of external links
}

\geometry
{
	a4paper,
	left = 1.0in,
	right = 1.0in,
	top = 1.0in,
	bottom = 1.0in
}

%\hyphenation{example, pa-ra-me-ter} % Over-ride Latex hyphenation, define hyphenated words.
\hyphenpenalty = 5000 % Reduce hyphenation as much as possible.
\tolerance = 1000 % Go with the previous command.
% Widow / orphan protection.
\clubpenalty = 10000 % Minimize orphans orphans (eliminate 10000).
\widowpenalty = 10000 % Minimize widows.
\brokenpenalty = 10000 % Do not allow hyphen across pages.

\raggedbottom % The \raggedbottom declaration makes all pages the height of the text on that page. No extra vertical space is added.
\pagestyle{plain}

\newcommand{\addToPDFBookmarks}[3]
{
	\cleardoublepage
	\phantomsection
	\pdfbookmark[#1]{#2}{#3}
}

\newcommand{\makeTitlePage}
{
	\thispagestyle{empty}
	\begin{spacing}{1.5}
	\vspace*{0.3in}
	\begin{center}
		\includegraphics[width=2cm]{UCD.eps}

		\huge \bf
		\@title
		
		\vfill
	
		\Large \rm
		\@author

		\vfill

		\normalsize
		\ifnum\@documentID=\thesisID
		{
			A thesis submitted to \@university \\ in fulfilment of the requirements for the degree of
			\bigskip
			
			\Large			
			\textbf{\@degree}
		} 
		\else
		{
			A Dissertation \\ Presented for the	\emph{\@degree}
		} \fi
		
		\bigskip

		\normalsize
		College of \@college \\
		School of \@dept \\

		\vfill

		\begin{tabular}{r l}
			\emph{Head of School:} &\@headSchool \\
			\emph{Supervisor:} &\@supervisor \\
		\end{tabular}
		
		\vfill		
		
		\@graduationMonth\ \@graduationYear
	\end{center}
	\end{spacing}
	\cleardoublepage
}

\newcommand{\addToTOC}[1]
{
	\cleardoublepage
	\phantomsection
	\addcontentsline{toc}{chapter}{#1}
}

\newcommand{\makeBibliographyPage}
{
	\newpage
	\addToTOC{References}
	\vspace*{2.0in} % Move down the page 2.0 inches.
	\begin{center}\Huge\bf{References}\end{center} % Make the bibliography title.
}

\newcommand{\makeAppendixPage}
{
	\newpage
	\vspace*{2.0in}
	\begin{center}\Huge \bf{Appendix} \end{center}
	\newpage
}
\endinput