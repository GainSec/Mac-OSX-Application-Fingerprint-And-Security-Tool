#!/usr/bin/python3

import subprocess
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('--f', help='OSX Application File')
parser.add_argument('--v', action='store_true', help='Print Cleaned Output')
parser.add_argument('--vv', action='store_true', help='Print Raw Output')
parser.add_arugment('--o', help='Output Directory')

args = parser.parse_args()

f = args.f
v = args.v
vv = args.vv
o = args.o

'''
Not needed atm 
ff= (f+'.app')
'''

def PIECheck():
    with open(o+'pieout.txt','w+') as fout:
        with open(o+'pieerr.txt','w+') as ferr:
            out=subprocess.run(["otool","-hv", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("PIE",rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("PIE is not set; You've got a finding!")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("PIE is set; No Finding")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
        elif vv is True:
            print(rawoutput)

 #   print(output)
 #   print(v)
#    print(errors)

def ARCCheck():
    with open(o+'arcout.txt','w+') as fout:
        with open(o+'arcerr.txt','w+') as ferr:
            out=subprocess.run(["nm", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("_objc_release",rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("ARC is not set; You've got a finding!")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("ARC is set; No Finding")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
        elif vv is True:
            print(rawoutput)

def CanaryCheck():
    with open(o+'canout.txt','w+') as fout:
        with open(o+'canerr.txt','w+') as ferr:
            out=subprocess.run(["otool", "-Iv", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search(("stack_chk_fail"),rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("Canary is not set; You've got a finding!")
                print("!-----------------------------------!")
            elif output is not None:
                output1 = re.search(("stack_chk_guard"),rawoutput)
            if output1 == None:
                print("!-----------------------------------!")
                print("Canary is not set; You've got a finding!")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("Canary is set; No Finding")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
            print(output1)
        elif vv is True:
            print(rawoutput)

def NSFileProtectionCheck():
    with open(o+'nsfout.txt','w+') as fout:
        with open(o+'nsferr.txt','w+') as ferr:
            out=subprocess.run(["nm", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("NSFileProtectionComplete",rawoutput)
            if output == None:
                output2 = re.search("NSFileProtectionNone", rawoutput)
                if output2 is not None:
                    print("!-----------------------------------!")
                    print("NSFileProtectionComplete is not set; You've got a finding!")
                    print("!-----------------------------------!")    
            else:
                print("?-----------------------------------?")
                print("NSFileProtection is not utilized; No Finding")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
        elif vv is True:
            print(rawoutput)

def SignatureCheck():
    with open(o+'sigfout.txt','w+') as fout:
        with open(o+'sigferr.txt','w+') as ferr:
            out=subprocess.run(["spctl", "--assess", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            codecheck = out.returncode
           # print(codecheck)
            # save output (if any) in variable
            #rawoutput=fout.read()
            #output = re.search("returncode=3",rawoutput)
            #print(output)
            if codecheck == 0:
                print("!-----------------------------------!")
                print("Signature is set or valid; No Finding!")
                print("!-----------------------------------!")    
            else:
                print("?-----------------------------------?")
                print("Signature is not set or is invalid; Possible finding")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(out)
        elif vv is True:
            print(out)

def DyLibCheck():
    with open(o+'dylout.txt','w+') as fout:
        with open(o+'dylerr.txt','w+') as ferr:
            out=subprocess.run(["otool", "-L", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
           # output = re.search("_objc_release",rawoutput)
            if rawoutput == None:
                print("!-----------------------------------!")
                print("DYLibs not found; Check Syntax!!")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("Dylibs saved to dylout.txt")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(rawoutput)
        elif vv is True:
            print(rawoutput)

def EntitlmentsCheck():
    with open(o+'entout.txt','w+') as fout:
        with open(o+'enterr.txt','w+') as ferr:
            out=subprocess.run(["codesign", "-d", "--entitlements", "-", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search(("com.apple.security.allow-dyld-environment-variables"),rawoutput)
            output1 = re.search(("com.apple.security.cs.disable-library-validation"),rawoutput)
            output2 = re.search(("get-task-allow"), rawoutput)
            output3 = re.search(("allow-unsigned-executable-memory"), rawoutput)
            output4 = re.search(("files.downloads.read-write"), rawoutput)
            output5 = re.search(("security.device.cameras"), rawoutput)
            if [x for x in (output, output1, output2, output3, output4, output5) if x is None]:
                print("!-----------------------------------!")
                print("No insecure entitlements; Double Check the entout file though!; No Finding")
                print("!-----------------------------------!")
            else:
                print("!-----------------------------------!")
                print("Weak Entitlement:")
                print(output, ' ', output1, ' ', output2, ' ', output3, ' ', output4, ' ', output5)
                print("!-----------------------------------!")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
            print(output1)
        elif vv is True:
            print(rawoutput)

'''
#Need to figure this one out

def EntitlmentsCheck2():
    with open(o+'entout.txt','w+') as fout:
        with open(o+'enterr.txt','w+') as ferr:
            out=subprocess.run(["codesign", "-d", "--entitlements", "-", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
          #  output = re.search(("com.apple.security.allow-dyld-environment-variables"),rawoutput)
           # output1 = re.search(("com.apple.security.cs.disable-library-validation"),rawoutput)
            #output2 = re.search(("get-task-allow"), rawoutput)
            #output3 = re.search(("allow-unsigned-executable-memory"), rawoutput)
            #output4 = re.search(("files.downloads.read-write"), rawoutput)
            #output5 = re.search(("security.device.cameras"), rawoutput)
            entitlesearch = re.compile("(com.apple.security.allow-dyld-environment-variables|com.apple.security.cs.disable-library-validation|get-task-allow|allow-unsigned-executable-memory|files.downloads.read-write|security.device.cameras)")
            output = entitlesearch.findall(rawoutput)
            print(output)
           # if output is not None:
            for hits in output:
                    print("!-----------------------------------!")
                    print("Weak Entitlement:")
                    print(output)
                    print("!-----------------------------------!")
            else:
                print("!-----------------------------------!")
                print("No insecure entitlements; Double Check the entout file though!; No Finding")
                print("!-----------------------------------!")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(output)
            print(output1)
        elif vv is True:
            print(rawoutput)
'''

#Ideally this would print the flag value found
def CodeDirectFlagCheck():
    with open(o+'cdfout.txt','w+') as fout:
        with open(o+'cdferr.txt','w+') as ferr:
            out=subprocess.run(["codesign", "-dv", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("flags=0x00000",rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("CodeDirectory Flags are set")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("CodeDirectory Flags are not set properly; finding! ")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(rawoutput)
        elif vv is True:
            print(rawoutput)

def DebugSymbolCheck():
    with open(o+'debugsymfout.txt','w+') as fout:
        with open(o+'debugsymferr.txt','w+') as ferr:
            out=subprocess.run(["dsymutil", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("warning",rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("Debug symbols do not exist; No Finding!")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("Debug symbols exist Flags are set; Finding ")
                print(output)
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(rawoutput)
        elif vv is True:
            print(rawoutput)

def TeamIDCheck():
    with open(o+'tidout.txt','w+') as fout:
        with open(o+'tiderr.txt','w+') as ferr:
            out=subprocess.run(["codesign", "-dv", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            output = re.search("not set",rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("Team Identifier is declared")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("Team Identifier is not declared; Finding! ")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(rawoutput)
        elif vv is True:
            print(rawoutput)

#Ideally this would print the string values
def StringsSensDataCheck():
    with open(o+'stringsout.txt','w+') as fout:
        with open(o+'stringserr.txt','w+') as ferr:
            out=subprocess.run(["strings", f],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            rawoutput=fout.read()
            stringsearch = re.compile("(pass|token|secret|cred|http|api|hash|iv)",re.IGNORECASE)
            output = stringsearch.findall(rawoutput)
            if output == None:
                print("!-----------------------------------!")
                print("No possible sensitive data was found")
                print("!-----------------------------------!")
            else:
                print("?-----------------------------------?")
                print("There may be some sensitive data!; Possible Finding! Grep the stringsout.txt file for further review!")
                print("?-----------------------------------?")
            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()
        if v is True:
            print(rawoutput)
        elif vv is True:
            print(rawoutput)

 #   print(output)
 #   print(v)
    # print(errors)


def Main():
    print(" __  __   ___      _      _____    _      ____ _____         ")
    print("|  \/  | / _ \    / \    |  ___|  / \    / ___|_   _|        ")
    print("| |\/| || | | |  / _ \   | |_    / _ \   \___ \ | |    _____ ")
    print("| |  | || |_| | / ___ \ _|  _|_ / ___ \ _ ___) || |   |_____|")
    print("|_|  |_(_)___(_)_/   \_(_)_| (_)_/   \_(_)____(_)_|          ")
    print("                                                             ")
    print(" __  __               ___  ______  __")
    print("|  \/  | __ _  ___   / _ \/ ___\ \/ /")
    print("| |\/| |/ _` |/ __| | | | \___ \\  / ")
    print("| |  | | (_| | (__  | |_| |___) /  \ ")
    print("|_|  |_|\__,_|\___|  \___/|____/_/\_\"")
    print("                                     ")
    print("    _                _ _           _   _             ")
    print("   / \   _ __  _ __ | (_) ___ __ _| |_(_) ___  _ __  ")
    print("  / _ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \ ")
    print(" / ___ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | |")
    print("/_/   \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|")
    print("        |_|   |_|                                    ")
    print(" _____ _                                  _       _                     _ ")
    print("|  ___(_)_ __   __ _  ___ _ __ _ __  _ __(_)_ __ | |_    __ _ _ __   __| |")
    print("| |_  | | '_ \ / _` |/ _ \ '__| '_ \| '__| | '_ \| __|  / _` | '_ \ / _` |")
    print("|  _| | | | | | (_| |  __/ |  | |_) | |  | | | | | |_  | (_| | | | | (_| |")
    print("|_|   |_|_| |_|\__, |\___|_|  | .__/|_|  |_|_| |_|\__|  \__,_|_| |_|\__,_|")
    print("               |___/          |_|                                         ")
    print(" ____                       _ _           _____           _ ")
    print("/ ___|  ___  ___ _   _ _ __(_) |_ _   _  |_   _|__   ___ | |")
    print("\___ \ / _ \/ __| | | | '__| | __| | | |   | |/ _ \ / _ \| |")
    print(" ___) |  __/ (__| |_| | |  | | |_| |_| |   | | (_) | (_) | |")
    print("|____/ \___|\___|\__,_|_|  |_|\__|\__, |   |_|\___/ \___/|_|")
    print("                                  |___/                     ")
    print("")
    print("")
    print("")
    print("---------------------------------")
    print("By Jon Gaines (@GainSec)")
    print("Managing Consultant @NetSPI")
    print("---------------------------------")
    print("---------------------------------")
    print("Example:")
    print(" ")
    print("./moafast.py --o \'~/Desktop/Engagements/GainSec/Thick-Client/Output/\' --f \'~/Desktop/Engagements/GainSec/Thick-Client/GainSec.app/Contents/MacOS/GainSec\'")
    print("---------------------------------")
    print("---------------------------------")
    PIECheck()
    ARCCheck()
    CanaryCheck()
    NSFileProtectionCheck()
    SignatureCheck()
    DyLibCheck()
    EntitlmentsCheck()
#   EntitlmentsCheck2() ## NOT READY
    CodeDirectFlagCheck()
    TeamIDCheck()
    StringsSensDataCheck()
    DebugSymbolCheck()

Main()

