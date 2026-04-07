import sys


def main(argv) -> int:
    data = {}
    with open(argv[1], "w") as f:
        # for amount in range(10,100, 10):
        amount = 20
        for i in range(0, 16):
            name = "base0" + hex(i)[2:]
            data[name] = {
                "color": f"<* if {{{{ is_dark_mode }}}} *>{{{{base16.{name}.default.hex | lighten: {-amount}}}}} <*else*> {{{{base16.{name}.default.hex | lighten: {amount}}}}} <*endif*>"
            }
        print(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
