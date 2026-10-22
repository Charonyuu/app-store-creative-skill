---
name: app-store-creative
description: Create, revise, and validate high-conversion Apple App Store and Google Play listing screenshots, promotional store graphics, native launch/splash artwork, and app icons from real product captures and brand assets. Use when the agent is asked to make 商店圖, App Store screenshots, Play Store screenshots, store-listing creatives, screenshot sets, splash screens, launch screens, app icons, localized store visuals, or release-ready visual asset packages.
---

# App Store Creative

Build truthful, readable store assets from the real product. Treat listing screenshots, launch screens, and icons as different artifacts with different jobs. For portrait store screenshots, default to the proven editorial system in [references/portrait-editorial-system.md](references/portrait-editorial-system.md) instead of inventing a generic poster layout.

## Start with the correct artifact

- **Store screenshots:** sell one user benefit per frame. Marketing copy and composed scenes are allowed.
- **Launch / splash screen:** bridge app launch into the first screen. Keep it quiet, fast, crop-safe, and free of advertising copy or fake UI.
- **App icon:** create an immediately recognizable mark at tiny sizes. Avoid screenshot-like detail and small text.
- **Promotional graphic:** follow the current store-specific rules; never reuse it blindly as a screenshot or splash.

Read [references/portrait-editorial-system.md](references/portrait-editorial-system.md) and inspect its bundled reference images before making portrait store screenshots. Read [references/store-screenshot-playbook.md](references/store-screenshot-playbook.md) for narrative, capture, localization, and QA decisions. Read [references/prompt-recipes.md](references/prompt-recipes.md) before generating or editing raster assets. Read [references/splash-and-icon.md](references/splash-and-icon.md) when the task includes a launch screen or icon.

## Workflow

1. **Inspect the product and brand.** Find the app entry point, platforms, target locale, theme, mascot, logo, existing screenshots, and actual working features. Open relevant images before using them as references.
2. **Verify current requirements.** Browse official Apple or Google documentation for current sizes, counts, alpha rules, device families, and submission constraints. Specifications are time-sensitive; do not rely on memory.
3. **Capture real screens.** Prefer an iOS Simulator, Android Emulator, physical device, or the app's local browser. Use stable seeded data and hide dev controls. Never fabricate product capabilities or replace the core UI with generated UI.
4. **Choose the story.** Define the target audience, one promise for each frame, and the first-three-frame sequence. Remove redundant frames before decorating them.
5. **Build a frame brief.** Record the exact headline, support line, source screen, dominant UI region, mascot/brand role, feature accent, and required invariants for every frame before generating any frame.
6. **Approve the hero frame first.** Generate only frame 1, inspect it beside the bundled portrait references, and revise until hierarchy, product scale, text, and brand integration pass. Do not generate the rest of the set from an unapproved first frame.
7. **Lock the visual system.** Record typography scale, top zone, product-panel start, panel width, background treatment, mascot overlap, accent palette, and shadow/radius treatment from the approved hero frame.
8. **Generate one subsequent frame at a time.** Use three distinct inputs whenever available: the new real screen as the content source, the canonical mascot/brand asset as the identity source, and the previously approved store frame as the style/composition source. State these roles explicitly. Preserve the new product UI and transfer only the approved presentation system.
9. **Compare after every call.** Reject a frame if it looks like a different campaign, shrinks the UI, weakens the headline, changes product truth, or floats decorations without hierarchy. Make one targeted correction before moving on.
10. **Export exact deliverables.** Produce store-native dimensions, correct color mode, no unintended alpha, numbered filenames, and localized variants. Keep source captures and discarded drafts separate from finals.
11. **Validate visually and mechanically.** Inspect each final at full size and as a small thumbnail. Run `scripts/validate_store_assets.py` for PNG dimensions, count, numeric ordering, and alpha checks.
12. **Deliver a manifest.** List platform, device class, locale, dimensions, final filenames, source-screen mapping, generation prompt, approved style reference, and any claims that still need product/legal confirmation.

## Non-negotiable quality rules

- Use genuine app screens as the evidence layer; generated scenery must not invent buttons, results, pricing, testimonials, or unavailable features.
- Lead with the outcome, not the feature label. Keep one clear headline and at most one short supporting line per store screenshot.
- Make the first three screenshots understandable without reading the full listing.
- Make the product UI the largest visual mass in the lower portion; reject tiny device mockups and wide empty margins.
- Use a large top headline zone with no more than two lines. At thumbnail size the benefit must still be the first readable element.
- Integrate the brand character or graphic at the transition between headline and product panel; do not scatter it as unrelated clip art.
- Carry the previous approved frame into the next generation call as a style reference. A text-only reminder is not enough for a consistent multi-frame set.
- Keep important copy and faces away from rounded corners, Dynamic Island regions, and likely crop zones.
- Preserve readable Traditional Chinese or the requested locale; inspect every rendered character.
- Avoid pasting a flat phone screenshot onto a generic gradient. Use depth, hierarchy, and brand-specific visual cues.
- Do not accept the first technically valid generation. Compare against the reference system, revise a single issue, and inspect again.
- Do not turn the splash screen into a store ad. Richness should come from atmosphere, brand shapes, and motion-ready composition, not claims.
- Do not overwrite a working asset by default. Save a versioned candidate, compare it, then install it after inspection.

## Suggested project layout

```text
deploy/store-assets/
├── source-screens/
├── drafts/
├── app-store/iphone-6.9/
├── app-store/ipad-13/
├── play-store/phone/
├── splash/
├── app-icon/
└── asset-manifest.md
```

## Mechanical validation

For an iPhone screenshot folder, run:

```bash
python scripts/validate_store_assets.py <folder> \
  --width <official-width> \
  --height <official-height> \
  --min-count 3 \
  --max-count 10 \
  --forbid-alpha \
  --require-numbered
```

Use the official current dimensions discovered for the actual submission rather than copying example numbers from an older project.

## Completion standard

Do not finish after generation alone. Finish only when final assets are saved inside the target project, visually inspected, mechanically validated, and documented with a manifest. Report the final paths and which files were installed into the application bundle.
