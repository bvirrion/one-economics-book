#!/bin/bash
# Kill any process over 4 GB whose working directory is in the economics book repo. Exits after a kill, so that the session hears of it.
REPO=$(cd "$(dirname "$0")/.." && pwd)
LOG=${MEMWATCH_LOG:-/tmp/memwatch.log}
LIMIT_KB=$((4*1024*1024))
peak=0
while true; do
  while read -r pid rss comm; do
    [ "$rss" -gt "$peak" ] && { peak=$rss; echo "$(date '+%F %H:%M:%S') new peak $((rss/1024)) MB pid $pid $comm" >> "$LOG"; }
    [ "$rss" -gt "$LIMIT_KB" ] || continue
    case "$comm" in claude|node|rust-analyzer*|mysqld) continue;; esac
    cwd=$(readlink "/proc/$pid/cwd" 2>/dev/null)
    case "$cwd" in "$REPO"*) ;; *) continue;; esac
    args=$(tr '\0' ' ' < "/proc/$pid/cmdline" | cut -c1-160)
    kill -9 "$pid" && { echo "$(date '+%F %H:%M:%S') KILLED pid $pid $((rss/1024)) MB in $cwd: $args" | tee -a "$LOG"; exit 3; }
  done < <(ps -eo pid=,rss=,comm= --sort=-rss | awk '{print} NR==6{exit}' | grep -v -E " (claude|node)$")
  sleep 5
done
