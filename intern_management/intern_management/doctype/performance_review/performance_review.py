# Copyright (c) 2025, Sathwik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime


class PerformanceReview(Document):

	def before_insert(self):
		if not self.review_date:
			self.review_date = now_datetime()
