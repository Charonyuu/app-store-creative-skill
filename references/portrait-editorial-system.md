# Portrait Editorial Store System

Use this as the default high-quality system for tall App Store or Play Store screenshots when the user has not supplied a stronger visual direction. It is derived from the approved QuokkaEnglish iPhone 6.9-inch set bundled under `assets/portrait-editorial-reference/`.

## Inspect the visual standard first

Before writing prompts, open at least these references with an image viewer:

- `assets/portrait-editorial-reference/01-home.png`
- `assets/portrait-editorial-reference/02-podcast.png`
- `assets/portrait-editorial-reference/03-speaking.png`
- `assets/portrait-editorial-reference/05-vocabulary.png`

Inspect all six when creating a complete set. Treat them as composition and quality references only. Do not copy Quokka characters, wording, colors, UI, or feature claims into another brand.

## Why this system works

- A huge benefit headline wins the thumbnail scan before the user reads details.
- The real product occupies almost the entire lower canvas, so the listing proves rather than merely claims.
- A character or brand graphic bridges marketing copy and product UI, making the composition feel integrated.
- Each feature gets a distinct accent while warm background texture, scale, type weight, radii, and shadows keep the set cohesive.
- The product panel continues to the bottom edge, creating depth and avoiding a small floating-device mockup.

## Layout ratios

Use ratios so the system adapts to current store dimensions. The Quokka reference masters are 1320 × 2868.

- Outer horizontal margin: 4–7% of canvas width.
- Headline zone: top 3–22% of canvas height.
- Headline: one or two lines, approximately 7–10% of canvas width in visual cap height, heavy weight, high contrast.
- Support line: one line when possible, approximately 2.8–4% of canvas width in visual cap height.
- Product-panel start: approximately 24–31% of canvas height.
- Product-panel width: approximately 90–96% of canvas width.
- Product content: extend to the bottom edge or deliberately crop beyond it; do not leave a large dead footer.
- Brand/mascot bridge: overlap the headline/product transition around 18–31% of canvas height.
- Decoration: keep below 10% of total visual attention and away from exact copy.

These are quality rails, not a mechanical template. Adjust for the source screen while preserving hierarchy.

## Visual grammar

- Start from a warm off-white or brand-neutral canvas rather than a saturated full-screen gradient.
- Add one feature accent family per frame: for example orange/home, sage/podcast, lavender/speaking, blue/vocabulary.
- Use two or three large soft shapes plus a few tiny feature cues. Avoid many equally weighted decorations.
- Use large rounded product containers, fine warm borders, and soft low-opacity shadows.
- Let the app's own UI remain detailed; keep the marketing layer simpler.
- Use a mascot action related to the feature when the brand has a character. Otherwise use a product-specific brand symbol, illustration, or visual metaphor.

## Set architecture

Plan the full sequence before generation:

1. Core daily value or transformation.
2. Most differentiated consumption/workflow feature.
3. Immediate proof or feedback loop.
4. High-retention interaction such as conversation, collaboration, or history.
5. Depth/content breadth.
6. Delight, challenge, or habit feature.

Change the sequence to match the product, but keep frames 1–3 focused on acquisition rather than completeness.

## Mandatory generation chain

### Frame 1

Use the real hero screen and canonical brand assets. Generate, inspect, and revise until it passes every quality gate below. Save the approved frame separately from drafts.

### Frames 2+

For each new frame, pass:

1. the new real app screen as the only UI/content source;
2. the canonical brand/mascot asset as the identity source;
3. the previous approved store frame as the only campaign-style reference.

Explicitly instruct the model to transfer composition, scale, texture, type hierarchy, depth, and density from input 3 while never copying its UI or claims. This visual chaining is required; repeating a text prompt alone does not reliably preserve the campaign.

Generate one frame per call. Do not ask one call to produce a six-frame board.

## Quality gates

Reject and revise if any gate fails:

- At a small thumbnail, the headline is not the first readable element.
- The headline exceeds two lines without a compelling language reason.
- The real product UI is narrower than roughly 88% of the canvas or feels like a small phone mockup.
- More than one quarter of the lower canvas is empty without a deliberate compositional reason.
- The mascot/brand element looks pasted on, covers key UI, or changes identity.
- The frame cannot sit beside the previous approved frame as the same campaign.
- Product text, values, navigation, feature state, or claims become materially false.
- Localized text contains malformed glyphs or unapproved wording.
- Decorations compete with the product or headline.

Correct only one failed gate per iteration and compare again.

## When image generation mutates the UI

First make a targeted edit that locks the authentic screen. If the model still changes important labels, numbers, navigation, pricing, or legal content, preserve the generated marketing shell but place the authentic screenshot deterministically into the approved product-panel mask. Product truth is more important than a fully generative composite.

## Deliverables

Keep:

- exact source captures;
- frame briefs;
- first-pass and revision prompts;
- approved style-chain reference for each frame;
- high-resolution masters;
- exact-size opaque finals;
- a manifest mapping every final to its authentic source screen.
