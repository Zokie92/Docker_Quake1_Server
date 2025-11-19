#!/bin/bash
set -e

if [ ! -f /game/id1/pak0.pak ]; then
  echo "ERROR: /game/id1/pak0.pak saknas!"
  exec sleep infinity
fi

exec /usr/local/bin/quakespasm -dedicated +port 26000 +map start +set sv_maxclients 8
