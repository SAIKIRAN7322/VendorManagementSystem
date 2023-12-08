# VendorManagementSystem

DESCRIPTION:
This project is for handling vendor profiles, track purchase orders, and calculate vendor performance metrics.
The Project name is fatmug
In this project,there are four apps namely,"vendormanagement"(for vendor related operations),"purchaseorder"(for purchaseorder related operations),"performancemetrics"(for vendor performance related operations),"accounts"(for user model related operations)
vendormanagement app consists of vendor model for storing data related to vendor,similarly purchaseorder consists purchaseorder model,performancemetrics consists performancemetrics model,accounts consists abstract user model
The apis related to all the apps are written in api folder of respective app.
The project was implemented using postgrese db consisting of user,vendor,purchaseorder,vendorperformancemetrics models

SETUP AND TESTING:
first create a python virtual environment(python -m venv [env name])
Then run the command pip install -r requirements.txt(for installing all the dependencies for starting the project)
Now set the database configurations according to your system by changing the database configurations in settings.py of project and apply all the migrations
Now set the path to project main folder(fatmug) and run the server using (python manage.py runserver)
Now the server is ready to take the requests
Now register a user using 'api/accounts/register' by passing name,email,password fields
Now generate a jwt auth token using 'api/accounts/api-token-auth' by passing username and password fields
Now use the access token obtained from previous response and call the following apis by passing jwt bearer token along with:

API endpoints:
get:"api/vendors/":for retrieving all the vendors list in the database
post:"api/vendors/":for creating a new vendor(fields:name,contact_details,address)
put:"api/vendors/<vendor_id>":for updating,deleting vendor object
get:"api/vendors/<vendor_id>/performance":for getting details of performance metricsss of a vendor
get:"api/purchase_orders/":for retrieving all the purchaseorders list in the database
post:"api/purchase_orders/":for creating a new purchaseorder(fields:"vendor",delivery_date","items","status","quality_rating","issue_date")
put:"api/purchase_orders/<purchaseorder_id>":for updating,deleting purchaseorder object
get:"api/purchase_orders/<purchaseorder_id>/acknowledge":for acknowledging a purchaseorder by vendor

NOTE:
You can test the above mentioned apis from the test cases written in the respective app's tests.py file by running python manage.py test {app_name} --> this will run tests for respective app api's
You can also test the api's from swagger ui whch can be opened using url "api/documentation"

