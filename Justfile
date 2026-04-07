python := require("python")
matugen := require("matugen")

gen-templates image: gen-matugen-config
    @echo "Generating templates..."
    {{ justfile_directory() }}/wallpaper.sh {{ image }}

gen-matugen-config: show-matugen make-build
    {{ python }} gen/gen-matugen-config.py ./build/matugen.toml ./templates

show-matugen:
    @echo Found matugen at {{ matugen }}

iterate wallpaper: gen-matugen-config
    @python -c "print('wallpaper.sh', *__import__('glob').glob(f'templates/**/*', recursive=True, include_hidden=True), sep='\n',)"\
    | entr just gen-templates {{ wallpaper }}

make-build:
    mkdir -p build

clean:
    @rm -rf build
