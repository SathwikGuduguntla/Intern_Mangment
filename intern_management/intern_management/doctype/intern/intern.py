# Copyright (c) 2025, Sathwik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime



class Intern(Document):
    def validate(self):
        allowed_domains = ["@gmail.com", "@outlook.com"]
        
        if self.email_id:
            email_id = self.email_id.strip().lower()  
            
            if not any(email_id.endswith(domain) for domain in allowed_domains):
                        frappe.throw("Email must end with @gmail.com or @outlook.com")
           
       