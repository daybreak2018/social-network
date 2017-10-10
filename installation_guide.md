# Installation Guide
Now that you have cloned our repository follow these steps to run the **Hostelbook** in your local server.
* **Install database** :- 
    ```
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
    ```
* **Create database using default user postgres** :- 
    * Enter your desired password for postgres
    ```
    sudo psswd postgres
    ```
    * Switch to user postgres and create a database named **hostel**.
    ```
    su - postgres
    createdb hostel
    ```
    * If you don't want to switch
    ```
    sudo -u postgres createdb hostel
    ```
    * Switch back to your normal account
