# pygments-extra-styles
This package provides extra custom styles to [Pygments](https://pygments.org).

Extra styles:
1. sas_studio: Style inspired by SAS Studio.

## Installation:
Use `pipx` in your environment:
``` shell
pipx install "Pygments[pygments-extra-styles]"
pipx inject Pygments git+https://github.com/ywwry66/pygments-extra-styles.git
```

## Upgrading both `Pygments` and `pygments-extra-styles`:

``` shell
pipx upgrade --include-injected Pygments
```
