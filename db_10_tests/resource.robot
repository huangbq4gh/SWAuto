*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.
Library           Selenium2Library
Library           ../lib/ADBOperations.py
Library           ../lib/ScreenVerification.py

*** Variables ***
${DELAY}          0
${BattleBtnX}     600
${BattleBtnY}     650
${SellBtnX}       410
${SellBtnY}       590
${RuneGetBtnX}    770
${RuneGetBtnY}    600
${SellYesBtnX}    400
${SellYesBtnY}    450
${ReplayBtnX}     200
${ReplayBtnY}     400
${DStartBtnX}     1050
${DStartBtnY}     500
${MapDungeonX}    650
${MapDungeonY}    650
${DragonLairX}    200
${DragonLairY}    400
${Level10X}       1000
${Level10Y}       600
${NonRuneOKX}     600
${NonRuneOKY}     600
${RuneStarPtX}    442
${RuneStarPtY}    242
${RuneQPtX}       820
${RuneQPtY}       250
${StartAdsCloseX}  115
${StartAdsCloseY}  660
${StartAppX}      90
${StartAppY}      660

*** Keywords ***
Start app
    Input Tap  ${StartAppX}  ${StartAppY}
    Sleep  60
    Close All Startads

Start DB10
    Input Tap  ${BattleBtnX}  ${BattleBtnY}
    Input Tap  ${MapDungeonX}  ${MapDungeonY}
    Input Tap  ${DragonLairX}  ${DragonLairY}
    Input Tap  ${Level10X}  ${Level10Y}
    Input Tap  ${DStartBtnX}  ${DStartBtnY}
    Sleep  4 minutes 30 seconds
    Input Tap  500  500
    Input Tap  500  500
    Sleep  5


Restart DB10
    Input Tap  ${ReplayBtnX}  ${ReplayBtnX}
    Input Tap  ${DStartBtnX}  ${DStartBtnY}
    Sleep  4 minutes 30 seconds
    Input Tap  500  500
    Input Tap  500  500
    Sleep  5


