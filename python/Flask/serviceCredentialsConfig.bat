@echo off
cls
set /p user=Enter Default Database Username:
powershell -Command $pword = read-host "Enter Default Database password" -AsSecureString ; $BSTR=[System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pword) ; [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR) > .tmp.txt & set /p password=<.tmp.txt & del .tmp.txt
python -c "import serviceCredentialsConfig;serviceCredentialsConfig.encrypt('%user%','%password%')"
echo Would you like to add other server?(Y/N)
set INPUT=
set /P INPUT=Type input: %=%
If "%INPUT%"=="y" goto yes 
If "%INPUT%"=="n" goto no
If "%INPUT%"=="Y" goto yes
If "%INPUT%"=="N" goto no
:yes
set /p user=Enter other Database Username:
powershell -Command $pword = read-host "Enter other Database password" -AsSecureString ; $BSTR=[System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pword) ; [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR) > .tmp.txt & set /p password=<.tmp.txt & del .tmp.txt
python -c "import serviceCredentialsConfig;serviceCredentialsConfig.encrypt1('%user%','%password%')"
:no
pause
exit
