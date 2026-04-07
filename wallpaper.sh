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

echo "Restarting swaybg"
# touch -m ~/.config/waybar/style.css
pkill -9 swaybg
niri msg action spawn -- swaybg -i $1 -m fill

echo "Running matugen"
python ./gen/par-matugen.py ${SCRIPT_DIR}/build/matugen.toml image $IMAGE\
    -t scheme-fidelity --resize-filter gaussian \
    --source-color-index 0 || die "Failed to update templates (read above)"

fish -c "fish_config theme choose lily-matugen"
gtk-update-icon-cache
gsettings set org.gnome.desktop.interface icon-theme "Midnight Sonata - Dark"
chmod +x ~/.config/niri/scripts/*

declare -a SYMLINKS=("$HOME/.config/vesktop/themes/bg.png")
declare -a REQUIRES_JPEG=("/usr/share/web-greeter/themes/waifu-greeter/assets/bg.jpg")
for i in "${SYMLINKS[@]}"
do
   link $1 $i
done

CACHE_JPG="$TEMP_DIR/wallpaper.jpg"
echo "Making cached jpeg background"
convert $1 $CACHE_JPG
for i in "${REQUIRES_JPEG[@]}"
do
    copy $CACHE_JPG $i
done
echo "Refreshing vibepanel icons"
pkill -9 vibepanel && niri msg action spawn -- vibepanel
echo "Done"
