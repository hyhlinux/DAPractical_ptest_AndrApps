#!/usr/bin/env python
#Copyright Thomas Stipsits
#26.04.2017
import os


print("Specify the whole path to your apk -- NOT Including the Apkname --> e.g. 'C:/test/'")
path = input("APK-Path:")
print("Specify the whole name of your apk -- NOT Including the Path or the .apk --> e.g. 'testapk' NOT 'testapk.apk'")
apkname = input("APK-Name")



os.system('enjarify ' + path+apkname+".apk");
os.system('move ' path+apkname+"-enjarify.jar ");

print("SMALI integration is not implemented yet")
