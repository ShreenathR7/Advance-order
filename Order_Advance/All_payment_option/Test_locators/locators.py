# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
   
    Billing = '(//*[@class="fa fa-cc text-orange"])[2]'
    
    Bill  = '(//*[@class="fa fa-circle-o"])[101]'
    
    Branch = 'id_branch'
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = 'select2-emp_select-container'
    
    sales = 'bill_type_order_advance'
    
    order_no = 'filter_order_no'
    
    search = 'search_order_no'
    
    close = '(//*[@class="btn btn-warning"])[16]'
    
    Total_summary = 'tab_tot_summary'
    
    advance_amount = 'billing[bill_amount]'
    
    Make_payment = 'tab_make_pay'
    
    PAN_No = 'pan_no'
    
    Adhaar_no = 'aadhar_no'
    
    Driving_lic_No = 'dl_no'
    
    Passport_no = 'pp_no'
    
    Credit = 'card_detail_modal'
    
    Received = 'billing[tot_amt_received]'
    
    credit_due_date = 'credit_due_date'
    
    Cash = 'make_pay_cash'
    
    Credit_card = 'card_detail_modal'
    
    Add_credit_card = 'new_card'
    
    card_name = 'card_details[card_name][]'
    
    card_type = 'card_details[card_type][]'
    
    Device_name = 'card_details[id_device][]'
    
    card_No = 'card_details[card_no][]'
    
    card_amount = 'card_details[card_amt][]'
    
    approval = 'card_details[ref_no][]'
    
    credit_pagr_save = 'add_newcc'
    
    cheque = 'cheque_modal'
    
    add_cheque = 'new_chq'
    
    cheque_Date = 'cheque_details[cheque_date][]'
    
    bank = 'cheque_details[id_bank][]'
    
    cheque_no = 'cheque_details[cheque_no][]'
    
    cheque_amount = 'cheque_details[payment_amount][]'
    
    cheque_page_save = 'add_newchq'
    
    net_banking = 'net_bank_modal'
    
    net_banking_type = 'nb_details[nb_type][]'
    
    net_bank = 'nb_details[id_bank][]'
    
    payment_date = 'nb_details[nb_date][]'
    
    Referral_no = 'nb_details[ref_no][]'
    
    net_banking_amount = 'nb_details[amount][]'
    
    net_bank_page_save = 'add_newnb'
    
    
    
    billing_save = 'pay_submit'