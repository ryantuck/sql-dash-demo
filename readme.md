# mvp sql dash

flask webserver for executing saved sql queries.

currently configured to run off a personal RDS instance with dummy databases.

## quickstart

1. `python main.py`
2. go to `localhost:5000`

## host your own

1. `psql -U username -h localhost -d target_db -f demo_tables.sql`
2. change `db_config.json` file to your own creds.

