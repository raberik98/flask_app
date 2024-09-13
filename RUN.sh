#!/run/current-system/sw/bin/bash

entry_file='app.py'

if [ "$#" -eq 0 ]; then
    echo '-----------------------------'
    echo '                             '
    echo 'venv:              get into the virtual environment';
    echo 'app:               run app';
    echo 'init:              flask-migration init';
    echo 'migrate:           create a migration';
    echo 'upgrade:           upgrade db';
    echo 'downgrade:         downgrade db';
    echo 'db:                start the db in Docker in non detached mode';
    echo 'dbd:               start the db in Docker in detached mode';
    echo 'backup:'           create a db backup;
    echo 'seed:'             populate the dv;
    echo '                             '
    echo '-----------------------------'
    
    exit 0
fi

if [ "$#" -ne 1 ]; then
    echo 'You can only pass 1 argument from bellow.'
    exit 1
fi

valid_args=('app' 'init' 'migrate' 'upgrade' 'downgrade' 'db' 'dbd' 'venv' 'backup' 'seed')

is_valid_arg() {
    local arg="$1"
    for valid in "${valid_args[@]}"; do
        if [ "$valid" == "$arg" ]; then
            return 0
        fi
    done
    return 1
}

if is_valid_arg "$1"; then
    if [ "$1" == "app" ]; then
        py app.py
    elif [ "$1" == "venv" ]; then
        source .venv/bin/activate
    elif [ "$1" == "init" ]; then
        flask db init
    elif [ "$1" == "migrate" ]; then
        flask db migrate
    elif [ "$1" == "upgrade" ]; then
        flask db upgrade
    elif [ "$1" == "downgrade" ]; then
        flask db downgrade
    elif [ "$1" == "db" ]; then
        docker run \
        -e POSTGRES_PASSWORD=password \
        -e POSTGRES_USER=admin \
        -e POSTGRES_DB=company \
        -p 5432:5432 postgres
    elif [ "$1" == "dbd" ]; then
        docker run \
        -e POSTGRES_PASSWORD=password \
        -e POSTGRES_USER=admin \
        -e POSTGRES_DB=company \
        -p 5432:5432 -d postgres
    elif [ "$1" == "backup" ]; then
        pg_dump -U admin -h 0.0.0.0 -p 5432 company > backup.sql
    elif [ "$1" == "seed" ]; then
        psql -U admin -d company -p 5432 -h 0.0.0.0 -f ./db/seed.sql
    else
        echo "Uhmm dude..."
    fi
else
    echo "Invalid argument: $1"
    echo "Please use one of these arguments:"
    echo "${valid_args[@]}"
    exit 1
fi



