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
    
    
    
    MC_Type = '(//*[@class="form-control est_mc_type"])'
    
    Non_tag = 'select_catalog_details'
    
    section = '(//*[@role="presentation"])[8]'
    
    Product = '(//*[@role="presentation"])[10]'
    
    design = '(//*[@role="presentation"])[12]'
    
    Sub_design = '(//*[@role="presentation"])[14]'
    
    purity = 'est_catalog[purity][]'
    
    size = 'est_catalog[size][]'
    
    pcs = 'est_catalog[pcs][]'
    
    G_wt = 'est_catalog[gwt][]'
    
    Non_mc_type = '(//*[@class="form-control mc_type"])'
    
    mc_value = 'est_catalog[mc][]'
    
    wastage_percentage = 'est_catalog[wastage][]'
    
    home_bill_checkbox = 'select_custom_details'
    
    Tag = 'est_custom[tag_name][]'
    
    home_section = '(//*[@role="presentation"])[16]'
    
    home_size = 'est_custom[size][]'
    
    home_pcs = 'est_custom[pcs][]'
    
    home_G_wt = 'est_custom[gwt][]'
    
    home_mc = '(//*[@class="form-control cus_mc_type"])'
    
    home_mc_value = 'est_custom[mc][]'
    
    home_wastage_per = 'est_custom[wastage][]'
    
    old_metal = 'select_oldmatel_details'
    
    Metals = '(//*[@role="presentation"])[24]'
    
    Metals_Type = '(//*[@role="presentation"])[26]'
    
    Category =  '(//*[@role="presentation"])[28]'
    
    purity_metal = 'est_oldmatel[purity][]'
    
    metal_G_wt = 'est_oldmatel[gwt][]'
    
    metal_D_wt = 'est_oldmatel[dwt][]'
    
    metal_wastage_percentage = 'est_oldmatel[wastage][]'
    
    purpose = '(//*[@class="select2-selection__arrow"])[15]'
    
    Remark = 'est_oldmatel[old_metal_remarks][]'
    
    save_print = "est_print"
    
    billing_save = 'pay_submit'