# Niri Dotfiles
These are my WIP Matugen template niri dotfiles. 

This repository is not meant to be used as is. Instead, it is meant to act as a dump for
templates I use for random software that I use that you can use freely with credit in your own themes. 

I do not provide a proper install script (for now) because I use some manually patched software that's always changing.

## Software Config Included 
- Alacritty (I don't use this and won't update it for now)
- Bottom
- Cliphist (only scripts for viewing history with Wofi + starting it on Niri boot)
- Fish (add `fish_config theme choose lily-matugen` into `~/.config/fish/config.fish`)
- Ghostty
- Gtk 3 and Gtk 4 (wip but usable)
- Gtk icons ([Midnight Sonata](<https://github.com/SethStormR/Midnight-Sonata>), but patched to be truly monochrome and a matugen template).
- Hyfetch (custom ascii logo in `.config/neofetch-logo`, does not configure to use it by default for obvious reasons)
- Lightdm (requires [`Waifu Greeter`](<https://github.com/anime-kun32/waifu-greeter>) theme and the `wallpaper.sh` script requires write permissions to `/usr/share/web-greeter/themes/waifu-greeter/assets/bg.jpg`)
- Niri (be careful there are some things that depend specifically on my current setup).
- Soteria (wip)
- Starship
- Swaylock
- Vesktop (heavily wip, far from perfect, select "Lily's stupid theme" and restart Vesktop completely)
- Vibepanel (note: might not work properly for you because I use a local fork that jankily patches it to barely work on Mint)
- Waybar (I don't use it anymore, won't update)
- Wlogout
- Wofi
- Zed (select "Lily's Matugen" theme in the theme toggle)

## Fonts
I heavily use [Lunchtype22](<https://fontesk.com/lunchtype-typeface/>) font for some themes and you will also need FiraCode fonts as well.

## Usage
All of the dotfiles can be installed with `sh wallpaper.sh path/to/wallpaper.png`.
This will override all of the dotfiles for equivalent programs you have.

The recommended use for this repo is to add/remove folders and files from the `templates` directory and then run the `wallpaper.sh`,
or even `just iterate /path/to/wallpaper` for a hot reloading workflow.
The `templates` folder acts as a proxy for your home directory.

This script generates a matugen config and then tells matugen to output all of the files directly to their corresponding path in home.
I do not use out of place symlinks because that constantly breaks apps that refuse to resolve symlinks.
