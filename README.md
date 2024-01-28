# M.O.A.F.A.S.T.
![MOAFAST](https://gainsec.com/wp-content/uploads/2024/01/bottlecap.png)

Quick script to automate some basic tasks done during a OSX Thick Client or Software Penetration Test. 

## Getting Started

cd /opt/Thick-Client

git clone https://github.com/GainSec/Mac-OSX-Application-Fingerprint-And-Security-Tool

chmod +x moafast-v1.py

### Prerequisites

This was tested on a OSX box and requires the following tools:

nm
otool
strings
spctl
codesign
dsymutil

## Author

* **Jon Gaines** - *Creator* - [GainSec](https://github.com/GainSec) - Managing Consultant @NetSPI

## To Do

* Note it outputs all files to the directory it ran at, I'll fix that shortly.
* Properly print Codedirectory flag
* Change SignatureCheck to not utilize return codes and print raw output properly
* Get EntitlementsCheck2 working

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details


## Example and How To

* ./moafast-v1 --f GainSec.app/Contents/MacOS/GainSec

OR 

* python3 moafast-v1.py --f GainSec.app/Contents/MacOS/GainSec