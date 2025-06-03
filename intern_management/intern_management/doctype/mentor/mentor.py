# Copyright (c) 2025, Sathwik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Mentor(Document):
    def validate(self):
        allowed_domains = ["@limendo.com"]
        
        if self.email:
            email = self.email.strip().lower()  
            
            if not any(email.endswith(domain) for domain in allowed_domains):
                frappe.throw("Email must end with your comapany name")