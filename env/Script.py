from Node import Node
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class Script:
    def __init__(self):
        self.node_list = []
        self.cmd_list = []
        while True:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            create_node(#Node)
            create_cmd(create_node)

    def create_node(element, element_type, mouse_action, keyboard_action):
        node_list.append(Node.__init__(element, element_type, mouse_action, keyboard_action))

    def create_cmd(Node node): 
        "driver.getelement(By.{}, '{}').{}".format(node.element_type, node.element, node.mouse_action)
    def loop_nodes()