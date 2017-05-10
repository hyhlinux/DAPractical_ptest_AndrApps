#!/usr/bin/env python
#Copyright Thomas Stipsits
#26.04.2017
import os
PermissionFileList	={}	
permissionList ={};
permissionDataList = [];
appList = []
appIDList=[]
appDataList = ['appID','URL','title', 'developer', 'booleanFree', 'Permissions'];
permissionList = ['permissionString',appIDList];


seperator = "--------------------------------------------------------------------------------------\n"
permissionIndexCounter=-1;
saveFilename = "ResultFiles/appIDs_Part"
mergedSaveFilename = "ResultFiles/appInfoWithPermissions_Part"

overviewPermFile = open("foundPermissionOverview.txt", 'w')
detailedPermFile = open("foundPermissionDetail.txt", 'w')
overviewPermFile.write(seperator);
detailedPermFile.write(seperator);



##Write directly Permission Overview File & Process Data for the PermissionDetail File 
def writePermissions(permissionString, appID, pIndexCounter):
	permissionString=permissionString[17:-3] #--> Strip Permissionstring from pre/suffixes
	#-----------------------------------------------------------------------------------------------------------
	#Write all found permissions into a permission file (Overview for all permissions, only once per permission)
	#-----------------------------------------------------------------------------------------------------------
	if  permissionString not in PermissionFileList:	
		##Only enters here if permission is new (no corresponding permissionString in PermissionFileList)
		#-----------------
		#Register permissionString in helpDictionary (so we know from now on that we 
		#already know that permission and what position it has in the permission Dictionary)
		#-----------------
		helpDict = {permissionString:pIndexCounter};
		#-----------------
		#Increment counter after registering old value
		#-----------------
		pIndexCounter=pIndexCounter+1
		#-----------------
		#Update PermissionDictionary with the created helpDictionary
		#-----------------
		PermissionFileList.update(helpDict);
		#-----------------
		#Write Permission String to Permission Overview File
		#-----------------
		overviewPermFile.write(permissionString+"\n");
		
		##-----------------------------------------------------------------------------------------------------------
		## Fancy Stuff comes now: Build up a 3D Structure:
		##			appIDList --> holds a number of app IDS (that correspond to a certain permission)
		##			permissionList --> holds permissionString and the List with the corresponding appIDs
		##			permissionDataList --> holds the permissionList of ALL permissions processed 
		##				--> In order to find certain permission again load indes number from the permission dictionary
		##-----------------------------------------------------------------------------------------------------------
		#Re-Instantiate Variable every iteration to prevent overwriting
		appIDList=[];
		permissionList=['permissionString',appIDList];
		appIDList.append(appID);
		permissionList[0]=permissionString;
		permissionList[1]=appIDList;
		permissionDataList.append(permissionList);
	else:
	##Only enters here if permission is NOT new (corresponding permissionString in PermissionFileList)
		#get permission Index from Dictionary
		index = PermissionFileList.get(permissionString)
		#Evaluate if given permissionstring really matches permissionString obtained by the 3D-Structure
		if permissionDataList[index][0] == permissionString:	#index 0 of List that is contained in permissionDataList[index] --> ['permissionString',appIDList], 
			permissionDataList[index][1].append(appID)			#this means we got the right indes from the Permission in the list
		else:
			raise Exception("Corresponding Permission Entry in permissionList Mismatched.")
	#return formerly updaten counter (If permission was new)
	return pIndexCounter
	#-----------------------------------------------------------------------------------------------------------
	#-------------------------------------------EOFunction------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------
	
##Simply writed Data from 3D-Permission Structure to permissionDetail file	
def writeDetailedPermissionFile():
	for pdList in permissionDataList:
		detailedPermFile.write(pdList[0]+"\n\n")
		for appEntry in pdList[1]:
			detailedPermFile.write("\t"+ appEntry+"\n");
		detailedPermFile.write(seperator+"\n");
	detailedPermFile.write(seperator+"\n");
	

			
#inputNumberOfAppsToCrawl = int(input("How many crawling result do you want?"))
#--------------------------------------------------------------------------------
###NON-Functioning --> Reworked Version in pythonTest.py Script --> Problem: Encoding fucks up the conversion --> Manual conversion till now
#Crawl Store & store crawled apps in junkfile
#if inputNumberOfAppsToCrawl>100
#	crawlCounter=0
#	tempCrawlString=""
#	while inputNumberOfAppsToCrawlcrawl%100>Counter
#		os.system("node crawlMedicalApps.js 100 "+counter" > ResultFiles/tempAppCrawlData.txt")
#		tempCrawlFile = open('ResultFiles/tempAppCrawlData.txt', 'r')#ReadTemporary crawlingValue
#		tempList = tempCrawlFile.readlines()
#		for tempDataline in tempList:
#			tempList = tempList+tempCrawlString
#Open up File of crawled App Informations
#crawledAppDataFile = open('ResultFiles/tempAppCrawlData.txt', 'r')
#
#crawledAppDataFile = open('Data/tempAppCrawlData.txt', 'r')
#
#crawledDataList = crawledAppDataFile.readlines()
#print("Document has ", len(crawledDataList),  "lines")
#--------------------------------------------------------------------------------

##________________________________________________________________________________________________________________________________________________________________________
							##TEMPORARY SOLUTION --> WILL BE REPLACED BY ABOVE COMMENT SECTION
##________________________________________________________________________________________________________________________________________________________________________
##--------------------------------------------------------------------------------
##Load Data From external Storage --> Temporary till encoding problem is solved
##--------------------------------------------------------------------------------
mockDataFilename = "Data/AppCrawlDataPart"
dataFilesCounter=1
crawledDataList=""
if os.path.exists(mockDataFilename+str(dataFilesCounter)+".txt"):
	while os.path.exists(mockDataFilename+str(dataFilesCounter)+".txt"):
		print("Trying to load Data from the files...")
		print("Data Part",dataFilesCounter,"exists and has been loaded")
		dataFile = open(mockDataFilename+str(dataFilesCounter)+".txt")
		if dataFilesCounter == 1:
			crawledDataList = dataFile.readlines()
		else:
			tempDataList = dataFile.readlines()
			for dataFileLine  in tempDataList:
				crawledDataList.append(dataFileLine)
		dataFilesCounter=dataFilesCounter+1
else:
	raise Exception("NO DATA FILES FOUND!!")
	
inputNumberOfAppsToCrawl = 200
##--------------------------------------------------------------------------------
##________________________________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________________________________
							#Determine Filename For Storing the Data Obtained by Crawling the Play Stores App List
#________________________________________________________________________________________________________________________________________________________________________
appInformationPartCounter=1
while os.path.exists((saveFilename+str(appInformationPartCounter))):
	print("Trying to save your parsed Data to file...")
	print("File Part",appInformationPartCounter,"already exists, continuing with Part", appInformationPartCounter+1)
	appInformationPartCounter=appInformationPartCounter+1
saveFile = open((saveFilename+str(appInformationPartCounter)+".txt"), 'w')
print("Your parsed Data has been saved to file:", (saveFilename+str(appInformationPartCounter)))


#________________________________________________________________________________________________________________________________________________________________________
							#Determine Filename For Storing the Data Obtained by Crawling the Play Stores App List
#________________________________________________________________________________________________________________________________________________________________________

mergedFilePartCounter=1
while os.path.exists((mergedSaveFilename+str(mergedFilePartCounter))):
	print("Trying to save your parsed Data to file...")
	print("File Part",appInformationPartCounter,"already exists, continuing with Part", mergedFilePartCounter+1)
	mergedFilePartCounter=mergedFilePartCounter+1
mergedSaveFile = open((mergedSaveFilename+str(mergedFilePartCounter)+".txt"), 'w')
print("Your parsed Data has been saved to file:", (mergedSaveFilename+str(mergedFilePartCounter)))

#________________________________________________________________________________________________________________________________________________________________________
														#Initialize Variables
#________________________________________________________________________________________________________________________________________________________________________
#Initialize Variables
appcounter = 0
appURL=""
mergedSaveFile.write(seperator+"\n")
permissioncounter=0 ##Used to Display how many permissions the app has
permissionIndexCounter=0; ##Used to Determine the Index of the Permission in the PermissionList (See beginning of file) 
#________________________________________________________________________________________________________________________________________________________________________
													#Start processing Data
												#CheckAppDatalist for keywords
#________________________________________________________________________________________________________________________________________________________________________
										
for dataline in crawledDataList:
	if "appId:" in dataline:
		appDataList = ['appID','URL','title', 'developer', 'booleanFree', 'Permissions'];		#Renew AppDataList --> If not your gonna overwrite old App Instances!!
		appDataList[0]="\t\tAppID:\t\t\t\t\t"+dataline[12:-3]+"\n";								#Write AppID to AppDataList
		permissionString="\t\tPermissions: \n" 													#New App has been found: clear permission list
		appIDString ='"'+dataline[12:-3]+'"' 													#Strip prefix & suffix from appID for executing shell cmd
		saveFile.write(dataline)																#Write AppIDS to the according File
		print("Processing App:" +appIDString + " ... its the " + str(appcounter) +"th/"+str(inputNumberOfAppsToCrawl))														
		os.system('node permissionCrawler.js '+appIDString+" > ResultFiles/tempPermissions.txt")#Conduct permission crawl on AppID
		permFile = open("ResultFiles/tempPermissions.txt")										#specify a tmporary permission file(filled with all permissions of the according app)
		permList = permFile.readlines()
		for permissionDataline in permList:
			if "permission:" in permissionDataline:
				permissioncounter = permissioncounter+1 
				permissionIndexCounter = writePermissions(permissionDataline,appIDString, permissionIndexCounter)	#Call Writepermission Function
				permissionString = permissionString + "\t\t\t"+permissionDataline[17:-3]+"\n"   #Add each permission to permission String 
			else:
				continue
		permissionString = permissionString + "\t\tNumber of actual Permissions:" +str(permissioncounter)+"\n"
		permissioncounter = 0
		appDataList[5]=permissionString;#APLLIST ENTRY 6										#Add permissionString to the app Entry
	else:
		if "url:" in dataline: 
			appURL = "\t\tPlay-Store URL:\t\t\t"+dataline[10:-3]+"\n"							#Strip URL from pre-&suffix
			appDataList[1]=appURL;																#APLLIST ENTRY 2 -- add url to list
		else:
			if "title:" in dataline: 
				appDataList[2]="\t\tTitle:\t\t\t\t\t"+ dataline[12:-3]+"\n";					#APLLIST ENTRY 3 -- add title to list	
			else:
				if "developer:" in dataline: 
					appDataList[3]="\t\tDeveloper:\t\t\t\t" + dataline[16:-3]+"\n";				#APLLIST ENTRY 4 -- add developer to list
				else:
					if "free:" in dataline: 													#Free is last Entry in App Details section --> Wrapp up and write it in output file
						appDataList[4]=("\t\tApp is Free(No Costs):\t" + dataline[10:-4]+"\n"); #APLLIST ENTRY 5 -- add free boolean to list
						appList.append(appDataList)
						appcounter=appcounter+1
					else:
						continue
appcounter=0			
for app in appList:
	appcounter=appcounter+1;	
	mergedSaveFile.write("App-Nr."+str(appcounter)+":\n")				
	for dataline2 in app:											#Write Applist to merged File (AppInformation File merged with Permissions)
		mergedSaveFile.write(dataline2)
	mergedSaveFile.write(seperator+"\n")
#________________________________________________________________________________________________________________________________________________________________________
												#Close all files, delete Tempfiles
#________________________________________________________________________________________________________________________________________________________________________
										
					
dataFile.close()																			
saveFile.close()
permFile.close()
os.remove("ResultFiles/tempPermissions.txt")
mergedSaveFile.close()
overviewPermFile.write(seperator);
overviewPermFile.close()
writeDetailedPermissionFile()
detailedPermFile.close()


