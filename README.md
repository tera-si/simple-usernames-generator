# simple-usernames-generator
A Python3.6+ script that generate a bunch of usernames from a list of full names.

Once in a CTF I need a tool that would generate a bunch of usernames from a list of full names. I was too lazy to search through the internet/Kali repository, so I just wrote one. Later I found myself using it quite often, and it has served me quite well, so I decided to freshen it up abit, with slightly better code quality and slightly more features (although still simple in nature).

So here it is.

# Customisation

At the moment the script is using `["", "-", "_", "."]` as delimiters. You can edit this part of the script to change them to suit your needs:

```
# Feel free to modify them
delimiters = ["", "-", "_", "."]
```

# Usage

```
$ python3 generator.py -h
usage: generator.py [-h] [-c] name_list [output_file]

Generate a list of simple usernames from a list of full names.

positional arguments:
  name_list    A list of full names. Each full name must be on a new line; first and last name
               must be separated by a space; middle names are ignored.
  output_file  File name for the output file, optional. If none are provided, will output to
               STDOUT.

options:
  -h, --help   show this help message and exit
  -c, --case   Enable case sensitive mode. If enabled, generated usernames will contain basic
               variations in upper and lowercase. Off by default, preserving original casing.
```

## Example Usages and Output

First prepare a list of full names, where each full name is on a new line, and the first and last names are all separated by a space.

```
$ cat names.txt
Biggus Dickus
Holy Hand Grenade
```

### Output to STDOUT with simple variations

```
$ python3 generator.py names.txt
##################################################
# Potential Usernames Generator v1.0             #
# By terasi                                      #
# https://github.com/tera-si                     #
##################################################

[*] Using delimiters: ['', '-', '_', '.']
==================================================
BiggusDickus
DickusBiggus
BDickus
DBiggus
BiggusD
DickusB
BD
DB
Biggus-Dickus
Dickus-Biggus
B-Dickus
D-Biggus
Biggus-D
Dickus-B
B-D
D-B
Biggus_Dickus
Dickus_Biggus
B_Dickus
D_Biggus
Biggus_D
Dickus_B
B_D
D_B
Biggus.Dickus
Dickus.Biggus
B.Dickus
D.Biggus
Biggus.D
Dickus.B
B.D
D.B
HolyGrenade
GrenadeHoly
HGrenade
GHoly
HolyG
GrenadeH
HG
GH
Holy-Grenade
Grenade-Holy
H-Grenade
G-Holy
Holy-G
Grenade-H
H-G
G-H
Holy_Grenade
Grenade_Holy
H_Grenade
G_Holy
Holy_G
Grenade_H
H_G
G_H
Holy.Grenade
Grenade.Holy
H.Grenade
G.Holy
Holy.G
Grenade.H
H.G
G.H
```

### Output to STDOUT with case variations

```
$ python3 generator.py names.txt -c
##################################################
# Potential Usernames Generator v1.0             #
# By terasi                                      #
# https://github.com/tera-si                     #
##################################################

[*] Using delimiters: ['', '-', '_', '.']
==================================================
biggusdickus
Biggusdickus
biggusDickus
BiggusDickus
dickusbiggus
Dickusbiggus
dickusBiggus
DickusBiggus
bdickus
Bdickus
bDickus
BDickus
dbiggus
Dbiggus
dBiggus
DBiggus
biggusd
Biggusd
biggusD
BiggusD
dickusb
Dickusb
dickusB
DickusB
bd
Bd
bD
BD
db
Db
dB
DB
biggus-dickus
Biggus-dickus
biggus-Dickus
Biggus-Dickus
dickus-biggus
Dickus-biggus
dickus-Biggus
Dickus-Biggus
b-dickus
B-dickus
b-Dickus
B-Dickus
d-biggus
D-biggus
d-Biggus
D-Biggus
biggus-d
Biggus-d
biggus-D
Biggus-D
dickus-b
Dickus-b
dickus-B
Dickus-B
b-d
B-d
b-D
B-D
d-b
D-b
d-B
D-B
biggus_dickus
Biggus_dickus
biggus_Dickus
Biggus_Dickus
dickus_biggus
Dickus_biggus
dickus_Biggus
Dickus_Biggus
b_dickus
B_dickus
b_Dickus
B_Dickus
d_biggus
D_biggus
d_Biggus
D_Biggus
biggus_d
Biggus_d
biggus_D
Biggus_D
dickus_b
Dickus_b
dickus_B
Dickus_B
b_d
B_d
b_D
B_D
d_b
D_b
d_B
D_B
biggus.dickus
Biggus.dickus
biggus.Dickus
Biggus.Dickus
dickus.biggus
Dickus.biggus
dickus.Biggus
Dickus.Biggus
b.dickus
B.dickus
b.Dickus
B.Dickus
d.biggus
D.biggus
d.Biggus
D.Biggus
biggus.d
Biggus.d
biggus.D
Biggus.D
dickus.b
Dickus.b
dickus.B
Dickus.B
b.d
B.d
b.D
B.D
d.b
D.b
d.B
D.B
holygrenade
Holygrenade
holyGrenade
HolyGrenade
grenadeholy
Grenadeholy
grenadeHoly
GrenadeHoly
hgrenade
Hgrenade
hGrenade
HGrenade
gholy
Gholy
gHoly
GHoly
holyg
Holyg
holyG
HolyG
grenadeh
Grenadeh
grenadeH
GrenadeH
hg
Hg
hG
HG
gh
Gh
gH
GH
holy-grenade
Holy-grenade
holy-Grenade
Holy-Grenade
grenade-holy
Grenade-holy
grenade-Holy
Grenade-Holy
h-grenade
H-grenade
h-Grenade
H-Grenade
g-holy
G-holy
g-Holy
G-Holy
holy-g
Holy-g
holy-G
Holy-G
grenade-h
Grenade-h
grenade-H
Grenade-H
h-g
H-g
h-G
H-G
g-h
G-h
g-H
G-H
holy_grenade
Holy_grenade
holy_Grenade
Holy_Grenade
grenade_holy
Grenade_holy
grenade_Holy
Grenade_Holy
h_grenade
H_grenade
h_Grenade
H_Grenade
g_holy
G_holy
g_Holy
G_Holy
holy_g
Holy_g
holy_G
Holy_G
grenade_h
Grenade_h
grenade_H
Grenade_H
h_g
H_g
h_G
H_G
g_h
G_h
g_H
G_H
holy.grenade
Holy.grenade
holy.Grenade
Holy.Grenade
grenade.holy
Grenade.holy
grenade.Holy
Grenade.Holy
h.grenade
H.grenade
h.Grenade
H.Grenade
g.holy
G.holy
g.Holy
G.Holy
holy.g
Holy.g
holy.G
Holy.G
grenade.h
Grenade.h
grenade.H
Grenade.H
h.g
H.g
h.G
H.G
g.h
G.h
g.H
G.H
```

### Output to Files

```
$ python3 generator.py names.txt out.txt
##################################################
# Potential Usernames Generator v1.0             #
# By terasi                                      #
# https://github.com/tera-si                     #
##################################################

[*] Using delimiters: ['', '-', '_', '.']
==================================================
[*] Output to file out.txt successful
```
