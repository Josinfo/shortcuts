!/usr/bin/python

JosinfoXtreme CCIE SP -- VIM Navegability


set nu : linha numerada

gg - SOBE NA PRIMEIRA LINHA

GG - DESCE ATE O FINAL

o = adiciona uma linha

0 = retorna inicio da linha

$ = Avanca ao final da linha

r : replace string

dw : apaga a palavra

dd : Deletes a whole line of text.

x : Deleta para frente (DEL).

shift + x : Deleta para trás (BACKSPACE).

. : (Dot) Repeats the last command

YS = Recortar a linha

yy : (Yank) Copies the current line into memory.

4yy : Copies 4 lines, beginning with the one under the cursor.

p : Paste previously deleted or yanked text

u : Crtl+Z

j : JumpLine

:X : onde X e o numero da linha

v + setas direcionais do teclado =

y = Copia o texto marcado.

c = Recorta o texto marcado.

/ = Localiza texto. n = Localiza novamente -

Vu = Torna todos os caracteres da linha minúsculos vu = Torna apenas o primeiro caractere da linha minúsculo

VU = Torna todos os caracteres da linha maiúsculos

:bufdo /palavra/ = Procura “palavra” em todos os arquivos abertos /Mari[oa] = Procura por “Mario” ou “Maria”

:e = Abrir arquivo. :! = Executa um comando do shell - :!ls

== :g/^teste/d = Use este comando caso queira deletar todas as linhas que comecem com a palavra “teste”

:%s/foo/bar/g = Este comando encontra todas as ocorrências “foo” no texto inteiro e substitui por “bar”

:s/foo/bar/g = Este comando encontra todas as ocorrências “foo” na linha atual e substitui por “bar”

:%s/foo/bar/gc = Substitui “foo” por “bar” mas pede uma confirmação antes

:%s/<foo>/bar/gc = Substitui apenas palavra inteiras “foo” por “bar” e pede confirmação antes
