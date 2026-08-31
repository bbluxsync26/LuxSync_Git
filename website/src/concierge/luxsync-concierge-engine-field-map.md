# LuxSync Concierge Engine Field Map

Stable IDs below should be treated as API contracts once the production form launches.

| Stage | Field ID | Type | Required | Prompt | Conditional Logic |
|---|---|---|---|---|---|
| welcome | entry_action | single_select | Yes | Let’s design how your space lives. | {} |
| intent | primary_intent | single_select | Yes | What brought you to LuxSync today? | {} |
| intent | desired_outcomes | multi_select | Yes | What would make your space feel more intelligent? | {} |
| property | property_type | single_select | Yes | What type of space are we designing? | {} |
| property | residence_type | single_select | Yes | What type of residence? | {"property_type": ["private_residence"]} |
| property | str_property_type | single_select | Yes | Tell us about the rental property. | {"property_type": ["short_term_rental"]} |
| property | business_type | single_select | Yes | What type of business or commercial space? | {"property_type": ["business"]} |
| property | property_description | text | Yes | Tell us about the space. | {"property_type": ["other"]} |
| property | square_feet_exact | number | No | Approximate square footage | {} |
| property | square_feet_band | single_select | No | Or choose a range | {} |
| property | levels | single_select | No | How many levels? | {"property_type": ["private_residence", "short_term_rental"]} |
| property | scope | single_select | No | Are you looking at the whole property or specific areas? | {"property_type": ["private_residence"]} |
| property | priority_rooms | multi_select | No | Where should we focus first? | {"scope": ["specific_rooms", "both"]} |
| property | str_unit_count | number | Yes | How many rental units are involved? | {"property_type": ["short_term_rental"]} |
| property | str_booking_platforms | multi_select | No | How do guests typically book? | {"property_type": ["short_term_rental"]} |
| property | str_remote_management | single_select | No | Do you manage the property remotely? | {"property_type": ["short_term_rental"]} |
| property | str_goals | multi_select | No | What are you most interested in improving? | {"property_type": ["short_term_rental"]} |
| property | business_location_count | number | No | How many locations are involved? | {"property_type": ["business"]} |
| property | business_goals | multi_select | No | What would you most like to improve? | {"property_type": ["business"]} |
| technology | technology_profile | multi_select | Yes | Tell us what’s already smart. | {} |
| technology | smartthings_hub_status | single_select | No | Do you currently use a SmartThings Hub or hub-enabled Samsung device? | {"technology_profile": ["smartthings"]} |
| technology | current_setup_health | single_select | Yes | How well is your current setup working? | {} |
| lifestyle | arrival_preferences | multi_select | No | When you arrive, what would you love to happen automatically? | {} |
| lifestyle | departure_preferences | multi_select | No | When everyone leaves, what should the property take care of? | {} |
| lifestyle | evening_preferences | multi_select | No | What should your space feel like as the day winds down? | {} |
| lifestyle | bedtime_preferences | multi_select | No | What would make bedtime more effortless? | {} |
| lifestyle | morning_preferences | multi_select | No | How would you like your space to wake up? | {} |
| lifestyle | entertainment_preferences | multi_select | No | How do you enjoy entertainment at home? | {"desired_outcomes": ["entertainment"], "arrival_preferences": ["entertainment"], "evening_preferences": ["entertainment"]} |
| lifestyle | pain_points | multi_select | Yes | What frustrates you about your space today? | {} |
| lifestyle | accessibility_needs | multi_select | No | Which everyday activities would you like technology to make easier? | {"desired_outcomes": ["accessibility"]} |
| priorities | priority_rank | ranked_select | Yes | If LuxSync could improve three things first, what matters most? | {} |
| priorities | implementation_preference | single_select | Yes | How would you like to approach your smart-living plan? | {} |

## Implementation Notes

- Keep presentation copy separate from stable answer values.
- Store exact square footage when supplied; otherwise preserve the selected band.
- Do not require customers to identify a hub or protocol before Blueprint generation.
- Device/product compatibility belongs in a separately maintained catalog.
- Preserve incomplete sessions where practical.
- Every displayed recommendation should include a human-readable “Why LuxSync Chose This” explanation.
- `support@luxsync.net` handles support; `info@luxsync.net` handles general and consultation inquiries.
