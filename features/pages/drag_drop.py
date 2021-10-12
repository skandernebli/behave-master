from selenium.webdriver import ActionChains

from Browser import Browser

objectToDrag = "draggable"
val_x = 120
val_y = 30

val_x_slide = 131

class dragdrop(Browser):

    def drag(self):
        source = self.driver.find_element_by_id(objectToDrag)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source, val_x, val_y).perform()


    def affi(self):
        target1 = self.driver.find_element_by_id('droppable')
        return target1


    def setup(self,link):
        self.driver.get(link)



    def slid(self):
        elm = self.driver.find_element_by_xpath("//input[@value='0']")
        move = ActionChains(self.driver)
        move.click_and_hold(elm).move_by_offset(val_x_slide, 0).release().perform()

    def affich_slid(self):
        maval = self.driver.find_element_by_id('range')
        return maval


