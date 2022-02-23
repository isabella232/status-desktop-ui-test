#******************************************************************************
# Status.im
#*****************************************************************************/
#/**
# * \file    AccountsPopup.py
# *
# * \date    February 2022
# * \brief   It defines the status accounts popup behavior and properties.
# *****************************************************************************/

from drivers.SquishDriver import *
from drivers.SquishDriver import StatusAccountsPopupComponents as component

#It defines the status accounts popup behavior and properties.
class AccountsPopup():    
    __is_loaded = False
    __accountsList = None
    
    def __init__(self):
        [self.__is_loaded, self.__accountsList] = is_loaded_visible_and_enabled(component.ACCOUNTS_POPUP.value)
        
    def is_loaded(self): 
        return self.__is_loaded
    
    def find_account(self, account):
        [found, account_obj] = self.__find_account(account)
        return found
    
    def select_account(self, account):
        [found, account_obj] = self.__find_account(account)
        if found:
            return click_obj(account_obj)       
        return found
    
    def __find_account(self, account):
        found = False
        account_obj = None
        for index in range(self.__accountsList.count):
            a = self.__accountsList.itemAtIndex(index)
            if(a.username == account):
                account_obj = a
                found = True
                break        
        return found, account_obj