#!/bin/bash

# def wide(path: str, n: int) -> int
# meant to fix aspect ratio issues with different text engines
wide() {
  if [ -f "$1" ]; then
    result=$(sed -e "s/\(.\)/\1$(printf '%*s' "$2")/g" "$1")
    echo "$result"
  else
    echo "$1 is not a file."
    return 1
  fi
}

wide "$1" "$2"
