## Create connection to Object Storage:

* On the project assets tab, click on the **"New asset +"** button.
* Select **"Connection"** and than **"IBM Cloud Object Storage"**.
* Fill **Name** as **"iai-data"**.
* Fill **Bucket** as **"iai-data"**.
* Fill **Login URL** as **"s3.us-south.cloud-object-storage.appdomain.cloud"**.
* From **Authentication method** select **"Service credentials"**
* Go to [Object storage](https://cloud.ibm.com/objectstorage/crn%3Av1%3Abluemix%3Apublic%3Acloud-object-storage%3Aglobal%3Aa%2F540ab0b7636d4bbb90e829db0ac2bd82%3A1cb119cc-c83f-4319-83b8-ba1be099ef38%3A%3A?paneId=manage) and click on **Service credentials**.
* Look for **"connection"** and **copy** it with the icon on the right side.
* Go back to the previous window and **paste** the credentials.
* Click on **"Create"**


## Import data to project:

* On the project assets tab, click on the **"Import assets"** button.
* Select **"iai-data"**.
* Select **"0807.csv"** and **"2007.csv"**.
* Click **Import**


## Run this notbook on Watson Studio:

* On the project assets tab, click on the **"New asset +"** button.
* Select the **"Jupyter notebook editor"**.
* Select the **"From URL"** tab.
* Fill the **Name** with **"iai-data-notebook"**.
* Fill the ***"Notebook URL"** with this link: https://raw.githubusercontent.com/tal2k4xj/iai-workshop/main/IAI%20data%20lab/real-iai-data.ipynb
* Click **"Create"**.
* Insert the data **"0807.csv"** and **"2007.csv"** from the **Find and add data** menu as **pandas DataFrame**.
* Change the **DataFrame** variabe to **"train_df"** and **"test_df"** accordingly.
* Click **"Run"** button for each cell.