from . import __version__ as app_version

app_name = "dsc_erpnext"
app_title = "Dsc Erpnext"
app_publisher = "Extension"
app_description = "Dsc Erpnext"
app_email = "hello@extensioncrm.com"
app_license = "MIT"






doc_events = {
	"*": {
		"on_submit": "dsc_erpnext.api.on_submit",
	},
	"DSC Purchase Order":{
		"validate":"dsc_erpnext.dsc_api.validate"
	},
	"DSC Sales Invoice":{
		"validate":"dsc_erpnext.dsc_api.validate"
	}
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dsc_erpnext/css/dsc_erpnext.css"
# app_include_js = "/assets/dsc_erpnext/js/dsc_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/dsc_erpnext/css/dsc_erpnext.css"
# web_include_js = "/assets/dsc_erpnext/js/dsc_erpnext.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dsc_erpnext/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "dsc_erpnext.utils.jinja_methods",
#	"filters": "dsc_erpnext.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dsc_erpnext.install.before_install"
# after_install = "dsc_erpnext.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dsc_erpnext.uninstall.before_uninstall"
# after_uninstall = "dsc_erpnext.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dsc_erpnext.utils.before_app_install"
# after_app_install = "dsc_erpnext.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dsc_erpnext.utils.before_app_uninstall"
# after_app_uninstall = "dsc_erpnext.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dsc_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"dsc_erpnext.tasks.all"
#	],
#	"daily": [
#		"dsc_erpnext.tasks.daily"
#	],
#	"hourly": [
#		"dsc_erpnext.tasks.hourly"
#	],
#	"weekly": [
#		"dsc_erpnext.tasks.weekly"
#	],
#	"monthly": [
#		"dsc_erpnext.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "dsc_erpnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "dsc_erpnext.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "dsc_erpnext.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dsc_erpnext.utils.before_request"]
# after_request = ["dsc_erpnext.utils.after_request"]

# Job Events
# ----------
# before_job = ["dsc_erpnext.utils.before_job"]
# after_job = ["dsc_erpnext.utils.after_job"]

# User Data Protection
# --------------------


user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]




# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"dsc_erpnext.auth.validate"
# ]