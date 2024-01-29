# M.O.A.F.A.S.T.
![MOAFAST](https://gainsec.com/wp-content/uploads/2024/01/bottlecap.png)

Quick script to automate some basic tasks done during a OSX Thick Client or Software Penetration Test. Checks for things like ARC, PIE, Canary, Codesignature Flags, NSFileProtect, Signature and more.

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

* Create output template rather then have unique 3 line print statements in each function
* Add function to add / to output directory
* add function to create output directory
* add function to run against all files in a dir
* ??

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details


## Example and How To

* ./moafast-v1 --o ~/Desktop/Engagements/GainSec/Thick-Client/Output/ --f GainSec.app/Contents/MacOS/GainSec

OR 

* python3 moafast-v1.py --o ~/Desktop/Engagements/GainSec/Thick-Client/Output/ --f GainSec.app/Contents/MacOS/GainSec