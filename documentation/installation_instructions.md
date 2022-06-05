## Installation Instructions

### Prerequisites

* Python version 3.8 or up
* Postgresql database

### Configuration

Copy `src/.env.example` to `src/.env`.<br>
Set `DATABASE_URL` to PostgreSQL database connection string<br>
Set `SECRET_KEY` to application secret

### Running the program

##### 1. Install all dependencies

```
 pip3 install -r requirements.txt
```

##### 2. Go to src file
```
  cd src
```

##### 3. Start the application

```
  flask run
```


