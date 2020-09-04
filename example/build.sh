#!/usr/bin/env sh

set -e

WORKDIR="${PWD}/gateapi-demo"
VENV_DIR="$WORKDIR/.venv"
: "${GATEAPI_SOURCE_DIR:=gateapi-python}"

# determine python environment
python=$(command -v python3 || true)

if [ -z "$python" ]; then
    python=$(command -v python2 || true)
    if [ -z "$python" ]; then
        echo >&2 "No python executable found."
        exit 1
    fi
fi

mkdir -p "$WORKDIR"

virtualenv=$(command -v virtualenv || true)
if [ -z "$virtualenv" ]; then
    echo "No virtualenv found. Native python environment will be used"
    LOCAL_INSTALL="--user"
else
    if [ -n "$VIRTUAL_ENV" ]; then
        # find original python path, osx compatible
        while true; do
            orig=$(readlink "$python")
            if [ -z "$orig" ]; then
                break
            elif [ "$orig" != "${orig#/}" ]; then
                python=$orig
                break
            else
                python="$(dirname "${python}")"/"$orig"
            fi
        done
    fi
    if [ ! -d "$VENV_DIR" ]; then
        "$virtualenv" -p "$python" "$VENV_DIR"
    fi
    python="$VENV_DIR/bin/python"
fi

echo "Python used: $python"

cd "$GATEAPI_SOURCE_DIR" && "$python" setup.py install ${LOCAL_INSTALL+"$LOCAL_INSTALL"} && cd -
cp "$GATEAPI_SOURCE_DIR"/example/*.py "$WORKDIR"

if [ -n "$virtualenv" ]; then
    echo "run \`source $VENV_DIR/bin/activate \` and then "
fi
echo "run \`cd $WORKDIR && $python app.py -h\` for help"
