*** Settings ***
Variables  auth_vars.py
Library  CrlCpLib.py    ${BASE_URL}   ${USERNAME}     ${PASSWORD}
Suite Setup     CHECK CREDENTIALS   # Checks if we can login to the given url with auth vars. If this fails no test will run

*** Variables ***
${BASE_URL}   https://prometheus.desy.de/Users/${USERNAME}/Private/

${FILE_DIR}     /home/andy/
${FILE_NAME}    CMSCalorimeter.png


*** Test Cases ***
FILE COPY
    COPY FILE TO    ${FILE_DIR}${FILE_NAME}   ${FILE_NAME}
    STATUS CODE SHOULD BE   201

FILE DELETE
    DELETE FILE  ${FILE_NAME}
    STATUS CODE SHOULD BE  204

FILE DOWNLOAD
    DOWNLOAD FILE AS    testfile     ${FILE_DIR}testfile
    STATUS CODE SHOULD BE   200

