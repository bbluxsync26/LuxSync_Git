# CL-002 — VIP Account Access Review

**Status:** Active  
**Use:** Review any LuxSync login, account-creation, password-recovery, verification, or post-login welcome implementation before production release.

## Approved Brand Assets

- [ ] Desktop uses `brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png` where a horizontal mark is appropriate.
- [ ] Mobile/compact account access uses `brand/assets/01-logos/LuxSync_Logo_Orb.png` where appropriate.
- [ ] `LuxSync_Logo_Horizontal_Final.png` is used only when the extended horizontal composition fits the available space.
- [ ] No logo has been redrawn, retyped, recolored, regenerated, simplified, or substituted.
- [ ] No AI-generated logo appears anywhere in the auth experience.

## Page Architecture

- [ ] Desktop uses the approved two-zone welcome/auth composition.
- [ ] Welcome zone feels atmospheric and premium without overpowering the form.
- [ ] Auth card is vertically centered with generous breathing room.
- [ ] Card width remains roughly within `360–480px`.
- [ ] Mobile collapses cleanly to one column.
- [ ] Mobile does not preserve a forced desktop split-screen layout.
- [ ] Software keyboard does not trap the primary action below an inaccessible viewport.

## VIP Experience

- [ ] Every ordinary customer receives the same high-care visual treatment.
- [ ] Headline is calm and welcoming, such as `Welcome Back`.
- [ ] Messaging does not imply artificial status tiers, exclusivity, or scarcity.
- [ ] Support/help path is easy to find.
- [ ] Post-login destination continues the same quality level instead of dropping into generic UI.

## Typography

- [ ] Headings, buttons, labels requiring display emphasis use Manrope 500/600.
- [ ] Body, helper, form, and supporting copy use Inter 400/500.
- [ ] Logo lettering is never recreated with a font.

## Plush Drift Tactile Illumination

- [ ] Rest state uses faint concealed underlight.
- [ ] Hover subtly widens/brightens the underlight.
- [ ] Keyboard focus is at least as clear as mouse hover.
- [ ] Focus includes a visible non-glow focus indicator.
- [ ] Press state visually compresses by about 1–2px where motion is allowed.
- [ ] Pressed state tightens the shadow and modestly increases concealed light.
- [ ] Release is calm, roughly 140–220ms, with no spring/bounce.
- [ ] Reduced-motion mode removes unnecessary physical travel.
- [ ] No neon, flashing, aggressive bloom, cyberpunk glow, or hard glowing outlines.
- [ ] Glow is never the only interaction/state cue.

## Color and Metallic Treatment

- [ ] Slate Navy anchors the page canvas.
- [ ] Dark Suede anchors the auth card/control surfaces.
- [ ] Pale Driftwood provides primary readable light copy.
- [ ] Warm Taupe Mauve supports helper/secondary copy.
- [ ] Dusty Steel is the preferred cool concealed underlight.
- [ ] Champagne Rose Gold is restrained to reflected edges, tiny dividers, or micro-detail.
- [ ] Metallic gradients are not used as dominant form backgrounds or large live-text fills.

## Inputs and Forms

- [ ] Every field has a semantic/programmatic label.
- [ ] Placeholder text is not the sole label.
- [ ] Show/hide-password control has an accessible name.
- [ ] Password manager/autofill behavior is preserved.
- [ ] Focus does not resize or jump the input.
- [ ] Filled/valid state does not rely on color alone.
- [ ] Error state includes linked text/icon guidance and does not rely on red alone.
- [ ] No shake animation or flashing error state.
- [ ] Disabled controls accurately expose disabled semantics.

## Login Flow

- [ ] Sign-in behavior uses the actual approved production account integration.
- [ ] Static prototype code does not collect or transmit real credentials.
- [ ] Authentication failure copy is calm and does not leak unnecessary security detail.
- [ ] Remember-me appears only if supported by the real platform.
- [ ] No unsupported Apple/Google/Microsoft/social-login button has been invented.

## Password Recovery

- [ ] Recovery messaging avoids revealing whether an account exists for a specific address.
- [ ] Confirmation uses security-safe wording such as `If an account matches that address...`.
- [ ] Recovery UI uses the same Plush Drift card/control language.
- [ ] Support route remains available.

## Create Account

- [ ] Account creation collects only information required by the actual production account/commerce platform.
- [ ] Property-profile or marketing questions are not silently added to credential creation.
- [ ] Privacy/terms links are real and approved before requiring agreement.
- [ ] Create-account messaging feels like a warm invitation, not a funnel trick.

## Verification / MFA

- [ ] Verification controls appear only if the production platform supports/requires them.
- [ ] Six-code UI or equivalent follows the real platform contract.
- [ ] Paste/autofill support is preserved where available.
- [ ] Resend guidance is clear.
- [ ] No aggressive countdown pressure language.
- [ ] No invented MFA method, passkey flow, or provider.

## Auth Graphics

- [ ] Production ambient graphics come only from production-approved entries in `website/assets/auth/manifest.json`.
- [ ] `login-vip-hero.svg` remains behind live HTML copy.
- [ ] `login-vip-hero-mobile.svg` is used only as ambient/decorative mobile art.
- [ ] `member-access-ambient.svg` remains decorative and non-interactive.
- [ ] `account-welcome-banner.svg` contains no customer-specific text baked into the graphic.
- [ ] `auth-card-reference.svg`, `auth-input-states.svg`, and `auth-button-states.svg` are not published as functional controls.

## Accessibility

- [ ] WCAG 2.2 AA-oriented contrast has been reviewed.
- [ ] Full keyboard path works.
- [ ] Visible focus works in light/dark/metallic contexts.
- [ ] Touch targets are at least 44px.
- [ ] Errors are programmatically associated with fields.
- [ ] Decorative imagery is hidden from assistive technology appropriately.
- [ ] Reduced-motion preference is respected.
- [ ] State does not rely on color, glow, or motion alone.

## Security / Commerce Boundary

- [ ] GoDaddy Commerce Plus remains the account/commerce authority unless an explicit decision changes it.
- [ ] No password storage or custom credential backend was created merely to match the visual design.
- [ ] Session, token, authorization, password, MFA, and identity policies come from the real production platform/security design.
- [ ] No credentials, tokens, API keys, or customer data are committed to the repository.

## Result

**Pass / Needs Revision:** ____________________

**Major issues:**

- 
- 
- 

**Approved states:**

- 
- 
- 

**Integration items still pending:**

- 
- 
- 
