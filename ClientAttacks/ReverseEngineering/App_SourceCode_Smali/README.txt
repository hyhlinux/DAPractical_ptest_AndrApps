ON DEMAND GEnerierung:

--> Erstellte Ordner sind recht groß (pro app zwischen 30-80 MB) --> deshalb on Demand generierung:

Im "~\DAPractical_ptest_AndrApps\ClientAttacks\ReverseEngineering" - Ordner folgender command:

java -jar  App_SourceCode_Smali\baksmali-2.2.0.jar disassemble App_APKs\yourMDApp.apk -o App_SourceCode_Smali\yourMD_smali_DecompSourceCode

Folder "yourMD_smali_DecompSourceCode" ist dann in "App_SourceCode_Smali" zu finden


