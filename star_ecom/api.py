import frappe

@frappe.whitelist()
def place_order(products):
	print("Products:", products)
	if not products:
		frappe.throw("Can't Place Empty Order")
	current_user = frappe.session.user
	new_order = frappe.new_doc("Product Sales")
	new_order.user = current_user
	new_order.status = "Pending"
	new_order.set("items",products)
	new_order.insert(ignore_permissions=True)
	return new_order