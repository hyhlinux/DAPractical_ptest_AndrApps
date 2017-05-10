#!/usr/bin/env python
import os
import shutil
saveFilename = "ResultFiles/appIDs_Part"
mergedSaveFilename = "ResultFiles/appInfoWithPermissions_Part"
#appList

appIDList=[]
permissionList = ['prmissionString',appIDList];
dataList = [];

print(len(dataList))
for a in dataList:
	print(a[0]+"\n")
	for b in a[1]:
		print("\t"+ b + ", "+ str(counter));
		counter = counter+1;


#inputNumberOfAppsToCrawl = int(input("How many crawling result do you want?"))
#print(inputNumberOfAppsToCrawl)
#Crawl Store & store crawled apps in junkfile
#crawlCounter=0
#tempCrawlString=""
#print (inputNumberOfAppsToCrawl%100)
#while (inputNumberOfAppsToCrawl%100) >= crawlCounter:
#	crawlCounter=crawlCounter+1
#	os.system("node crawlMedicalApps.js 100 "+str(crawlCounter*100)+" > ResultFiles/tempAppCrawlData.txt")
#	tempCrawlFile = open("ResultFiles/tempAppCrawlData.txt",'r')#ReadTemporary crawlingValue
#	tempList = tempCrawlFile.readlines()
#	for tempDataline in tempList:
#		tempCrawlString = tempCrawlString+tempDataline
#		print(tempDataline)
#	#shutil.rmtree('ResultFiles/tempAppCrawlData.txt')
#
#Open up File of crawled App Informations
#
#testFile = open("ResultFiles/test.txt",'w')
#testFile.write(tempCrawlString)
#
#testFile.close()







#permissionList ={
#				"add or remove accounts":'android.permission.MANAGE_ACCOUNTS',
#				"read calendar events plus confidential information":'android.permission.READ_CALENDAR',
#				"add or modify calendar events and send email to guests without owners knowledge":'android.permission.WRITE_CALENDAR',
#				"read your contacts":'android.permission.READ_CONTACTS',
#				"approximate location (network-based)":'android.permission.ACCESS_COARSE_LOCATION',
#				"send SMS messages":'android.permission.SEND_SMS',
#				"directly call phone numbers":'android.permission.CALL_PHONE',
#				"read the contents of your USB storage":'android.permission.READ_EXTERNAL_STORAGE',
#				"modify or delete the contents of your USB storage":'android.permission.WRITE_EXTERNAL_STORAGE',
#				"take pictures and videos":'android.permission.CAMERA',
#				"view Wi-Fi connections":'android.permission.ACCESS_WIFI_STATE',
#				"view network connections":'android.permission.ACCESS_NETWORK_STATE',
#				"delete all app cache data":'android.permission.CLEAR_APP_CACHE',
#				"full network access":"???_full network access_???",
#				"enable app debugging":'android.permission.SET_DEBUG_APP',
#				"use accounts on the device":'android.permission.USE_CREDENTIALS',
#				"control vibration":'android.permission.VIBRATE',
#				"prevent device from sleeping":'android.permission.WAKE_LOCK',
#				"Google Play license check":'com.android.vending.CHECK_LICENSE',
#				"receive data from Internet":'android.permission.INTERNET',
#				"change your audio settings":'android.permission.MODIFY_AUDIO_SETTINGS'}
				