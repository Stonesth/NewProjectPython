import sys
import os
from os.path import dirname
from selenium.webdriver.common.keys import Keys
from Tools import tools_v000 as tools

# -16 for the name of this project NewProjectPython
save_path = dirname(__file__)[ : -16]

propertiesFolder_path = save_path + "Properties"


def create():
    try :
        projectName = str(sys.argv[1])
        if projectName != '' :
            tools.createFolder(save_path, projectName)

            GitLab_user = tools.readProperty(propertiesFolder_path, 'NewProjectPython', 'GitLab_user=')
            GitLab_password = tools.readProperty(propertiesFolder_path, 'NewProjectPython', 'GitLab_password=')
            tools.openBrowserChrome()
            tools.driver.get('http://github.com/login')

            # user name
            login_field = tools.driver.find_element_by_id('login_field')
            login_field.send_keys(GitLab_user)

            # password
            password = tools.driver.find_element_by_id('password')
            password.send_keys(GitLab_password)

            # Sign in
            sing_in = tools.driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')
            sing_in.click()

            tools.waitLoadingPageByID('start-of-content')

            # New Repository
            tools.driver.get('https://github.com/new')
            tools.waitLoadingPageByID('repository_name')

            repository_name = tools.driver.find_element_by_id('repository_name')
            repository_name.send_keys(projectName)

            # Initialize this repository with a README
            repository_auto_init = tools.driver.find_element_by_id('repository_auto_init')
            repository_auto_init.click()

            # add .gitignore 
            gitignore_list = tools.driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[6]/div[4]/div[2]/details/summary')
            gitignore_list.click()

            gitignore_input = tools.driver.find_element_by_id('context-ignore-filter-field')
            gitignore_input.send_keys('Python')
            gitignore_input.send_keys(Keys.ARROW_DOWN)
            gitignore_input.send_keys(Keys.ENTER)

            # Create Repository
            create_repository_button = tools.driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[6]/button')
            create_repository_button.click()
            
            tools.closeBrowserChrome()

            # open terminal to clone the repository into the folder







    except IndexError as e1:
        print ("You don't place a name for the project") 
    except WindowsError as e2:
        print ("Project : " + projectName + " already exist") 
    

    
# https://www.google.com/search?q=multiple+account+git&rlz=1C1GCEA_frNL817NL817&oq=multiple+account+git&aqs=chrome.0.0l8.7053j0j7&sourceid=chrome&ie=UTF-8
# https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca/
# https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3
# https://adimian.com/blog/2014/10/basic-ldap-actions-using-python/
# https://faq.o2switch.fr/hebergement-mutualise/tutoriels-cpanel/app-python
# https://libraries.io/pypi/pyOutlook
# https://pypi.org/project/pyOutlook/#description
# https://stackoverflow.com/questions/6332577/send-outlook-email-via-python
# https://docs.microsoft.com/en-us/power-automate/flows-teams
# https://fr.beincrypto.com/analyses/2929/decrire-le-mouvement-a-long-terme-dethereum/
# https://fr.tradingview.com/symbols/ETHEUR/technicals/
# https://pro.coinbase.com/trade/ETH-EUR


    # x = 
# ask to have user / name password GitHub
    # txt = input("Type something to test this out: ")
    # Note that in version 3, the print() function
    # requires the use of parenthesis.
    # print("Is this what you just said? " + txt.text() )

create()
# tools.readProperty(propertiesFolder_path, 'NewProjectPython', 'GitLab_password=')