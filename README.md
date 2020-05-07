# About 1pfuscat0r
A tool to automatically generate alternative IP representations, a rewritten version of IPFuscator: https://github.com/vysecurity/IPFuscator

# Why 1pfuscat0r
With 1pfuscat0r is easy to generate obfuscated versions based on IP addresses. Improvents are:
* provide IP addresses through standard input. It's easy to redirect the contents of a file with several IP addresses to this tool.
* The output is clean so it can be redirected to another tool.
* If the target tool of choice doesn't have support for delays, this script does.
* And it's written for Python 3.

# Install
1pfuscat0r should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running 1pfuscat0r, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: 1pfuscat0r [-h] [-i <ipaddress>] [-o <file>]

Use 1pfuscat0r to obfuscate a given IP address. Either supply an IP address as an argument or through standard input. 
By default valid and invalid IP addresses are shown.

optional arguments:
  -h, --help      show this help message and exit
  -d <seconds>    Supply a delay in seconds.
  -i <ipaddress>  Supply a valid IP address to obfuscate
  -o <file>       Supply an output file
```
# Examples
Want to convert multiple IP addresses and save output in a separate file:
```
cat ipaddresses.txt|1pfuscat0r -o output.txt 
```
Want to convert multiple IP addresses and redirect it to a tool that doesn't take input from standard input, for example ping?
Install [2cmd](https://github.com/Zarcolio/2cmd) and create 1pfuscat0r-ping.2cmd:
```
ping $2cmd$ -c 1
```
And run the following command:

```
cat ipaddresses.txt|1pfuscat0r|2cmd 1pfuscat0r-ping.2cmd
```

# Contribute?
Do you have some usefull additions to the script, please send in a pull request to help make this script better :)
