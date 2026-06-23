#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TEMP_DIR=$(mktemp -d "${TMPDIR:-/tmp/}$(basename $0).XXXXXXXXXXXX")
IMAGE=$1

function die() {
    echo $1
    exit 1
}
if [ ! -f $IMAGE ]; then
    die "Invalid path: $1"
fi

function link() {
    local from=$1
    local to=$2
    echo "Linking $from -> $to"
    if [ -L $to ]; then
       unlink $to
    fi
    ln -s $from $to
}

function copy() {
    local from=$1
    local to=$2
    echo "Copying $from -> $to"
    local parent=$(dirname $to)
    if [ ! -d $parent ]; then
        echo "Creating dir $parent"
        mkdir -p $parent
    fi
    cp -r $from $to
}

# TODO: replace with my own app lmao
echo "Restarting swaybg"
pkill -9 swaybg
niri msg action spawn -- swaybg -i $1 -m fill

echo "Running matugen"
python ./gen/par-matugen.py ${SCRIPT_DIR}/build/matugen.toml image $IMAGE\
    -t scheme-tonal-spot --source-color-index 0 --contrast=0.3\
    || die "Failed to update templates (read above)"

echo "Updating icons, pywalfox, and fish"
pywalfox update
fish -c "fish_config theme choose lily-matugen"
gtk-update-icon-cache
gsettings set org.gnome.desktop.interface icon-theme "Midnight Sonata - Dark"
chmod +x ~/.config/niri/scripts/*

# Do not question the elevated one
declare -a SYMLINKS=("$HOME/.config/vesktop/themes/bg.png")
for i in "${SYMLINKS[@]}"
do
   link $1 $i
done

echo "Making cached jpeg background"
# Don't ask why this stupid piece of shit needs jpeg specifically
declare -a REQUIRES_JPEG=("/usr/share/web-greeter/themes/waifu-greeter/assets/bg.jpg")
CACHE_JPG="$TEMP_DIR/wallpaper.jpg"
convert $1 $CACHE_JPG
for i in "${REQUIRES_JPEG[@]}"
do
    copy $CACHE_JPG $i
done

echo "Refreshing vibepanel icons"
pkill -9 vibepanel && niri msg action spawn -- vibepanel
echo "Done"
