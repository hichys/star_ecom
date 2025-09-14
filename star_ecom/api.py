import frappe

@frappe.whitelist()
def place_order(products,city,delivery_request):
	print("Products:", products)
	if not products:
		frappe.throw("Can't Place Empty Order")
	current_user = frappe.session.user
	new_order = frappe.new_doc("Product Sales")
	new_order.user = current_user
	new_order.status = "Pending"
	new_order.city = city
	new_order.delivery_request = delivery_request
	new_order.set("items",products)
	new_order.grand_total = get_total_amount(products)
	new_order.insert(ignore_permissions=True)
	return new_order.name


def get_total_amount(items):
    total = 0
    for item in items:
        total += item.get("total", 0)
    return total