import psycopg2

PGHOST='ep-small-grass-a4tf7qdb-pooler.us-east-1.aws.neon.tech'
PGDATABASE='nomina'
PGUSER='nomina_owner'
PGPASSWORD='npg_bgo8dWYUj5pm'

psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)


