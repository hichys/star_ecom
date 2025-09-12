// Copyright (c) 2025, awad mohamed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product Sales", {
    refresh(frm) {

    },
});

function calculate_grand_total(frm) {
    let grand_total = 0;
    frm.doc.items.forEach(item => {
        if (item.total)
            grand_total += item.total;
    });
    frm.set_value('grand_total', grand_total);
    frm.refresh_field('grand_total');
}
frappe.ui.form.on('Product Items', {
    refresh(frm, cdt, cdn) {
        // your code here
        //make total read only
        frm.set_df_property('total', 'read_only', 1);
        frm.set_df_property('qty', 'read_only', 1);
        frm.set_df_property('rate', 'read_only', 1);

    },
    // when qty chang update total
    qty(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (!row.rate)
            row.rate = 0;
        row.total = row.qty * row.rate;
        frm.refresh_field('items');
        // update grand total
        calculate_grand_total(frm);

    },
    rate(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (!row.qty)
            row.qty = 0;
        row.total = row.qty * row.rate;
        frm.refresh_field('items');
        calculate_grand_total(frm);

    }

})