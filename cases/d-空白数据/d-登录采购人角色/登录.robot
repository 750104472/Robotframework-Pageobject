*** Settings ***
Library  pages.loginPage.LoginPage    ${dri}
Library  pylib.login
*** Test Cases ***
登录采购人角色 - tc00001
   open url
   login    admin    123456
   del cookie