# Auto Shop product plan

## MVP (prototype included)
- Responsive landing and discovery UI
- Demo vehicle cards and local filters
- Australian units, currency and states
- API scaffold for vehicle listings
- PostgreSQL schema and local Docker setup

## Release 1 — data foundation
- Provider adapter interface for authorised feeds
- Normalise make/model/variant, VIN where lawfully supplied, odometer, location and seller type
- Deduplicate listings using provider IDs and probabilistic vehicle fingerprints
- Store source attribution, capture timestamp and listing status
- Data quality and freshness monitoring

## Release 2 — buyer intelligence
- Comparable-vehicle matching (variant, year, odometer, condition, location)
- Price range with confidence interval and sample size
- Price-change timeline only where snapshots are lawfully retained
- Explainable deal signals; avoid unsupported claims such as "best deal"
- PPSR link-out/check workflow and inspection checklist

## Release 3 — accounts and revenue
- Email/social authentication, saved vehicles and searches
- Alert preferences and notification queue
- Dealer workspace and team roles
- Subscription billing and invoices
- Admin moderation, support and audit trail

## Australian considerations
- Privacy Act 1988 and Australian Privacy Principles where applicable
- Australian Consumer Law: clear disclosures, no misleading valuation or availability claims
- Spam Act consent/unsubscribe requirements for marketing alerts
- Provider terms, copyright, database rights and contractual restrictions
- Security controls, retention policy, breach response and data access/deletion workflows

## Valuation principles
Never present an estimate as a guaranteed sale price. Show date, data coverage, comparable count, confidence band and exclusions. Do not infer accident history, finance status, write-off status or ownership history without a suitable authoritative check.
