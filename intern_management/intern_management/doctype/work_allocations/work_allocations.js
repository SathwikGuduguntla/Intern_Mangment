frappe.ui.form.on('Work Allocations', {
    template: frappe.utils.debounce(function (frm) {
        if (frm.doc.template) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Work Template",
                    name: frm.doc.template
                },
                callback: function (r) {
                    console.log("Template response:", r.message);

                    if (r.message && r.message.task && r.message.task.length) {
                        frm.clear_table("task");

                        r.message.task.forEach(function (row) {
                            console.log("Copying row:", row);
                            let child = frm.add_child("task");
                            child.task = row.task_name;
                            child.due_date = row.due_date;

                        });

                        frm.refresh_field("task");
                    } else {
                        frappe.msgprint("No tasks found in the selected Work Template.");
                    }
                },
                error: function (err) {
                    console.error("Error fetching Work Template:", err);
                    frappe.msgprint("Failed to fetch template.");
                }
            });
        }
    }, 500)
});
