# Splash and Icon Guidance

## Launch / splash screen

The launch screen is a transition state, not a listing screenshot. It should appear immediately, crop safely, and hand off naturally to the first real screen.

Prefer:

- the same dominant background color as the initial app view;
- one centered brand mark or mascot;
- subtle abstract brand shapes, glow, or texture;
- generous negative space;
- important content within a central safe area that survives phone and tablet crops.

Avoid:

- feature claims, prices, slogans, CTAs, loading percentages, or fake controls;
- detailed scenes that imply the app is ready before it is;
- text close to Dynamic Island/notch/home-indicator zones;
- important decoration at edges;
- relying on one bitmap crop without checking multiple aspect ratios.

If a richer introduction is desired, keep the native launch screen restrained and build a separate, optional first-run onboarding animation after the app is interactive.

Always compare the launch artwork with the first rendered app frame. Sudden background, scale, or alignment changes make launch feel slower.

## App icon

Verify current official platform rules before export. In general:

- use one strong subject or mark;
- test at 29, 40, 60, 120, and 1024 px;
- remove small text and secondary props;
- preserve internal padding for platform masking;
- avoid baking a platform-shaped rounded-rectangle mask unless official guidance specifically requires it;
- export the required color profile and alpha behavior;
- inspect light/dark/tinted variants when the target OS supports them.

The icon, splash, and first store screenshot should feel related but should not be the same composition reused three times.
