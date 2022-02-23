#******************************************************************************
# Status.im
#*****************************************************************************/
#/**
# * \file    StatusLoginScreen.py
# *
# * \date    February 2022
# * \brief   It defines the status login screen behavior and properties.
# *****************************************************************************/

from enum import Enum
from screens.AccountsPopup import AccountsPopup
from drivers.SquishDriver import *
from drivers.SquishDriver import StatusLoginViewComponents as component

# It defines expected password placeholder text.
class PswPlaceholderTextType(Enum):
    NONE       = None
    CONNECTING = "Connecting..."
    PASSWORD   = "Enter password"

# It defines the status login screen behavior and properties.
class StatusLoginScreen():    
    __is_loaded = False
    __login_view_obj = None
    
    def __init__(self):
        [self.__is_loaded, self.__login_view_obj] = is_loaded_visible_and_enabled(component.MAIN_VIEW.value)
        
    def is_loaded(self): 
        return self.__is_loaded

    def introduce_password(self, password):
        result = False
        if click_obj_by_name(component.PASSWORD_INPUT.value) and type(component.PASSWORD_INPUT.value, password):
            result = True
        return result
    
    def submit_password(self):
        return click_obj_by_name(component.SUBMIT_BTN.value)
        
    def open_accounts_selector_popup(self):
        return click_obj_by_name(component.CHANGE_ACCOUNT_BTN.value)
            
    def get_accounts_selector_popup(self):
        return AccountsPopup()
    
    def get_password_placeholder_text(self):
        result = ""
        [loaded, obj] = is_loaded(component.PASSWORD_INPUT.value)
        if loaded:
            result = obj.placeholderText 
        return result
    
    def get_error_message_text(self): 
        result = ""
        [loaded, obj] = is_loaded_visible_and_enabled(component.ERR_MSG_LABEL.value)
        if loaded:
            result = obj.text 
        return result
        
    def get_expected_error_message_text(self):#, language):
        # NOTE: It could introduce language checkers.
        return "Login failed. Please re-enter your password and try again."
    
    # NOT IMPLEMENTED STUFF:    
    def get_expected_placeholder_text(self, pswPlaceholderTextType):#, language):
        # NOTE: It could introduce language checkers.               
        raise NotImplementedError("TODO: get_expected_placeholder_text method")
    
    def open_generate_new_keys_popup(self):
        raise NotImplementedError("TODO: open_generate_new_keys_popup method")
    
    def get_current_account_name(self):
        raise NotImplementedError("TODO: get_current_account_name method")   
    
    def get_current_identicon(self):
        raise NotImplementedError("TODO: get_current_identicon method") 
        