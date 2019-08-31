*** Settings ***
Library  pages.cartPage.CartPage    ${dri}
Library  pylib.login
*** Test Cases ***
清空购物车 - tc00001
    open addproducturl
    delete products