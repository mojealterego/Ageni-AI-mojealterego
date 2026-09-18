# Diagramy i źródła LaTeX

Diagramy są przygotowane jako źródła do kompilacji, nie jako zweryfikowany wynik kompilacji. Wymagają dystrybucji LaTeX z pakietem TikZ.

## P vs NP — schemat relacji klas

```latex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[every node/.style={draw,rounded corners,minimum width=3cm,minimum height=1cm}]
  \node (np) {NP};
  \node[below=1.2cm of np] (p) {P};
  \draw[->,thick] (p) -- node[right,draw=none,fill=white] {$P\subseteq NP$} (np);
\end{tikzpicture}
\end{document}
```

## Hipoteza Riemanna — położenie nietrywialnych zer

```latex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[x=5cm,y=1.1cm]
  \draw[->] (-0.15,0) -- (1.15,0) node[right] {$\Re(s)$};
  \draw[->] (0,-2.2) -- (0,2.2) node[above] {$\Im(s)$};
  \draw[dashed,thick] (0.5,-2) -- (0.5,2) node[above right] {$\Re(s)=\frac12$};
  \draw[thick] (0,0) -- (1,0);
  \node[below] at (0,0) {$0$};
  \node[below] at (0.5,0) {$\frac12$};
  \node[below] at (1,0) {$1$};
  \node[draw=none] at (0.5,1.5) {linia krytyczna};
\end{tikzpicture}
\end{document}
```

**Interpretacja:** rysunek przedstawia linię, na której według RH leżą wszystkie nietrywialne zera. Nie przedstawia obliczonych zer ani dowodu hipotezy.

## Hipoteza Hodge’a — schemat mapy cykli

```latex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[every node/.style={draw,rounded corners,align=center,minimum width=4cm,minimum height=1cm}]
  \node (a) {Cykle algebraiczne\z współczynnikami wymiernymi};
  \node[right=2.3cm of a] (b) {Klasy Hodge’a\w odpowiednim stopniu};
  \draw[->,thick] (a) -- node[above,draw=none] {mapa cykli} (b);
\end{tikzpicture}
\end{document}
```

## BSD — schemat porównania rzędu

```latex
\documentclass[tikz,border=6pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[every node/.style={draw,rounded corners,align=center,minimum width=4cm,minimum height=1cm}]
  \node (a) {Rząd grupy\$E(\mathbb{Q})$};
  \node[right=2.2cm of a] (b) {Rząd zera\$L(E,s)$ w $s=1$};
  \draw[<->,thick] (a) -- node[above,draw=none] {równość przewidywana przez BSD} (b);
\end{tikzpicture}
\end{document}
```

## Uwagi kompilacyjne

Powyższe przykłady korzystają z pozycjonowania `below=... of` i `right=... of`, więc w preambule każdego dokumentu należy dodać:

```latex
\usetikzlibrary{positioning}
```

Diagramy są poglądowymi schematami relacji. Nie zastępują pełnych definicji ani dowodów. Kompilacja nie została wykonana w tym repozytorium.
