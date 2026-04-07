css_vars = """
--widget-background-color: {{colors.primary_container.default.hex}};
--widget-background-opacity: 100%;
--popover-background-opacity: 100%;
--widget-hover-tint: white;
--color-accent-primary: {{colors.primary.default.hex}};
/* ===== Background Colors ===== */
/* Bar background with opacity applied via color-mix */
--bar-icon-color: {{colors.on_background.default.hex}};
--color-background-bar:  {{colors.background.default.hex_alpha | set_alpha: 0.6}};
--popover-bg: {{colors.secondary_container.default.hex_alpha | set_alpha: 0.6}};
/* ===== Foreground Colors ===== */
--color-foreground-primary: {{colors.on_secondary_container.default.hex}};
--color-foreground-muted: {{colors.on_secondary_container.default.hex | set_alpha: 0.6}};
--color-foreground-disabled:  {{colors.on_secondary_container.default.hex | set_alpha: 0.4}};
--color-foreground-faint: {{colors.on_secondary_container.default.hex | set_alpha: 0.3}};

/* ===== Accent Colors ===== */
--color-accent-primary: {{colors.primary.default.hex}};
--color-accent-subtle: color-mix(in oklab, {{colors.primary.default.hex}} 20%, transparent);
/* Slider accent - alias for user CSS overrides */
--color-accent-slider: {{colors.primary.default.hex}};
--color-accent-text: {{colors.on_primary.default.hex}};
--color-accent-hover-bg: color-mix(in oklab, {{colors.primary.default.hex}} 80%, black);

/* ===== State Colors ===== */
--color-state-success: #4a7a4a;
--color-state-warning: #e5c07b;
--color-state-urgent: #ff6b6b;

/* ===== Card Overlays ===== */
--color-card-overlay: {{colors.secondary.default.hex_alpha | set_alpha: 0.15}};
--color-card-overlay-hover: {{colors.secondary.default.hex_alpha | set_alpha: 0.07}};
--color-card-overlay-subtle: {{colors.secondary.default.hex_alpha | set_alpha: 0.03}};
--color-card-overlay-strong: {{colors.secondary.default.hex_alpha | set_alpha: 0.15}};
--color-click-catcher-overlay: rgba(128, 128, 128, 0.01);

/* ===== Borders & Shadows ===== */
--color-border-subtle: {{colors.outline.default.hex_alpha | set_alpha: 0.2}};
--shadow-soft: 0 1px 2px rgba(0, 0, 0, 0.2), 0 1px 3px rgba(0, 0, 0, 0.24);
--shadow-strong:
    0 1px 2px rgba(0, 0, 0, 0.2), 0 1px 5px rgba(0, 0, 0, 0.24);

/* ===== Slider Tracks ===== */
--color-slider-track: rgba(255, 255, 255, 0.15);
--color-slider-track-disabled: rgba(255, 255, 255, 0.09);

/* ===== Contextual Backgrounds ===== */
--color-row-background: {{colors.secondary.default.hex_alpha | set_alpha: 0.2}};
--color-row-background-hover: {{colors.secondary.default.hex_alpha | set_alpha: 0.4}};
--color-row-critical-background: rgba(59, 34, 38, 0.95);
--color-toast-critical-background: rgba(106, 54, 54, 0.95);

/* ===== Radii ===== */
--radius-bar: 17px;
--radius-surface: 20px;
--radius-widget: 20px;
--radius-widget-lg: calc(20px * 2);
--radius-pill: 10px;
--radius-card: 20px; /* Cards/containers - never goes pill */
--radius-round: 9999px; /* Always circular */
--radius-factor: 0.8; /* 0.0 at 0%, 1.0 at 50%+ for fixed-size elements */

/* ===== Sizes & Spacing ===== */
--bar-margin: 0px;
--bar-height: 35px;
--bar-padding-y: 4px;
--bar-padding-y-bottom: 4px;
--widget-height: 34px;
--widget-padding-x: 7px;
--widget-padding-y: 2px;
--spacing-internal: 12px;
--spacing-widget-edge: 6px;
--spacing-widget-gap: 11px;
--widget-opacity: 1;

/* Spacing tokens - consistent spacing scale */
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 12px;
--spacing-lg: 16px;
--spacing-xl: 24px;

/* Component tokens */
--card-padding: var(--spacing-md);
--row-padding-v: var(--spacing-sm);
--row-padding-h: var(--spacing-md);

/* ===== Typography ===== */
--font-family: "LunchType22";
--font-scale: 0.6;
--font-size: calc(var(--widget-height) * var(--font-scale));
--font-size-text-icon: 26px;

/* Slider height - scales with widget height */
--slider-height: calc(var(--widget-height) * 0.25);
--slider-height-thick: calc(var(--widget-height) * 0.4);
--slider-knob-size: calc(var(--widget-height) * 0.65);
/* Slider radii - half of height, scaled by radius factor */
--slider-radius: calc(var(--widget-height) * 0.125 * 0.8);
--slider-radius-thick: calc(var(--widget-height) * 0.2 * 0.8);
--slider-knob-radius: calc(var(--widget-height) * 0.325 * 0.8);

/* Font size scale for visual hierarchy */
--font-size-lg: 1.1em; /* Headings, section titles */
--font-size-base: 1em; /* Primary content, main labels */
--font-size-md: 0.9em; /* Row titles, content that needs slight reduction */
--font-size-sm: 0.85em; /* Supporting content, secondary text */
--font-size-xs: 0.7em; /* De-emphasized (timestamps, week numbers) */

/* ===== Icon Sizes ===== */
--pixmap-icon-size: 26px;
/* Canonical icon box size for bar widgets - all icons sit in this size container */
--icon-size: 26px;

"""

input_css = open("templates/.config/vibepanel/default_css.css").read()

values = dict(i.split(":", 1) for i in css_vars.splitlines() if i.startswith("--"))
values = {i: j.split(";")[0].strip() for i, j in values.items()}
# print(values)

for _ in range(3):
    for value, replacement in values.items():
        # print(value, replacement)
        input_css = input_css.replace(f"var({value})", replacement)

with open("templates/.config/vibepanel/style.css", "w") as f:
    f.write(input_css)
