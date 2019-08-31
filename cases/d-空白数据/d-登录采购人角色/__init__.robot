*** Settings ***
Library  pages.loginPage.LoginPage    ${dri}
Library  pylib.login

Suite Setup  run keywords    open url    AND    login  tz_cgr  12345678
Suite Teardown  del cookie