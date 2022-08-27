class Node:

    #element = element path
    #type = CSS, XPATH, ID, NAME
    #mouse_action = Click, doubleClick, Click and Hold, drag and drop, right click, moveToElement
    #Keyboard_action = SendKeys, KeyUp, KeyDown
    def __init__(self, url, element, element_type, mouse_action, keyboard_action):
        self.url = url
        self.element = element
        self.element_type = element_type
        self.mouse_action = mouse_action
        self.keyboard_action = mouse_action

    
    