# AI Subscription Plans , OpenAI and Anthropic

> Snapshot: 9 August 2026. Prices in USD, excluding tax, for consumer and team subscriptions to the chat products (ChatGPT and Claude). API token billing is not covered here.
> Reliability key: 🟢 primary research / authoritative , 🟠 serious journalism or institutional , 🔴 blog / vendor / low-quality journal.
> Source quality note: Anthropic figures come from the official pricing page (🟢). OpenAI blocks automated access to its pricing page, so ChatGPT figures come from tech press (🟠) and pricing aggregators (🔴). Verify before citing in a deck.

## Why this page exists

Students ask which plan they should pay for. The honest answer depends on what learning work they actually do, not on which tier has the biggest number. This page gives the raw grid first, then the part that matters pedagogically: a higher tier buys volume and speed, not better thinking on the learner's part. See [Cognitive Load Theory](cognitive_load_theory.md) for why a faster, more complete answer can be the expensive option.

## The grid

| Vendor | Plan | Monthly price | Annualised price | Target user | Model access / usage | Distinguishing features |
|---|---|---|---|---|---|---|
| OpenAI | Free | $0 | : | General public | Frontier model capped (order of 10 messages per 5 h), then automatic fallback to a lighter model | Web search, file and image analysis, limited image generation, limited voice. Contextual advertising in testing |
| OpenAI | Go | ~$8 | : | Price-sensitive markets (98 countries since Jan 2026, EU included) | Higher caps than Free on messages, uploads, images, memory length | Positioned against the free tier; may carry advertising depending on market |
| OpenAI | Plus | $20 | : | Standard individual | Advanced reasoning access, quotas around 160 messages per 3 h | Deep Research (tens of runs per month), custom GPTs, Projects, advanced voice, ad-free |
| OpenAI | Pro (Codex tier) | $100 | : | Developers, heavy agentic use | 5x the Codex usage of Plus; same model catalogue as the $200 tier | Introduced 9 April 2026 as a direct answer to Claude Max 5x. Difference from $200 is volume, not capability |
| OpenAI | Pro (top tier) | $200 | : | Power users | ~20x Plus, exclusive "Pro" model, extended context, high Deep Research quota | Effectively unlimited uploads and image generation |
| OpenAI | Business | $25 /seat | $20 /seat | Teams, 2 seat minimum | Broad usage on mainstream models | Shared workspaces, admin console, SSO, no training on business data. Price cut on 2 April 2026 (previously $30 / $25) |
| OpenAI | Enterprise | Custom | Custom | Large organisations | Negotiated allowances | SCIM, EKM, analytics, extended context, dedicated support, compliance |
| OpenAI | Edu | Custom | Custom | Universities | Negotiated | Institutional deployment, no public price |
| Anthropic | Free | $0 | : | General public | Reduced usage, subset of models | Web, mobile and desktop chat, web search, memory, file creation, connectors, extended thinking |
| Anthropic | Pro | $20 | $17 /month | Standard individual | Increased usage, rolling 5 h windows plus a weekly cap | Claude Code, Cowork, Design, Science, unlimited projects, Research, Microsoft 365 integration. Non-interactive usage credit: $20/month |
| Anthropic | Max 5x | $100 | : | Heavy use | 5x Pro usage, raised output limits | Early access to new features, priority during peak traffic. Non-interactive credit: $100/month |
| Anthropic | Max 20x | $200 | : | Power users | 20x Pro usage | Same feature set as Max 5x, separate weekly caps (all models / Sonnet only). Non-interactive credit: $200/month |
| Anthropic | Team, standard seat | $25 /seat | $20 /seat | Teams | More usage than Pro | Central billing, SSO, enterprise search, no training on content by default |
| Anthropic | Team, premium seat | $125 /seat | $100 /seat | Heavy-use teams | 5x the standard seat's usage | Same feature base, multiplied quota |
| Anthropic | Enterprise, self-serve | $20 /seat plus usage at API rates | : | Organisations | Seat plus variable consumption | Spend limits, RBAC, SCIM, audit logs, compliance API, data retention controls, IP allowlisting, HIPAA |
| Anthropic | Enterprise, sales-assisted | Custom | Custom | Large accounts | Volume commitments | Tailored MSAs, PO support, product bundling |
| Anthropic | Education | Custom | Custom | Universities | Negotiated | Student and faculty access, research credits, training resources |

## Reading the grid

Both catalogues have converged on the same ladder: free, ~$20, $100, $200, then a team seat around $20:25. OpenAI's $100 tier was introduced on 9 April 2026 and explicitly targets Claude Max 5x. The only real asymmetry is at the bottom: OpenAI has an $8 tier (Go), Anthropic has nothing between $0 and $20.

What the paid tiers buy, in order of how much they actually matter to a learner:

1. **Volume.** More messages before the cap. This is the main thing above $20.
2. **Latency and priority.** Access during peak hours.
3. **Agentic and coding quota.** The $100 and $200 tiers on both sides are largely sold on this. Irrelevant to most non-technical students.
4. **Model capability.** Real but smaller than the marketing suggests, and mostly concentrated in the top reasoning models.

Nothing in the ladder buys better learning. A student who pastes an assignment prompt into a $200 plan gets the same non-learning as on the free tier, faster.

## Caveats

Two points where sources disagree, and where nothing should be asserted without the official page:

- **Exact model names per tier for ChatGPT.** Aggregators cite GPT-5.3, 5.4 and 5.5 depending on when the article was written.
- **Message quotas.** OpenAI adjusts these without announcement. The figures above are observed orders of magnitude, not contractual commitments.

Not covered, because it is not a subscription: per-token API billing on both sides. It stacks with or replaces the subscription depending on plan, notably Anthropic's self-serve Enterprise, where the $20 seat does not cover consumption.

## Sources

| Source | Outlet | Reliability | Link |
|---|---|---|---|
| Claude pricing page | Anthropic | 🟢 Official vendor pricing | https://claude.com/pricing |
| OpenAI introduces ChatGPT Pro $100 tier with 5x Codex usage | VentureBeat, 9 Apr 2026 | 🟠 Tech journalism, quotes the OpenAI announcement | https://venturebeat.com/orchestration/openai-introduces-chatgpt-pro-usd100-tier-with-5x-usage-limits-for-codex |
| OpenAI adds new $100/month ChatGPT subscription tier | MacRumors, 9 Apr 2026 | 🟠 Tech journalism | https://www.macrumors.com/2026/04/09/openai-pro-subscription-tiers/ |
| ChatGPT pricing 2026: Free vs Go vs Plus vs Pro | CometAPI | 🔴 Vendor-adjacent aggregator, used only for tier structure | https://www.cometapi.com/chatgpt-pricing-2026-free-vs-go-vs-plus-vs-pro/ |
| ChatGPT Business pricing 2026 | Azterion | 🔴 Commercial blog, used only for the April 2026 Business price cut | https://azterion.com/en-us/chatgpt-for-business-pricing/ |
| Anthropic usage limits explained | tokenkarma | 🔴 Blog, used only for the 5x / 20x usage multipliers | https://tokenkarma.app/blog/anthropic-usage-limits-explained-2026/ |

## Maintenance

This page dates fast. Both vendors changed prices twice in the first half of 2026. Re-check the two official pricing pages before reusing these figures in teaching material, and update the snapshot date at the top when you do.
