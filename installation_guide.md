# Installation Guide
Now that you have cloned our repository follow these steps to run the **Hostelbook** in your local server.
* **Install database** :- 
    ```
    #~/social-network/>>
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
    ```
* **Create database using default user postgres** :- 
    * Enter password (remember this) for postgres
    ```
    sudo passwd postgres
    ```
    * Switch to user postgres and create a database named **postgres** if its already not there.
    ```
    su - postgres
    createdb postgres
    psql -d postgres -c "ALTER USER postgres WITH PASSWORD '123';"
    ```
    * If you don't want to switch
    ```
    sudo -u postgres createdb postgres
    sudo -u postgres psql -d postgres -c "ALTER USER postgres WITH PASSWORD '123';"
    ```
    * Switch back to your normal account
    * Migrate database
    ```
    python manage.py migrate
    sudo python manage.py runserver 0.0.0.0:80
    ```
    * Port forward to make this accessible from outside internet
    * You can also deploy this website using the above steps (without port forwarding) to deploy it in a Cloud Virtual Machine like Google Cloud Platform : Compute Engine : VM Instance : Ubuntu 16.04 and access the website through the VM's external IP.
