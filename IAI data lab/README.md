# Steps:

1. Create connection to IBM Cloud Object Storage.
2. Import asset from Object Storage.
3. Import the Notebook.
4. Add the data to Notebook.
5. Run the Notebook.

## 1. Create connection to IBM Cloud Object Storage.

* On the project assets tab, click on the **"New asset +"** button.
* Select the **"Connection"** asset.
* Select **"IBM Cloud Object Storage"**.
* Fill the **Name** with **"iai-data"**.
* Under the "Connection details" fill the **Bucket** with **"iai-data"**.
* Fill the Login **URL** with **"s3.us-south.cloud-object-storage.appdomain.cloud"**.
* Copy the Json of the [connection credentials](https://cloud.ibm.com/objectstorage/crn%3Av1%3Abluemix%3Apublic%3Acloud-object-storage%3Aglobal%3Aa%2F540ab0b7636d4bbb90e829db0ac2bd82%3A1cb119cc-c83f-4319-83b8-ba1be099ef38%3A%3A) and paste it in the **"Service credentials"**.
* Click **"Create"**.

## 2. Import asset from Object Storage.

* On the project assets tab, click on the **"Import Assets"** button.
* Select the **"iai-data"** and select **"0807.csv"**.
* Click on **"Import"**.

## 3. Import the Notebook.

* On the project assets tab, click on the **"New asset +"** button.
* Select the **"Jupyter notebook editor"**.
* Select the **"From URL"** tab.
* Fill the **Name** with **"iai-data-notebook"**.
* Fill the ***"Notebook URL"** with this link: 
* Click **"Create"**.

## 4. Add the data to Notebook.

* Inside the Notebook click on the **"Find and add data"** icon (top right corner).
* Uner the 0807.csv click on **"Insert to code"**.
* Select **"pandas DataFrame"**.

## 5. Run the Notebook.

* Make sure the name of the DataFrame is **"df_data_1"**.
* Click **"Run"** button for each cell.