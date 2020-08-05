# Flask Migration Tutorial
* `pip install Flask-Migrate`
* `from flask_migrate import Migrate`
* `migrate = Migrate(app, db)`
* `flask db init` -> create `migrations` folder at the root  
* `flask db migrate -m "Initial migration."` create 1st migration. It will COMPARE current database status (tables, views, ...) and Flask models to generate the migration UP and DOWN.  
* Edit the revision file as needed. Remember: Alembic currently does not detect every change you make to your models. Afterall, run `flask db upgrade`
* For help on commands: `flask db --help`  
    - `flask db upgrade [--sql] [--tag TAG] [--x-arg ARG] <revision>`: Upgrades the database. If revision isn’t given then "head" is assumed.
    - `flask db downgrade [--sql] [--tag TAG] [--x-arg ARG] <revision>`: Downgrades the database. If revision isn’t given then -1 is assumed.  
    - `flask db current [--verbose]`: Shows the current revision of the database.
    - `flask db history [--rev-range REV_RANGE] [--verbose]`: Shows the list of migrations. If a range isn’t given then the entire history is shown.
    - `flask db migrate [--message MESSAGE] [--sql] [--head HEAD] [--splice] [--branch-label BRANCH_LABEL] [--version-path VERSION_PATH] [--rev-id REV_ID]`: Equivalent to revision --autogenerate. The migration script is populated with changes detected automatically. The generated script should to be reviewed and edited as not all types of changes can be detected automatically. This command does not make any changes to the database, just creates the revision script.
