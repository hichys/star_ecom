import frappe

@frappe.whitelist()
def place_order(products,city,delivery_request,phone_number):
	try:
		print("Products:", products)
		if not products:
			frappe.throw("Can't Place Empty Order")
		current_user = frappe.session.user
		new_order = frappe.new_doc("Product Sales")
		new_order.user = current_user
		new_order.status = "Pending"
		new_order.city = city
		new_order.delivery_request = delivery_request
		new_order.phone_number = '+218-0920821334'
		new_order.set("items",products)
		new_order.grand_total = get_total_amount(products)
		new_order.insert(ignore_permissions=True)
		frappe.log_error("Error occurred in placing order", "Order Placement Error")
		return new_order.name
	except Exception as e:
		frappe.log_error(str(e)+" in placing order", "Order Placement Error")


def get_total_amount(items):
    total = 0
    for item in items:
        total += item.get("total", 0)
    return total

def phone_number():
	pass