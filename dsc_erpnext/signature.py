
import frappe
from crypt import crypt as _crypt
# from dsc_erpnext.dsc_api import get_envelope_definition, send_envelope
from frappe.utils import frappe, get_url
import requests
from urllib.parse import parse_qs, urlparse
import secrets, string
import urllib

# def get_signing_url(doctype, docname):
#   """
#   Retrieves access token, downloads PDF, creates DocuSign envelope,
#   and returns the signing URL.
#   """

#   # 1. Get DocuSign configuration
#   # (Replace with your configuration retrieval logic)
#   account_id = "4b3845f8-2f6c-4a11-9724-76691431dd56"
#   base_path = "https://demo.docusign.net"

#   # 2. Get DocuSign access token (if not already retrieved)
#   # (Replace with your access token retrieval logic)
#   access_token = "..."

#   # 3. Fetch document details
#   doc = frappe.get_doc(doctype, docname)

#   # 4. Access the PDF document
#   pdf_url = doc.pdf_document
#   if not pdf_url:
#     # Construct downloadable PDF URL if needed
#     pdf_url = get_url(
#         path=doc.pdf_document,
#         doctype=doc.document_type,
#         name=doc.document
#     )

#   # 5. Download PDF content
#   response = requests.get(pdf_url, stream=True)
#   pdf_content = response.content

#   # 6. Create DocuSign envelope definition
#   envelope_definition = get_envelope_definition(
#       pdf_content,
#       # Add signer information, email, name, and signature location(s)
#       # based on your document or ERPNext configuration
#   )

#   # 7. Send the envelope and get signing URL
#   signing_url = send_envelope(account_id, base_path, access_token, envelope_definition)

#   return signing_url



def get_docusign_credentials(doc_name="Docusign Settings"):
  """
  Fetches DocuSign credentials from a custom DocType.

  Args:
      doc_name (str, optional): Name of the DocType storing credentials. Defaults to "Docusign Settings".

  Returns:
      dict: Dictionary containing DocuSign credentials (account_id, secret_key, base_path).
          If DocType is not found or there's an error, returns an empty dictionary.
  """
  try:
    doc = frappe.get_doc(doc_name)
    if doc:
      return {
          "account_id": doc.account_id,
          "secret_key": doc.get_password("secret_key"),
          "base_path": doc.base_path
      }
  except frappe.DocNotFoundError:
    print(f"DocType '{doc_name}' not found")
  except Exception as e:
    print(f"Error retrieving credentials: {e}")
  return {}

# Example usage
credentials = get_docusign_credentials()

if credentials:
  print("Hello")
#   access_token = get_docusign_access_token(**credentials)
  # Use access_token for DocuSign API calls
  # ...
else:
  print("Failed to retrieve credentials")

@frappe.whitelist()
def get_docusign_access_token(account_id=None, secret_key=None, base_path="https://account-d.docusign.com/oauth/auth", scope="signature", redirect_uri="http://0.0.0.0:8001/api/method/dsc_erpnext.dsc_apis.auth_login"):

  # Retrieve credentials from DocType if not provided
  if not account_id or not secret_key:
    credentials = get_docusign_credentials()
    if not credentials:
      return None  # Indicate failure to retrieve credentials

    account_id = credentials.get("account_id")
    secret_key = credentials.get("secret_key")
    state = state=generate_random_string()

  params = {
      "response_type": "token",
      "scope": scope,
      "client_id": account_id,
      "redirect_uri": redirect_uri,
      "state": state
  }

  oauth_url = f"{base_path}?{urllib.parse.urlencode(params)}"
  return oauth_url


@frappe.whitelist()
def generate_random_string(length=32):
  """
  Generates a cryptographically secure random string of specified length.

  Args:
      length (int, optional): Length of the random string. Defaults to 32.

  Returns:
      str: Random string of the specified length.
  """

  # Use secrets module for cryptographically secure random values
  return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(length))



