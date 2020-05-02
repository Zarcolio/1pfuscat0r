# About 1pfuscat0r
A tool to automatically generate alternative IP representations, a rewritten version of IPFuscator: https://github.com/vysecurity/IPFuscator

# Why 1pfuscat0r
With 1pfuscat0r is easy to generate obfuscated versions based on IP addresses provided through standard input. It's easy to redirect the contents of a file with several IP addresses to this tool. The output is  clean so it can be redirected to another tool.

# Install
1pfuscat0r should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running 1pfuscat0r, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: 1pfuscat0r [-h] [-i <ipaddress>] [-o <file>]

Use 1pfuscat0r to obfuscate a given IP address. Either supply an IP as an argument or through standard input. By default valid and invalid IP addresses are shown.

optional arguments:
  -h, --help      show this help message and exit
  -i <ipaddress>  Supply a valid IP address to obfuscate
  -o <file>       Supply an output file
```
# Examples
Want to convert multiple IP addresses and save output in a separate file:
```
cat ipaddresses.txt|1pfuscat0r -o output.txt 
```
Want to search for communication invites with yandex but leave site: out of the query? Just use the following command:
```
sitedorks -cat comm -site disable -engine yandex -query uber
```
# Contribute?
Do you have some usefull additions to the script or to the list of dorkable websites, please send in a pull request to help make this script better :)
