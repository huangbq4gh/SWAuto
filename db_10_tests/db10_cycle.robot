*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
#db10_initialization
#    Start DB10
#
#dungeon_restart
#    Restart DB10

initialization
    Close All Startads