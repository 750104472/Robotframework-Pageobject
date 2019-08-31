
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH
import pdb

class CartPage(Base):

    locator = ParseConfig(LOCATOR_PATH)

    url = locator('TestUrl', 'carturl')
    addproducturl = locator('TestUrl', 'addproducturl')
    shopcar_delbuttons = locator('CartPage', 'shopcar_delbuttons')

    def open_url(self):
        self.open(self.url)

    def open_addproducturl(self):
        self.open(self.addproducturl)
        self.logger.info("购物车已添加商品！")

    def delete_buttons(self):
        is_product = self.is_element_exist(*self.shopcar_delbuttons)
        return is_product

    def delete_products(self):
        try:
            if self.delete_buttons() == False:
                self.logger.info("购物车已清空！")
            else:
                eles = self.find_elements(*self.shopcar_delbuttons)
                for ele in eles:
                    ele.click()
                    self.accept_alert()
                self.logger.info("购物车已清空！")

        except Exception as e:
            self.logger.info("%s"%e)




if __name__ == '__main__':
    pass
